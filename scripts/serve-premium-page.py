#!/usr/bin/env python3
"""Serves this repository's files on 127.0.0.1 to try the Premium page against scripts/mock-premium-api.py.

The shipped page's Content-Security-Policy lets it talk to the real game server only (`connect-src https://spacecorps-game.sliplane.app`). To try it against a mock on this machine
this server serves premium/index.html with that one directive widened to http://localhost:* and http://127.0.0.1:*. Nothing is written to the repository: the file on disk stays strict,
and the real site is served by GitHub Pages, not by this script.

    python scripts/serve-premium-page.py --port 8081            (in the repository root)
"""
import argparse
import http.server
import os
import sys

STRICT = "connect-src https://spacecorps-game.sliplane.app;"
LOCAL = "connect-src https://spacecorps-game.sliplane.app http://localhost:* http://127.0.0.1:*;"


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path in ("/premium/", "/premium/index.html"):
            with open(os.path.join(self.directory, "premium", "index.html"), encoding="utf-8") as f:
                html = f.read()
            if STRICT not in html:
                # the page's policy changed: do not serve a page whose policy this script has not seen
                self.send_error(500, "premium/index.html: the connect-src directive is not the one this script widens")
                return
            body = html.replace(STRICT, LOCAL).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def log_message(self, *args):
        pass


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8081)
    ap.add_argument("--bind", default="127.0.0.1")
    args = ap.parse_args()
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    handler = lambda *a, **k: Handler(*a, directory=root, **k)  # noqa: E731
    server = http.server.ThreadingHTTPServer((args.bind, args.port), handler)
    print(f"serving {root} on http://{args.bind}:{args.port}/premium/", file=sys.stderr)
    server.serve_forever()


if __name__ == "__main__":
    main()
