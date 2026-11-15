#!/usr/bin/env node
// Looks at the Premium page in a real headless browser (Edge or Chrome) against the local mock API: nothing here calls the real game server or Stripe.
//
//   node scripts/premium-shots.mjs OUTDIR            (needs Node 22+, Python 3, Edge or Chrome; run it in the repository root)
//
// It starts `python -m http.server` for the page (port 8081) and scripts/mock-premium-api.py (port 8787), drives the browser over the DevTools protocol
// (sign in, tick, click, buy, pay at the pretend Stripe, come back) and writes one PNG per state and viewport (390x844 and 1280x800) into OUTDIR,
// plus checks.txt: what the script asserted about the page on the way (it exits 1 when one fails).
import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const out = process.argv[2];
if (!out) { console.error('usage: node scripts/premium-shots.mjs OUTDIR'); process.exit(2); }
mkdirSync(out, { recursive: true });

const PAGE_PORT = 8081, API_PORT = 8787, DEBUG_PORT = 9333;
const PAGE = `http://127.0.0.1:${PAGE_PORT}`, API = `http://127.0.0.1:${API_PORT}`;
const START = `${PAGE}/premium/?api=${API}`;
const browsers = [
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  '/usr/bin/google-chrome', '/usr/bin/chromium', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
];
const browser = browsers.find(existsSync);
if (!browser) { console.error('no Edge or Chrome found'); process.exit(2); }

// A server left over from an earlier run on one of these ports would answer instead of ours, with a state of its own: refuse to start then.
import { createServer } from 'node:net';
for (const port of [PAGE_PORT, API_PORT, DEBUG_PORT]) {
  const free = await new Promise((resolve) => {
    const s = createServer().once('error', () => resolve(false)).once('listening', () => s.close(() => resolve(true)));
    s.listen(port, '127.0.0.1');
  });
  if (!free) { console.error(`port ${port} is in use: stop what holds it (a server of an earlier run?) and run again`); process.exit(2); }
}

const children = [];
// (on Windows `python` may be a launcher that starts the real interpreter: the whole tree has to go)
const stop = (c) => { try { if (process.platform === 'win32') spawn('taskkill', ['/T', '/F', '/PID', String(c.pid)], { stdio: 'ignore' }); else c.kill(); } catch { /* gone */ } };
const run = (cmd, args, opts = {}) => { const c = spawn(cmd, args, { stdio: 'ignore', ...opts }); children.push(c); return c; };
const python = process.platform === 'win32' ? 'python' : 'python3';
run(python, ['-m', 'http.server', String(PAGE_PORT), '--bind', '127.0.0.1']);
// the pretend Stripe sends the browser back to the page WITH ?api=, so the page keeps talking to the mock after a payment
let mock;
async function startMock() {
  if (mock) stop(mock);
  await new Promise((r) => setTimeout(r, 1200));
  mock = run(python, ['scripts/mock-premium-api.py', '--port', String(API_PORT), '--page', PAGE, '--return-url', START]);
}
const profile = mkdtempSync(join(tmpdir(), 'premium-shots-'));
run(browser, [`--remote-debugging-port=${DEBUG_PORT}`, `--user-data-dir=${profile}`, '--headless=new', '--no-first-run', '--no-default-browser-check', '--disable-gpu', 'about:blank']);

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
async function until(fn, what, ms = 10000) {
  const end = Date.now() + ms;
  for (;;) {
    try { const v = await fn(); if (v) return v; } catch { /* not yet */ }
    if (Date.now() > end) throw new Error('timed out: ' + what);
    await sleep(100);
  }
}
const getJson = async (url) => (await fetch(url)).json();

let ws, nextId = 0;
const pending = new Map();
const failures = [];
const log = [];
function note(ok, what) { log.push((ok ? 'ok   ' : 'FAIL ') + what); if (!ok) failures.push(what); }

function send(method, params = {}) {
  return new Promise((resolve, reject) => {
    const id = ++nextId;
    pending.set(id, { resolve, reject });
    ws.send(JSON.stringify({ id, method, params }));
  });
}
async function ev(expression) {
  const r = await send('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
  if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description || 'evaluate failed');
  return r.result.value;
}

async function connect() {
  const target = await until(async () => (await getJson(`http://127.0.0.1:${DEBUG_PORT}/json/list`)).find((t) => t.type === 'page'), 'the browser', 20000);
  ws = new WebSocket(target.webSocketDebuggerUrl);
  ws.onmessage = (e) => {
    const m = JSON.parse(e.data);
    const p = m.id && pending.get(m.id);
    if (p) { pending.delete(m.id); m.error ? p.reject(new Error(m.error.message)) : p.resolve(m.result); }
  };
  await new Promise((r) => { ws.onopen = r; });
  await send('Page.enable');
}

let viewport = { w: 1280, h: 800 };
async function setViewport(w, h) {
  viewport = { w, h };
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile: w < 500 });
}
async function open(url) {
  await ev('try { sessionStorage.clear() } catch (e) {}').catch(() => {});
  await send('Page.navigate', { url });
  await until(() => ev("document.readyState === 'complete'"), 'load ' + url);
  await sleep(150);
}
const visible = (id) => ev(`(() => { const e = document.getElementById(${JSON.stringify(id)}); return !!e && !e.hidden && e.getClientRects().length > 0; })()`);
const text = (id) => ev(`document.getElementById(${JSON.stringify(id)}).textContent`);
async function signIn(user, pass = 'pilotpass') {
  await ev(`document.getElementById('user').value = ${JSON.stringify(user)}; document.getElementById('pass').value = ${JSON.stringify(pass)}; document.getElementById('signin-form').requestSubmit();`);
}
const signedIn = () => until(() => visible('signed-in'), 'the signed-in block');
const tick = (id) => ev(`(() => { const c = document.getElementById(${JSON.stringify(id)}); if (!c.checked) c.click(); })()`);
const disabled = (id) => ev(`document.getElementById(${JSON.stringify(id)}).disabled`);

async function shot(name) {
  // full page: the viewport is as high as the content
  const h = await ev('Math.max(document.documentElement.scrollHeight, document.body.scrollHeight)');
  await send('Emulation.setDeviceMetricsOverride', { width: viewport.w, height: Math.max(viewport.h, h), deviceScaleFactor: 1, mobile: viewport.w < 500 });
  await sleep(150);
  const r = await send('Page.captureScreenshot', { format: 'png', fromSurface: true });
  const file = join(out, `${name}-${viewport.w}x${viewport.h}.png`);
  writeFileSync(file, Buffer.from(r.data, 'base64'));
  await setViewport(viewport.w, viewport.h);
  console.log('wrote', file);
}

async function scenarios() {
  // 1. signed out
  await open(START);
  note(await visible('signed-out') && !(await visible('signed-in')), 'signed out: the sign-in form shows, the account block does not');
  note(await disabled('buy-premium') && await disabled('buy-sub'), 'signed out: both buy buttons are disabled');
  note((await text('hint-premium')).includes('Sign in'), 'signed out: the hint says to sign in');
  await shot('01-signed-out');

  // 2. wrong password, then an unknown user
  await signIn('newbie', 'wrong');
  await until(() => visible('signin-msg'), 'the sign-in error');
  note((await text('signin-msg')) === 'Wrong user name or password.', 'wrong password: "Wrong user name or password."');
  await shot('02-wrong-password');

  // 3. signed in, no Premium
  await signIn('newbie');
  await signedIn();
  note((await text('who-name')) === 'newbie', 'signed in: the pilot\'s name is shown');
  note((await text('premium-badge')) === 'not running', 'no Premium: "not running"');
  note(await disabled('buy-premium') && await disabled('buy-sub'), 'signed in, box not ticked: both buy buttons are disabled');
  note(!(await visible('manage')), 'no subscription: no Manage subscription button');
  const token = await ev("sessionStorage.getItem('spacecorps.premium.token')");
  note(token === 'mock-newbie' && !(await ev('location.href')).includes('mock-newbie'), 'the token is in sessionStorage and not in the address');
  await shot('03-signed-in-no-premium');

  // 4. the boxes ticked: the buttons come on
  await tick('agree-premium'); await tick('agree-sub');
  note(!(await disabled('buy-premium')) && !(await disabled('buy-sub')), 'both boxes ticked: both buy buttons are enabled');
  await shot('04-boxes-ticked');

  // 5. sign out clears the token
  await ev("document.getElementById('signout').click()");
  await until(() => visible('signed-out'), 'sign out');
  note((await ev("sessionStorage.getItem('spacecorps.premium.token')")) === null, 'sign out: the token is gone from sessionStorage');

  // 6. Premium running and a subscription
  await signIn('supporter');
  await signedIn();
  note((await text('premium-badge')) === 'running' && (await text('premium-until')).startsWith('until '), 'supporter: Premium "running" with its end date');
  note(await visible('manage'), 'supporter: Manage subscription shows');
  note(await disabled('buy-sub'), 'supporter: the subscription button stays disabled (a second one is not offered)');
  await shot('05-premium-and-subscribed');

  // 7. payments are not available (503)
  await open(START); await signIn('nopay'); await signedIn();
  note(await disabled('buy-premium') && (await text('hint-premium')).includes('not available'), 'nopay: buttons disabled, "not available yet"');
  await shot('06-payments-not-available');

  // 8. the server cannot be reached
  await open(`${PAGE}/premium/?api=http://127.0.0.1:1`); await signIn('newbie');
  await until(() => visible('signin-msg'), 'the unreachable error');
  note((await text('signin-msg')).includes('cannot be reached'), 'server down: "The game server cannot be reached..."');
  await shot('07-server-unavailable');

  // 9. a busy server (503 from a payment call, while a season changes)
  await open(START); await signIn('busy'); await signedIn(); await tick('agree-premium');
  await ev("document.getElementById('buy-premium').click()");
  await until(() => visible('banner'), 'the busy banner');
  note((await text('banner')).includes('busy'), 'busy: the 503 says the server is busy');
  await shot('08-server-busy');

  // 10. the pilot comes back from Stripe without paying
  await open(`${START}&canceled=true`);
  await until(() => visible('banner'), 'the cancel banner');
  note((await text('banner')).startsWith('Nothing was charged'), 'canceled=true: "Nothing was charged."');
  await shot('09-canceled');

  // 11. the whole purchase: sign in, tick, buy, pay at the pretend Stripe, come back, "Thank you"
  await open(START); await signIn('oneoff'); await signedIn();
  const before = await text('premium-until');
  await tick('agree-premium');
  await ev("document.getElementById('buy-premium').click()");
  await until(async () => (await ev('location.href')).includes('/stripe/checkout'), 'the pretend Stripe checkout');
  await until(() => ev("document.getElementById('pay') !== null"), 'its pay link');
  await ev("document.getElementById('pay').click()");
  await until(async () => (await ev('location.href')).includes('/premium/'), 'the way back');
  await until(async () => (await ev("document.getElementById('banner').textContent")).startsWith('Thank you for supporting'), 'the thank-you', 20000);
  const after = await text('premium-until');
  note(!(await ev('location.search')).includes('session_id'), 'back from Stripe: the session id is taken out of the address');
  note(before !== after && after.startsWith('until '), `a purchase adds 30 days (${before.trim()} -> ${after.trim()})`);
  await shot('10-thank-you');

  // 12. the subscription purchase, then Manage subscription goes to the pretend portal
  await open(START); await signIn('newbie'); await signedIn(); await tick('agree-sub');
  await ev("document.getElementById('buy-sub').click()");
  await until(async () => (await ev('location.href')).includes('/stripe/checkout'), 'the subscription checkout');
  await ev("document.getElementById('pay').click()");
  await until(async () => (await ev("document.getElementById('banner')?.textContent || ''")).startsWith('Thank you for supporting'), 'the thank-you', 20000);
  note(await visible('manage') && await disabled('buy-sub'), 'after subscribing: Manage subscription shows and a second subscription is not offered');
  await ev("document.getElementById('manage-btn').click()");
  await until(async () => (await ev('location.href')).includes('/stripe/portal'), 'the pretend billing portal');
  note(true, 'Manage subscription opens the (pretend) billing portal');

  // 13. the terms page
  await open(`${PAGE}/premium/terms/`);
  await shot('11-terms');
}

let code = 0;
try {
  await connect();
  for (const [w, h] of [[390, 844], [1280, 800]]) {
    await startMock();   // a fresh mock for each size: the purchases of the first run must not be in the second
    await until(async () => (await fetch(`${API}/stripe/portal`)).ok, 'the mock API', 15000);
    await setViewport(w, h);
    await scenarios();
  }
} catch (e) {
  console.error('FAILED:', e.message);
  log.push('FAIL ' + e.message);
  failures.push(e.message);
  code = 1;
} finally {
  writeFileSync(join(out, 'checks.txt'), log.join('\n') + '\n');
  console.log(log.join('\n'));
  try { ws?.close(); } catch { /* gone */ }
  for (const c of children) stop(c);
}
process.exit(code || (failures.length ? 1 : 0));
