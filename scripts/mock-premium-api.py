#!/usr/bin/env python3
"""A local stand-in for the game server's payment routes, to try the Premium page without the real server and without Stripe.

It serves the routes the page calls, with the answers and the CORS headers the real server gives (server/src/payment, server/src/main.rs `cors_origins`):

    POST /api/auth/login                       {username, password}            -> the token as plain text, or 400 "User not found." / "Wrong password."
    GET  /api/payment/status                   Bearer                          -> {username, isPremium, premiumUntil, paymentsOpen, subscription}
    POST /api/payment/create-checkout-session  Bearer, {product}               -> {url}
    POST /api/payment/portal                   Bearer                          -> {url}, or 404 "No subscription found."
    POST /api/payment/sync-session             Bearer, {session_id}            -> {status: "synced"} once the mock "Stripe" page below was paid

and a pretend Stripe (GET /stripe/checkout, /stripe/pay, /stripe/portal) that sends the browser back to the page's return URL with
?success=true&session_id=... or ?canceled=true, like Stripe Checkout does. Nothing here calls any real service.

Pilots (the password of every one is "pilotpass"):

    newbie      no Premium, no subscription          oneoff     Premium for 12 more days, no subscription
    supporter   Premium for 20 more days, subscribed  nopay      payments are not available (503 / paymentsOpen false)
    flaky       Stripe cannot be asked (subscription null)       busy       every payment call answers 503 "The Universe Wipe is running."
    banned      the login answers 403                  slow       a checkout takes three seconds

Run it:        python scripts/mock-premium-api.py --port 8787 --page http://127.0.0.1:8081
Look at it:    python -m http.server 8081   (in the repository root), then open  http://127.0.0.1:8081/premium/?api=http://127.0.0.1:8787
Self-test:     python scripts/mock-premium-api.py --selftest
"""
import argparse
import json
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PASSWORD = "pilotpass"
ALREADY_SUBSCRIBED = "You already have a subscription: cancel or change it under Manage subscription."
NOT_FOR_SALE = "This item is not for sale."
PRODUCTS = ("premium", "subscription")
# What the real server allows (Cors__ExtraOrigins defaults to the download site) besides the localhost development pages
BASE_ORIGINS = ["http://localhost:5173", "http://localhost:5174", "http://localhost:5175", "http://localhost:3000", "https://spacecorps.github.io"]


def now():
    return datetime.now(timezone.utc)


class World:
    """The pilots and the pretend Stripe sessions."""

    def __init__(self, port, page, origins, return_url):
        self.port, self.page, self.origins, self.return_url = port, page, origins, return_url
        self.lock = threading.Lock()
        self.pilots = {
            "newbie": dict(premium_until=None, subscription=False),
            "oneoff": dict(premium_until=now() + timedelta(days=12), subscription=False),
            "supporter": dict(premium_until=now() + timedelta(days=20), subscription=True),
            "nopay": dict(premium_until=None, subscription=False),
            "flaky": dict(premium_until=None, subscription=None),
            "busy": dict(premium_until=None, subscription=False),
            "banned": dict(premium_until=None, subscription=False),
            "slow": dict(premium_until=None, subscription=False),
        }
        self.sessions = {}  # id -> dict(user, product, paid)
        self.log = []

    def premium_active(self, pilot):
        until = pilot["premium_until"]
        return until is not None and until > now()


class Handler(BaseHTTPRequestHandler):
    world: World = None
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):  # quiet; the world keeps the log the self-test reads
        self.world.log.append(fmt % args)

    # ---- plumbing ----

    def origin_headers(self):
        origin = self.headers.get("Origin")
        if origin and origin in self.world.origins:
            return [
                ("Access-Control-Allow-Origin", origin),
                ("Access-Control-Allow-Credentials", "true"),
                ("Access-Control-Expose-Headers", "x-refreshed-token"),
                ("Vary", "Origin"),
            ]
        return []

    def reply(self, status, body="", content_type="text/plain; charset=utf-8", extra=()):
        data = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        for k, v in list(self.origin_headers()) + list(extra):
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(data)

    def reply_json(self, status, obj):
        self.reply(status, json.dumps(obj), "application/json")

    def body_json(self):
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b""
        try:
            return json.loads(raw or b"{}")
        except ValueError:
            return None

    def pilot(self):
        """(username, pilot) of the Bearer token, or None after answering 401."""
        auth = self.headers.get("Authorization", "")
        if auth.startswith("Bearer mock-"):
            name = auth[len("Bearer mock-"):]
            if name in self.world.pilots:
                return name, self.world.pilots[name]
        self.reply(401, "Your session expired, please sign in again.")
        return None

    # ---- CORS preflight, as tower-http answers it ----

    def do_OPTIONS(self):
        extra = []
        if self.origin_headers():
            extra = [
                ("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,OPTIONS"),
                ("Access-Control-Allow-Headers", "authorization,content-type"),
            ]
        self.reply(200, "", extra=extra)

    # ---- routes ----

    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        q = urllib.parse.parse_qs(url.query)
        if url.path == "/api/payment/status":
            return self.status()
        if url.path == "/stripe/checkout":
            return self.stripe_checkout(q)
        if url.path == "/stripe/pay":
            return self.stripe_pay(q)
        if url.path == "/stripe/portal":
            return self.reply(200, "<!doctype html><title>Mock Stripe portal</title><h1>Mock Stripe billing portal</h1>"
                                   f"<p><a href='{self.world.return_url}'>Return to the page</a></p>", "text/html; charset=utf-8")
        self.reply(404, "Not found")

    def do_POST(self):
        path = urllib.parse.urlparse(self.path).path
        routes = {
            "/api/auth/login": self.login,
            "/api/payment/create-checkout-session": self.checkout,
            "/api/payment/portal": self.portal,
            "/api/payment/sync-session": self.sync,
        }
        handler = routes.get(path)
        if handler is None:
            return self.reply(404, "Not found")
        handler()

    def login(self):
        body = self.body_json()
        if not isinstance(body, dict) or not isinstance(body.get("username"), str) or not isinstance(body.get("password"), str):
            return self.reply(422, "Failed to deserialize the JSON body")
        name = body["username"]
        if name not in self.world.pilots:
            return self.reply(400, "User not found.")
        if body["password"] != PASSWORD:
            return self.reply(400, "Wrong password.")
        if name == "banned":
            return self.reply(403, "Your account is suspended.")
        self.reply(200, "mock-" + name)

    def status(self):
        who = self.pilot()
        if not who:
            return
        name, pilot = who
        open_ = name != "nopay"
        sub = False if not open_ else pilot["subscription"]
        until = pilot["premium_until"]
        self.reply_json(200, {
            "username": name,
            "isPremium": self.world.premium_active(pilot),
            "premiumUntil": until.isoformat() if until else None,
            "paymentsOpen": open_,
            "subscription": sub,
        })

    def refuse_payment(self, name):
        if name == "nopay":
            self.reply(503, "Payments are not available on this server.")
            return True
        if name == "busy":
            self.reply(503, "The Universe Wipe is running.")
            return True
        return False

    def checkout(self):
        who = self.pilot()
        if not who:
            return
        name, pilot = who
        body = self.body_json()
        if self.refuse_payment(name):
            return
        product = body.get("product") if isinstance(body, dict) else None
        if body is None or (product is None and "item_id" not in body):
            return self.reply(400, "Choose a product.")
        if product not in PRODUCTS:
            return self.reply(400, NOT_FOR_SALE)
        if product == "subscription" and pilot["subscription"]:
            return self.reply(400, ALREADY_SUBSCRIBED)
        if name == "slow":
            time.sleep(3)
        with self.world.lock:
            sid = "cs_test_mock%d" % (len(self.world.sessions) + 1)
            self.world.sessions[sid] = dict(user=name, product=product, paid=False)
        # Stripe's own address in the real thing; this server's pretend checkout here
        self.reply_json(200, {"url": f"http://127.0.0.1:{self.world.port}/stripe/checkout?s={sid}"})

    def portal(self):
        who = self.pilot()
        if not who:
            return
        name, pilot = who
        if self.refuse_payment(name):
            return
        if not pilot["subscription"]:
            return self.reply(404, "No subscription found.")
        self.reply_json(200, {"url": f"http://127.0.0.1:{self.world.port}/stripe/portal"})

    def sync(self):
        who = self.pilot()
        if not who:
            return
        name, pilot = who
        if self.refuse_payment(name):
            return
        body = self.body_json() or {}
        session = self.world.sessions.get(body.get("session_id"))
        if session is None:
            return self.reply(400, "Stripe API failed to retrieve session")
        if session["user"] != name:
            return self.reply(400, "This payment does not belong to your user.")
        if not session["paid"]:
            return self.reply(400, "Payment not paid yet.")
        with self.world.lock:
            if not session.get("fulfilled"):
                session["fulfilled"] = True
                base = pilot["premium_until"] if self.world.premium_active(pilot) else now()
                pilot["premium_until"] = base + timedelta(days=30)
                if session["product"] == "subscription":
                    pilot["subscription"] = True
        self.reply_json(200, {"status": "synced"})

    # ---- the pretend Stripe ----

    def stripe_checkout(self, q):
        sid = (q.get("s") or [""])[0]
        if sid not in self.world.sessions:
            return self.reply(404, "No such session")
        ret = self.world.return_url
        sep = "&" if "?" in ret else "?"
        page = (
            "<!doctype html><meta charset=utf-8><title>Mock Stripe Checkout</title>"
            "<body style='font:16px system-ui;background:#fff;color:#222;max-width:420px;margin:40px auto;padding:0 16px'>"
            f"<h1>Mock Stripe Checkout</h1><p>Session {sid} ({self.world.sessions[sid]['product']}). No money moves here.</p>"
            f"<p><a id=pay href='/stripe/pay?s={sid}'>Pay (pretend)</a></p>"
            f"<p><a id=cancel href='{ret}{sep}canceled=true'>Cancel and go back</a></p></body>"
        )
        self.reply(200, page, "text/html; charset=utf-8")

    def stripe_pay(self, q):
        sid = (q.get("s") or [""])[0]
        session = self.world.sessions.get(sid)
        if session is None:
            return self.reply(404, "No such session")
        session["paid"] = True
        ret = self.world.return_url
        sep = "&" if "?" in ret else "?"
        self.send_response(302)
        self.send_header("Location", f"{ret}{sep}success=true&session_id={sid}")
        self.send_header("Content-Length", "0")
        self.end_headers()


def serve(port, page, extra_origins, return_url):
    origins = list(BASE_ORIGINS) + [page] + list(extra_origins)
    world = World(port, page, origins, return_url or page.rstrip("/") + "/premium/")
    Handler.world = world
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    return server, world


# ---- the self-test: the same checks a browser would depend on -----------------------------------------------------------------------------------------

def selftest():
    page = "http://127.0.0.1:8081"
    server, world = serve(0, page, [], None)
    world.port = server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{world.port}"
    fails = []

    def call(method, path, body=None, token=None, origin=None, headers=None):
        req = urllib.request.Request(base + path, method=method, data=None if body is None else json.dumps(body).encode())
        if body is not None:
            req.add_header("Content-Type", "application/json")
        if token:
            req.add_header("Authorization", "Bearer " + token)
        if origin:
            req.add_header("Origin", origin)
        for k, v in (headers or {}).items():
            req.add_header(k, v)
        try:
            with urllib.request.urlopen(req) as r:
                return r.status, r.read().decode(), r.headers
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode(), e.headers

    def check(name, ok, detail=""):
        print(("ok   " if ok else "FAIL ") + name + ("" if ok else "  " + str(detail)))
        if not ok:
            fails.append(name)

    site = "https://spacecorps.github.io"
    # CORS: the download site and the page's own origin are allowed, a foreign page is not
    for origin, allowed in ((site, True), (page, True), ("https://evil.example", False), ("http://spacecorps.github.io", False)):
        s, _, h = call("OPTIONS", "/api/payment/create-checkout-session", origin=origin,
                       headers={"Access-Control-Request-Method": "POST", "Access-Control-Request-Headers": "authorization,content-type"})
        got = h.get("Access-Control-Allow-Origin")
        check(f"preflight from {origin}: {'allowed' if allowed else 'not allowed'}", s == 200 and (got == origin) == allowed and (allowed or got is None), (s, got))
    s, _, h = call("OPTIONS", "/api/auth/login", origin=site, headers={"Access-Control-Request-Method": "POST", "Access-Control-Request-Headers": "authorization,content-type"})
    check("preflight allows authorization and content-type", "authorization" in h.get("Access-Control-Allow-Headers", "") and "content-type" in h.get("Access-Control-Allow-Headers", ""))

    # sign-in
    check("unknown user is 400", call("POST", "/api/auth/login", {"username": "nobody", "password": "x"})[:2] == (400, "User not found."))
    check("wrong password is 400", call("POST", "/api/auth/login", {"username": "newbie", "password": "x"})[:2] == (400, "Wrong password."))
    check("banned is 403", call("POST", "/api/auth/login", {"username": "banned", "password": PASSWORD})[0] == 403)
    s, token, h = call("POST", "/api/auth/login", {"username": "newbie", "password": PASSWORD}, origin=site)
    check("login answers the token as text, with the origin", s == 200 and token == "mock-newbie" and h.get("Access-Control-Allow-Origin") == site, (s, token))
    check("no token is 401", call("GET", "/api/payment/status")[0] == 401)

    # status
    s, body, _ = call("GET", "/api/payment/status", token=token)
    check("newbie status", s == 200 and json.loads(body) == {"username": "newbie", "isPremium": False, "premiumUntil": None, "paymentsOpen": True, "subscription": False}, body)
    st = json.loads(call("GET", "/api/payment/status", token="mock-supporter")[1])
    check("supporter status", st["isPremium"] and st["subscription"] is True and st["premiumUntil"], st)
    check("nopay status closes payments", json.loads(call("GET", "/api/payment/status", token="mock-nopay")[1])["paymentsOpen"] is False)
    check("flaky status has an unknown subscription", json.loads(call("GET", "/api/payment/status", token="mock-flaky")[1])["subscription"] is None)

    # checkout refusals
    check("unknown product is refused", call("POST", "/api/payment/create-checkout-session", {"product": "thulium"}, token=token)[:2] == (400, NOT_FOR_SALE))
    check("no product is refused", call("POST", "/api/payment/create-checkout-session", {}, token=token)[:2] == (400, "Choose a product."))
    check("a second subscription is refused", call("POST", "/api/payment/create-checkout-session", {"product": "subscription"}, token="mock-supporter")[:2] == (400, ALREADY_SUBSCRIBED))
    check("closed payments are 503", call("POST", "/api/payment/create-checkout-session", {"product": "premium"}, token="mock-nopay")[:2] == (503, "Payments are not available on this server."))
    check("portal without a subscription is 404", call("POST", "/api/payment/portal", {}, token=token)[:2] == (404, "No subscription found."))

    # the whole purchase: checkout -> pay at the pretend Stripe -> sync -> Premium
    s, body, _ = call("POST", "/api/payment/create-checkout-session", {"product": "premium"}, token=token)
    url = json.loads(body)["url"]
    sid = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)["s"][0]
    check("checkout answers a url", s == 200 and url.startswith(f"{base}/stripe/checkout"), body)
    check("sync before paying is refused", call("POST", "/api/payment/sync-session", {"session_id": sid}, token=token)[:2] == (400, "Payment not paid yet."))
    check("somebody else's session is refused", call("POST", "/api/payment/sync-session", {"session_id": sid}, token="mock-oneoff")[:2] == (400, "This payment does not belong to your user."))

    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k):
            return None
    try:
        urllib.request.build_opener(NoRedirect).open(f"{base}/stripe/pay?s={sid}")
    except urllib.error.HTTPError as e:
        check("paying goes back to the page with success=true", e.code == 302 and e.headers["Location"] == f"{page}/premium/?success=true&session_id={sid}", e.headers["Location"])
    check("sync after paying works", call("POST", "/api/payment/sync-session", {"session_id": sid}, token=token)[:2] == (200, '{"status": "synced"}'))
    st = json.loads(call("GET", "/api/payment/status", token=token)[1])
    check("Premium now runs for about 30 days", st["isPremium"] and 29 <= (datetime.fromisoformat(st["premiumUntil"]) - now()).days <= 30, st)
    call("POST", "/api/payment/sync-session", {"session_id": sid}, token=token)
    st2 = json.loads(call("GET", "/api/payment/status", token=token)[1])
    check("a repeated sync adds nothing", st2["premiumUntil"] == st["premiumUntil"])

    server.shutdown()
    print("\nFAILED: " + ", ".join(fails) if fails else "\nall checks passed")
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8787)
    ap.add_argument("--page", default="http://127.0.0.1:8081", help="the origin the page is served from (allowed by CORS)")
    ap.add_argument("--allow-origin", action="append", default=[], help="another allowed origin (like Cors__ExtraOrigins)")
    ap.add_argument("--return-url", default=None, help="where the pretend Stripe sends the browser back (default: PAGE/premium/)")
    ap.add_argument("--selftest", action="store_true", help="start on a free port, check the routes and the CORS headers, and exit")
    args = ap.parse_args()
    if args.selftest:
        sys.exit(selftest())
    server, world = serve(args.port, args.page, args.allow_origin, args.return_url)
    print(f"mock premium API on http://127.0.0.1:{args.port}  (page origin {args.page}, return url {world.return_url})", flush=True)
    print("pilots (password 'pilotpass'): " + ", ".join(world.pilots), flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
