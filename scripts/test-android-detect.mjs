// Android UA emulation (CDP userAgentMetadata + a phone viewport) vs iPhone vs desktop: the APK card, the big button and the notes. Serve the repository (python -m http.server 8769), then: node scripts/test-android-detect.mjs http://127.0.0.1:8769 /tmp/android-shots
import { spawn } from 'node:child_process';
import { mkdtempSync, mkdirSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
const [BASE, OUT] = [process.argv[2], process.argv[3]];
mkdirSync(OUT, { recursive: true });
const PORT = 9335;
const chrome = spawn(process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe', ['--headless=new', `--remote-debugging-port=${PORT}`, `--user-data-dir=${mkdtempSync(join(tmpdir(), 'and-'))}`, '--no-first-run', '--hide-scrollbars', 'about:blank'], { stdio: 'ignore' });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let url; for (let i = 0; i < 60 && !url; i++) { try { url = (await (await fetch(`http://127.0.0.1:${PORT}/json/version`)).json()).webSocketDebuggerUrl; } catch { await sleep(250); } }
const ws = new WebSocket(url); await new Promise((r) => ws.addEventListener('open', r));
let id = 0; const cbs = new Map();
ws.addEventListener('message', (e) => { const m = JSON.parse(e.data); if (m.id && cbs.has(m.id)) { cbs.get(m.id)(m); cbs.delete(m.id); } });
const send = (method, params = {}, sessionId) => new Promise((res) => { const i = ++id; cbs.set(i, res); ws.send(JSON.stringify({ id: i, method, params, sessionId })); });

const ANDROID_UA = 'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36';
const IPHONE_UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1';
const DESK_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const md = (platform, arch, mobile) => ({ brands: [{ brand: 'Chromium', version: '131' }], fullVersion: '131.0.0.0', platform, platformVersion: '14.0.0', architecture: arch, model: platform === 'Android' ? 'Pixel 8' : '', mobile, bitness: '64', wow64: false });
const SC = [
  { name: 'android-chrome', ua: ANDROID_UA, meta: md('Android', '', true), w: 412, h: 915, mobile: true, expect: 'android-aarch64.apk' },
  { name: 'iphone-safari', ua: IPHONE_UA, w: 390, h: 844, mobile: true, expect: null },
  { name: 'win-desktop', ua: DESK_UA, meta: md('Windows', 'x86', false), w: 1280, h: 900, mobile: false, expect: 'windows-x86_64.zip' },
];
const READ = `(() => { const q = (s) => document.querySelector(s); const cards = [...document.querySelectorAll('.platform')].map((c) => [c.dataset.asset, c.querySelector('.size').textContent, c.querySelector('.sha code').textContent.slice(0, 10), c.classList.contains('is-missing')]);
  return JSON.stringify({ main: q('#dl-main').href.split('/').pop(), label: q('#dl-main-label').textContent, sub: q('#dl-main-sub').textContent.trim(), note: q('#dl-note').textContent.trim(), webSub: q('#play-web .btn-sub').textContent.trim(),
  you: [...document.querySelectorAll('.platform.is-you')].map((c) => c.dataset.asset), cards, phones: q('[data-i18n="download.phones"]').textContent, hscroll: document.documentElement.scrollWidth > innerWidth }); })()`;
const results = [];
for (const sc of SC) {
  const { result: { targetId } } = await send('Target.createTarget', { url: 'about:blank' });
  const { result: { sessionId } } = await send('Target.attachToTarget', { targetId, flatten: true });
  const S = (m, p) => send(m, p, sessionId);
  await S('Page.enable');
  await S('Emulation.setDeviceMetricsOverride', { width: sc.w, height: sc.h, deviceScaleFactor: 1, mobile: sc.mobile });
  if (!sc.mobile) await S('Page.addScriptToEvaluateOnNewDocument', { source: "Object.defineProperty(navigator,'maxTouchPoints',{get:()=>0})" });
  await S('Emulation.setUserAgentOverride', { userAgent: sc.ua, acceptLanguage: 'en-US', ...(sc.meta ? { userAgentMetadata: sc.meta } : {}) });
  await S('Page.navigate', { url: BASE + '/' }); await sleep(2500);
  const r = JSON.parse((await S('Runtime.evaluate', { expression: READ, returnByValue: true })).result.result.value);
  const shot = async (suffix) => { const img = await S('Page.captureScreenshot', { format: 'png' }); writeFileSync(join(OUT, `${sc.name}-${suffix}.png`), Buffer.from(img.result.data, 'base64')); };
  await shot('hero');
  await S('Runtime.evaluate', { expression: `window.scrollTo({top: document.querySelector('#download-title').getBoundingClientRect().top + scrollY - 70, behavior: 'instant'})` }); await sleep(400);
  await shot('list');
  await S('Runtime.evaluate', { expression: `(()=>{const d=document.querySelector('#help-android'); d.open=true; d.scrollIntoView({block:'center', behavior:'instant'})})()` }); await sleep(400);
  await shot('help');
  const pass = sc.expect ? r.main.endsWith(sc.expect) && r.you.length === 1 && r.you[0].endsWith(sc.expect) : !r.main.endsWith('.apk') && r.you.length === 0;
  const android = r.cards.find((c) => c[0].endsWith('.apk'));
  results.push({ ...sc, ...r, pass: pass && !r.hscroll && android && !android[3] });
  console.log(pass && !r.hscroll ? 'PASS' : 'FAIL', sc.name.padEnd(15), '| main:', r.main, '| label:', r.label, '| sub:', r.sub, '| is-you:', r.you.join(',') || '-', '| web sub:', r.webSub, '| hscroll:', r.hscroll);
  console.log('     note:', r.note); console.log('     apk card:', JSON.stringify(android));
  await send('Target.closeTarget', { targetId });
}
chrome.kill();
process.exit(results.every((r) => r.pass) ? 0 : 1);
