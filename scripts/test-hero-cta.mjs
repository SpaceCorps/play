// Hero buttons line up (icon and label at the same x in Download, Play in browser, Support) at 375, 768, 1024 and 1400 px, in a real Chrome over CDP. Serve the repository (python -m http.server 8768), then: node scripts/test-hero-cta.mjs http://127.0.0.1:8768 /tmp/cta-shots
import { spawn } from 'node:child_process';
import { mkdtempSync, mkdirSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
const [BASE, OUT] = [process.argv[2], process.argv[3]];
mkdirSync(OUT, { recursive: true });
const PORT = 9334;
const chrome = spawn(process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe', ['--headless=new', `--remote-debugging-port=${PORT}`, `--user-data-dir=${mkdtempSync(join(tmpdir(), 'cta-'))}`, '--no-first-run', '--hide-scrollbars', 'about:blank'], { stdio: 'ignore' });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let url; for (let i = 0; i < 60 && !url; i++) { try { url = (await (await fetch(`http://127.0.0.1:${PORT}/json/version`)).json()).webSocketDebuggerUrl; } catch { await sleep(250); } }
const ws = new WebSocket(url); await new Promise((r) => ws.addEventListener('open', r));
let id = 0; const cbs = new Map();
ws.addEventListener('message', (e) => { const m = JSON.parse(e.data); if (m.id && cbs.has(m.id)) { cbs.get(m.id)(m); cbs.delete(m.id); } });
const send = (method, params = {}, sessionId) => new Promise((res) => { const i = ++id; cbs.set(i, res); ws.send(JSON.stringify({ id: i, method, params, sessionId })); });
const { result: { targetId } } = await send('Target.createTarget', { url: 'about:blank' });
const { result: { sessionId } } = await send('Target.attachToTarget', { targetId, flatten: true });
const S = (m, p) => send(m, p, sessionId);
await S('Page.enable');
const MEASURE = `(() => { const r = (el) => el.getBoundingClientRect(); const out = {};
  for (const [name, sel] of [['download', '#dl-main'], ['play', '#play-web'], ['support', '#support-main']]) {
    const b = document.querySelector(sel); const ic = b.querySelector('svg'); const lb = b.querySelector('.btn-label');
    out[name] = { btnX: Math.round(r(b).left), btnW: Math.round(r(b).width), iconX: Math.round(r(ic).left - r(b).left), labelX: Math.round(r(lb).left - r(b).left), h: Math.round(r(b).height) }; }
  const note = document.querySelector('#play-web-note'); out.noteX = Math.round(r(note).left); out.hScroll = document.documentElement.scrollWidth > innerWidth; return JSON.stringify(out); })()`;
const rows = [];
for (const [w, h] of [[375, 812], [768, 1024], [1024, 800], [1400, 900]]) {
  await S('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile: w < 600 });
  await S('Page.navigate', { url: BASE + '/' }); await sleep(2500);
  const v = JSON.parse((await S('Runtime.evaluate', { expression: MEASURE, returnByValue: true })).result.result.value);
  await S('Runtime.evaluate', { expression: `window.scrollTo(0, document.querySelector('.cta').getBoundingClientRect().top + scrollY - 120)` }); await sleep(300);
  const img = await S('Page.captureScreenshot', { format: 'png' });
  writeFileSync(join(OUT, `hero-${w}.png`), Buffer.from(img.result.data, 'base64'));
  const aligned = ['download', 'play', 'support'].every((k) => v[k].iconX === v.download.iconX && v[k].labelX === v.download.labelX);
  rows.push({ w, aligned, ...v });
  console.log(String(w).padStart(4), aligned ? 'ALIGNED' : 'MISALIGNED', 'icon/label x in button: dl', v.download.iconX + '/' + v.download.labelX, 'play', v.play.iconX + '/' + v.play.labelX, 'support', v.support.iconX + '/' + v.support.labelX, '| heights', v.download.h, v.play.h, v.support.h, '| hscroll', v.hScroll);
}
writeFileSync(join(OUT, 'measure.json'), JSON.stringify(rows, null, 2));
chrome.kill();
process.exit(rows.every((r) => r.aligned && !r.hScroll) ? 0 : 1);
