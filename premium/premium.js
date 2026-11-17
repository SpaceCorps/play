/* The Premium page: signs in with the game account, shows the pilot's Premium, and sends the pilot to Stripe to pay.
   No framework, no external script, no cookie, no analytics. The token lives in sessionStorage (this tab only), never in a URL.
   Everything the server says is written with textContent, never as HTML. */
(function () {
  'use strict';

  // The game server (Home). The ONE place the address is written.
  const API = 'https://spacecorps-game.sliplane.app';

  // For trying the page against a local mock API (scripts/mock-premium-api.py): only a page that is itself served from this machine may
  // name another API, with ?api=http://127.0.0.1:8787. On the real site the constant above is all there is.
  const LOCAL_PAGE = ['localhost', '127.0.0.1', '[::1]'].indexOf(location.hostname) !== -1;
  function apiBase() {
    const asked = LOCAL_PAGE ? new URLSearchParams(location.search).get('api') : null;
    return asked && /^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/.test(asked) ? asked : API;
  }
  const BASE = apiBase();

  const TOKEN_KEY = 'spacecorps.premium.token';
  const $ = function (id) { return document.getElementById(id); };

  // ---- the session (this tab only) --------------------------------------------------------------------------------------------------------------

  let token = '';
  try { token = sessionStorage.getItem(TOKEN_KEY) || ''; } catch (e) { token = ''; }

  function setToken(value) {
    token = value || '';
    try {
      if (token) sessionStorage.setItem(TOKEN_KEY, token); else sessionStorage.removeItem(TOKEN_KEY);
    } catch (e) { /* the page still works until it is reloaded */ }
  }

  // ---- the state of the page --------------------------------------------------------------------------------------------------------------------

  const state = {
    signedIn: false,
    paymentsOpen: true,   // false: the server has no payments (yet)
    subscription: false,  // true: Stripe has a subscription of the pilot; null: could not be asked
    busy: false,          // a call is under way
  };

  // ---- the server -------------------------------------------------------------------------------------------------------------------------------

  function ApiError(status, text) {
    this.status = status;   // 0: no answer at all
    this.text = text || '';
  }

  function api(method, path, body) {
    const headers = {};
    if (token) headers['Authorization'] = 'Bearer ' + token;
    if (body !== undefined) headers['Content-Type'] = 'application/json';
    return fetch(BASE + path, {
      method: method,
      headers: headers,
      body: body === undefined ? undefined : JSON.stringify(body),
      cache: 'no-store',
      credentials: 'omit',
      referrerPolicy: 'no-referrer',
    }).then(function (res) {
      // the server renews a token that is an hour old and says so in this header
      const renewed = res.headers.get('x-refreshed-token');
      if (renewed && token) setToken(renewed);
      return res.text().then(function (text) {
        if (!res.ok) throw new ApiError(res.status, text);
        return text;
      });
    }, function () {
      throw new ApiError(0, '');
    });
  }

  function json(text) {
    try { return JSON.parse(text); } catch (e) { return {}; }
  }

  // The sentence of an error body: plain text as it is, or the "message" of a JSON body ({"code": ..., "message": ...}, which some refusals of the server are).
  // Raw JSON is never shown to the pilot.
  function sentence(text) {
    const t = (text || '').trim();
    if (t.charAt(0) !== '{') return t;
    const body = json(t);
    return typeof body.message === 'string' ? body.message.trim() : '';
  }

  // What a failed call says to the pilot, in plain words.
  function explain(err) {
    if (!(err instanceof ApiError)) return 'Something went wrong. Try again in a minute.';
    const said = sentence(err.text);
    switch (true) {
      case err.status === 0:
        return 'The game server cannot be reached. Check your connection and try again in a minute.';
      case err.status === 401:
        return 'Your session ended. Please sign in again.';
      case err.status === 429:
        return 'Too many tries. Wait a few minutes and try again.';
      case err.status === 409 && /FLYING_ELSEWHERE/.test(err.text || ''):
        return 'Your ship is still flying on another server. Bring it home in the game (Bring my ship home) and try again.';
      case err.status === 503 && /payments are not available/i.test(said):
        return 'Payments are not available yet.';
      case err.status === 503:
        return 'The game server is busy right now, for example while a season changes. Try again in a few minutes.';
      case err.status >= 500:
        return 'Something went wrong on the game server. Try again in a minute.';
      case err.status === 404:
        return said && said.length < 160 ? said : 'Not found.';
      default:
        // 400 and the like: the server's own short sentence ("You already have a subscription: ...")
        return said && said.length < 300 ? said : 'That did not work. Try again in a minute.';
    }
  }

  // ---- messages ---------------------------------------------------------------------------------------------------------------------------------

  function show(el, text, kind) {
    el.textContent = text;
    el.className = 'msg' + (kind ? ' msg-' + kind : '');
    el.hidden = !text;
  }
  // The banner is at the top; a pilot who just pressed a button further down must see what it says.
  const banner = function (text, kind) {
    const el = $('banner');
    show(el, text, kind);
    if (text && el.scrollIntoView) {
      try { el.scrollIntoView({ block: 'nearest', behavior: 'smooth' }); } catch (e) { /* not important */ }
    }
  };
  const signinMsg = function (text) { show($('signin-msg'), text, 'error'); };

  // "14 December 2026, 18:04 CET"
  function when(iso) {
    const d = new Date(iso);
    if (isNaN(d.getTime())) return '';
    return new Intl.DateTimeFormat('en-GB', {
      day: 'numeric', month: 'long', year: 'numeric', hour: '2-digit', minute: '2-digit', timeZoneName: 'short',
    }).format(d);
  }

  // ---- drawing ----------------------------------------------------------------------------------------------------------------------------------

  function render() {
    $('signed-out').hidden = state.signedIn;
    $('signed-in').hidden = !state.signedIn;

    const canBuy = state.signedIn && state.paymentsOpen && !state.busy;
    const premiumReady = canBuy && $('agree-premium').checked;
    const subReady = canBuy && $('agree-sub').checked && state.subscription !== true;
    $('buy-premium').disabled = !premiumReady;
    $('buy-sub').disabled = !subReady;
    $('agree-premium').disabled = !state.signedIn || !state.paymentsOpen;
    $('agree-sub').disabled = !state.signedIn || !state.paymentsOpen || state.subscription === true;

    // what stands under each button
    const hintPremium = $('hint-premium');
    const hintSub = $('hint-sub');
    hintPremium.hidden = hintSub.hidden = false;
    if (!state.signedIn) {
      hintPremium.textContent = 'Sign in above to buy.';
      hintSub.textContent = 'Sign in above to subscribe.';
    } else if (!state.paymentsOpen) {
      hintPremium.textContent = hintSub.textContent = 'Payments are not available yet.';
    } else {
      hintPremium.hidden = $('agree-premium').checked;
      hintPremium.textContent = 'Tick the box to buy.';
      if (state.subscription === true) {
        hintSub.textContent = 'You already have a subscription. Manage it below.';
      } else {
        hintSub.hidden = $('agree-sub').checked;
        hintSub.textContent = 'Tick the box to subscribe.';
      }
    }

    // Manage subscription: for a pilot who has one (and when Stripe could not be asked, in case he has)
    $('manage').hidden = !(state.signedIn && state.paymentsOpen && state.subscription !== false);
    $('manage-btn').disabled = state.busy;
    $('signout').disabled = false;

    const subState = $('sub-state');
    if (!state.signedIn) subState.textContent = '';
    else if (!state.paymentsOpen) subState.textContent = 'not available yet';
    else if (state.subscription === true) subState.textContent = 'you have one';
    else if (state.subscription === null) subState.textContent = 'could not be checked right now';
    else subState.textContent = 'none';
  }

  function drawStatus(s) {
    $('who-name').textContent = s.username || '';
    const on = s.isPremium === true;
    const badge = $('premium-badge');
    badge.textContent = on ? 'running' : 'not running';
    badge.className = 'badge ' + (on ? 'badge-on' : 'badge-off');
    $('premium-until').textContent = on && s.premiumUntil ? 'until ' + when(s.premiumUntil) : '';
    state.paymentsOpen = s.paymentsOpen !== false;
    state.subscription = s.subscription === null ? null : s.subscription === true;
  }

  // ---- sign in, sign out ------------------------------------------------------------------------------------------------------------------------

  function signOut(message, kind) {
    setToken('');
    state.signedIn = false;
    state.subscription = false;
    state.paymentsOpen = true;
    $('pass').value = '';
    $('agree-premium').checked = false;
    $('agree-sub').checked = false;
    signinMsg('');
    banner(message || '', kind);
    render();
  }

  // Asks the server who this is and what he has. false: the token is no good (the page has gone back to the sign-in).
  function refresh() {
    return api('GET', '/api/payment/status').then(function (text) {
      drawStatus(json(text));
      state.signedIn = true;
      render();
      return true;
    }, function (err) {
      if (err instanceof ApiError && err.status === 401) {
        signOut('Your session ended. Please sign in again.', 'info');
        return false;
      }
      if (state.signedIn) {
        banner(explain(err), 'error');
      } else {
        // a token from this tab that could not be checked (the server is down): sign-in stays, with the reason
        setToken('');
        signinMsg(explain(err));
        render();
      }
      return false;
    });
  }

  function signIn(ev) {
    ev.preventDefault();
    const username = $('user').value.trim();
    const password = $('pass').value;
    if (!username || !password) {
      signinMsg('Enter your user name and your password.');
      return;
    }
    signinMsg('');
    banner('');
    state.busy = true;
    $('signin-btn').disabled = true;
    $('signin-btn').textContent = 'Signing in…';
    api('POST', '/api/auth/login', { username: username, password: password }).then(function (text) {
      // the answer is the token as plain text (some servers may wrap it in a JSON string)
      const value = text.trim().replace(/^"|"$/g, '');
      if (!value) throw new ApiError(500, '');
      setToken(value);
      $('pass').value = '';
      return refresh().then(function (ok) { if (ok) return afterSignIn(); });
    }).catch(function (err) {
      if (err instanceof ApiError && err.status === 400) signinMsg('Wrong user name or password.');
      else if (err instanceof ApiError && err.status === 403) signinMsg(err.text || 'This account cannot sign in.');
      else signinMsg(explain(err));
    }).then(function () {
      state.busy = false;
      $('signin-btn').disabled = false;
      $('signin-btn').textContent = 'Sign in';
      render();
    });
  }

  // ---- coming back from Stripe ------------------------------------------------------------------------------------------------------------------

  let pendingSession = '';   // a paid session to confirm once the pilot is signed in

  function readReturn() {
    const q = new URLSearchParams(location.search);
    if (q.get('canceled') === 'true') {
      banner('Nothing was charged. You can pick a way to pay again whenever you like.', 'info');
      cleanUrl();
    } else if (q.get('success') === 'true') {
      const id = q.get('session_id') || '';
      if (/^cs_[A-Za-z0-9_]{6,200}$/.test(id)) pendingSession = id;
      else banner('We could not read the payment from this address. If you paid, Premium is added as soon as Stripe confirms it. Sign in to see your Premium.', 'info');
    }
  }

  // The query goes (a reload must not confirm or cancel again), but the ?api= of a test stays.
  function cleanUrl() {
    const q = new URLSearchParams(location.search);
    const keep = q.get('api');
    const next = location.pathname + (keep && LOCAL_PAGE ? '?api=' + encodeURIComponent(keep) : '');
    try { history.replaceState(null, '', next); } catch (e) { /* not important */ }
  }

  function afterSignIn() {
    if (!pendingSession) return Promise.resolve();
    return confirmPayment(pendingSession, 0);
  }

  function confirmPayment(id, attempt) {
    banner('Confirming your payment…', 'info');
    return api('POST', '/api/payment/sync-session', { session_id: id }).then(function () {
      pendingSession = '';
      cleanUrl();
      return refresh().then(function () {
        const until = $('premium-until').textContent;
        banner('Thank you for supporting SpaceCorps! Premium is running' + (until ? ' ' + until : '') + '.', 'ok');
      });
    }, function (err) {
      if (err instanceof ApiError && err.status === 401) { signOut('Your session ended. Please sign in again.', 'info'); return; }
      // A payment that is not this pilot's is not asked about again
      if (err instanceof ApiError && err.status === 400 && /does not belong/i.test(err.text)) {
        pendingSession = '';
        cleanUrl();
        banner(explain(err), 'error');
        return;
      }
      // Stripe may take a moment to say "paid": ask again a few times
      if (attempt < 4) {
        return new Promise(function (resolve) { setTimeout(resolve, 3000); }).then(function () { return confirmPayment(id, attempt + 1); });
      }
      pendingSession = '';
      cleanUrl();
      // (nothing is known about the payment here: it may be forged, refused or just slow; some payment methods take a while to settle)
      banner('Stripe has not confirmed this payment yet. If you paid, Premium is added to your account by itself as soon as Stripe confirms it; some payment methods take a while. Reload this page later to check.', 'info');
    });
  }

  // ---- paying -----------------------------------------------------------------------------------------------------------------------------------

  // Only a Stripe address is followed (a page served from this machine, for a test, may follow its mock).
  function stripeUrl(value) {
    let u;
    try { u = new URL(value); } catch (e) { return ''; }
    const host = u.hostname;
    if (u.protocol === 'https:' && (host === 'stripe.com' || /\.stripe\.com$/.test(host))) return u.href;
    if (LOCAL_PAGE && (u.protocol === 'https:' || u.protocol === 'http:') && ['localhost', '127.0.0.1'].indexOf(host) !== -1) return u.href;
    return '';
  }

  function go(path, body, button, busyText) {
    if (state.busy) return;
    state.busy = true;
    banner('');
    const label = button.textContent;
    button.textContent = busyText;
    render();
    api('POST', path, body).then(function (text) {
      const url = stripeUrl(json(text).url || '');
      if (!url) throw new ApiError(502, '');
      // the browser goes to Stripe; the busy state stays until it has left
      location.assign(url);
    }).catch(function (err) {
      state.busy = false;
      button.textContent = label;
      if (err instanceof ApiError && err.status === 401) {
        signOut('Your session ended. Please sign in again.', 'info');
        return;
      }
      banner(err instanceof ApiError && err.status === 502 ? 'Stripe did not answer as expected. Nothing was charged. Try again in a minute.' : explain(err), 'error');
      // a refusal can mean the state changed (a subscription that exists now): look again
      if (err instanceof ApiError && err.status === 400) refresh();
      render();
    });
  }

  function buyPremium() {
    go('/api/payment/create-checkout-session', { product: 'premium' }, $('buy-premium'), 'Opening Stripe…');
  }
  function buySubscription() {
    go('/api/payment/create-checkout-session', { product: 'subscription' }, $('buy-sub'), 'Opening Stripe…');
  }
  function manage() {
    go('/api/payment/portal', {}, $('manage-btn'), 'Opening Stripe…');
  }

  // The browser's Back button from Stripe can bring this page back as it was left, with a button still saying "Opening Stripe…".
  function restoreLabels() {
    state.busy = false;
    $('buy-premium').textContent = 'Buy 30 days for $14.99';
    $('buy-sub').textContent = 'Subscribe for $9.99 per month';
    $('manage-btn').textContent = 'Manage subscription';
    render();
  }

  // ---- start ------------------------------------------------------------------------------------------------------------------------------------

  $('signin-form').addEventListener('submit', signIn);
  $('signout').addEventListener('click', function () { signOut('You are signed out.', 'info'); });
  $('agree-premium').addEventListener('change', render);
  $('agree-sub').addEventListener('change', render);
  $('buy-premium').addEventListener('click', buyPremium);
  $('buy-sub').addEventListener('click', buySubscription);
  $('manage-btn').addEventListener('click', manage);
  window.addEventListener('pageshow', function (ev) { if (ev.persisted) restoreLabels(); });

  // a tick left from before the page was reloaded or came back from Stripe is not consent to this payment
  $('agree-premium').checked = false;
  $('agree-sub').checked = false;

  readReturn();
  render();
  if (token) {
    refresh().then(function (ok) { if (ok) return afterSignIn(); });
  } else if (pendingSession) {
    banner('Your payment went through. Sign in to see your Premium; it is added to your account automatically.', 'ok');
  }
})();
