// Drives a real Chrome over CDP (no dependencies; Node 22+ has fetch and WebSocket).
// Real-Chrome test of the download page's processor detection and the x64 | ARM64 switch.
// Serve the repository (python -m http.server 8767), then: node scripts/test-arch-detect.mjs http://127.0.0.1:8767 /tmp/arch-shots
import { spawn } from 'node:child_process';
import { mkdtempSync, mkdirSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const BASE = process.argv[2];
const OUT = process.argv[3];
mkdirSync(OUT, { recursive: true });
const CHROME = process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9333;
const profile = mkdtempSync(join(tmpdir(), 'cdp-prof-'));
const chrome = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`,
  '--no-first-run', '--no-default-browser-check', '--window-size=1280,900', '--hide-scrollbars', 'about:blank'], { stdio: 'ignore' });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function wsUrl() {
  for (let i = 0; i < 60; i++) {
    try { const r = await fetch(`http://127.0.0.1:${PORT}/json/version`); return (await r.json()).webSocketDebuggerUrl; } catch { await sleep(250); }
  }
  throw new Error('Chrome did not start');
}

class Cdp {
  constructor(url) { this.id = 0; this.cbs = new Map(); this.ws = new WebSocket(url); this.ready = new Promise((r) => this.ws.addEventListener('open', r));
    this.ws.addEventListener('message', (e) => { const m = JSON.parse(e.data); if (m.id && this.cbs.has(m.id)) { const { res, rej } = this.cbs.get(m.id); this.cbs.delete(m.id); m.error ? rej(new Error(JSON.stringify(m.error))) : res(m.result); } }); }
  send(method, params = {}, sessionId) { const id = ++this.id; return new Promise((res, rej) => { this.cbs.set(id, { res, rej }); this.ws.send(JSON.stringify({ id, method, params, sessionId })); }); }
}

const WIN_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const EDGE_UA = WIN_UA + ' Edg/131.0.0.0';
const MAC_UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const LINUX_UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const LINUX_ARM_UA = 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const FIREFOX_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0';
const meta = (platform, architecture) => ({ brands: [{ brand: 'Chromium', version: '131' }, { brand: 'Google Chrome', version: '131' }], fullVersion: '131.0.0.0', platform, platformVersion: platform === 'Windows' ? '15.0.0' : '14.0.0', architecture, model: '', mobile: false, bitness: '64', wow64: false });
// what Firefox/Safari expose: no userAgentData at all; optionally a WebGL renderer string
const noUAData = (renderer) => `Object.defineProperty(navigator,'userAgentData',{get:()=>undefined});` + (renderer ? `
const g=(P)=>{const o=P.prototype.getParameter;P.prototype.getParameter=function(p){if(p===0x9246||p===37446)return ${JSON.stringify(renderer)};if(p===0x9245||p===37445)return 'Google Inc.';return o.call(this,p)};const e=P.prototype.getExtension;P.prototype.getExtension=function(n){return n==='WEBGL_debug_renderer_info'?{UNMASKED_VENDOR_WEBGL:37445,UNMASKED_RENDERER_WEBGL:37446}:e.call(this,n)}};g(WebGLRenderingContext);if(window.WebGL2RenderingContext)g(WebGL2RenderingContext);` : '');

const SCENARIOS = [
  { name: 'win-arm-chrome', ua: WIN_UA, metadata: meta('Windows', 'arm'), expect: 'windows-aarch64.zip' },
  { name: 'win-arm-edge', ua: EDGE_UA, metadata: meta('Windows', 'arm'), expect: 'windows-aarch64.zip' },
  { name: 'win-x86-chrome', ua: WIN_UA, metadata: meta('Windows', 'x86'), expect: 'windows-x86_64.zip' },
  { name: 'mac-arm-chrome', ua: MAC_UA, metadata: meta('macOS', 'arm'), expect: 'macos-universal.dmg' },
  { name: 'linux-x86-chrome', ua: LINUX_UA, metadata: meta('Linux', 'x86'), expect: 'linux-x86_64.AppImage' },
  { name: 'linux-arm-chrome', ua: LINUX_ARM_UA, metadata: meta('Linux', 'arm'), expect: 'linux-aarch64.AppImage' },
  { name: 'win-arm-firefox-noUAData-adreno', ua: FIREFOX_UA, script: noUAData('Qualcomm(R) Adreno(TM) X1-85 GPU'), expect: 'windows-aarch64.zip', hintOnly: true },
  { name: 'win-x64-firefox-noUAData-nvidia', ua: FIREFOX_UA, script: noUAData('NVIDIA GeForce RTX 4070'), expect: 'windows-x86_64.zip' },
  { name: 'win-x86-chrome-user-picks-arm', ua: WIN_UA, metadata: meta('Windows', 'x86'), expect: 'windows-x86_64.zip', click: 'arm64', expectAfterClick: 'windows-aarch64.zip', reload: true },
  { name: 'win-arm-firefox-noUAData-unknown-then-switch', ua: FIREFOX_UA, script: noUAData(''), expect: 'windows-x86_64.zip', click: 'arm64', expectAfterClick: 'windows-aarch64.zip', reload: true },
];

const READ = `(() => { const q = (s) => document.querySelector(s); return JSON.stringify({
  main: q('#dl-main').href.split('/').pop(), sub: q('#dl-main-sub').textContent.trim(),
  you: [...document.querySelectorAll('.platform.is-you')].map((c) => c.dataset.asset),
  switchShown: !!q('#arch-switch') && !q('#arch-switch').hidden,
  switchChecked: [...document.querySelectorAll('#arch-switch [role=radio][aria-checked=true]')].map((b) => b.dataset.arch),
  storage: (() => { try { return localStorage.getItem('sc-arch'); } catch { return 'n/a'; } })() }); })()`;

const results = [];
try {
  const cdp = new Cdp(await wsUrl());
  await cdp.ready;
  for (const sc of SCENARIOS) {
    const { browserContextId } = await cdp.send('Target.createBrowserContext'); // own storage per scenario
    const { targetId } = await cdp.send('Target.createTarget', { url: 'about:blank', browserContextId });
    const { sessionId } = await cdp.send('Target.attachToTarget', { targetId, flatten: true });
    const S = (m, p) => cdp.send(m, p, sessionId);
    await S('Page.enable'); await S('Runtime.enable');
    await S('Emulation.setDeviceMetricsOverride', { width: 1280, height: 900, deviceScaleFactor: 1, mobile: false });
    await S('Page.addScriptToEvaluateOnNewDocument', { source: "Object.defineProperty(navigator,'maxTouchPoints',{get:()=>0})" }); // this PC has a touch screen
    await S('Emulation.setUserAgentOverride', { userAgent: sc.ua, acceptLanguage: 'en-US', ...(sc.metadata ? { userAgentMetadata: sc.metadata } : {}) });
    if (sc.script) await S('Page.addScriptToEvaluateOnNewDocument', { source: sc.script });
    await S('Page.navigate', { url: BASE + '/' });
    await sleep(2500);
    const ev = async (expr) => JSON.parse((await S('Runtime.evaluate', { expression: expr, returnByValue: true })).result.value);
    let r = await ev(READ);
    const row = { scenario: sc.name, ...r, expect: sc.expect, pass: r.main.endsWith(sc.expect) && r.you.every((a) => a.endsWith(sc.expect)) && r.you.length === 1 };
    const shot = async (suffix) => { const img = await S('Page.captureScreenshot', { format: 'png' }); writeFileSync(join(OUT, `${sc.name}${suffix}.png`), Buffer.from(img.data, 'base64')); };
    await shot('-hero');
    if (sc.click) {
      await S('Runtime.evaluate', { expression: `document.querySelector('#arch-switch [data-arch=${sc.click}]').click()` });
      await sleep(500);
      r = await ev(READ);
      row.afterClick = r; row.expectAfterClick = sc.expectAfterClick;
      row.pass = row.pass && r.main.endsWith(sc.expectAfterClick) && r.you.length === 1 && r.you[0].endsWith(sc.expectAfterClick) && r.storage === 'arm64';
      await shot('-after-click');
      if (sc.reload) {
        await S('Page.reload'); await sleep(2500);
        const r2 = await ev(READ);
        row.afterReload = r2;
        row.pass = row.pass && r2.main.endsWith(sc.expectAfterClick) && r2.switchChecked.join() === 'arm64';
      }
    }
    // download list screenshot with the highlighted card
    await S('Runtime.evaluate', { expression: `window.scrollTo({top: document.querySelector('#download-title').getBoundingClientRect().top + scrollY - 70, behavior: 'instant'})` });
    await sleep(400);
    await shot('-list');
    results.push(row);
    await cdp.send('Target.closeTarget', { targetId });
  }
} finally {
  chrome.kill();
}
writeFileSync(join(OUT, 'results.json'), JSON.stringify(results, null, 2));
for (const r of results) console.log((r.pass ? 'PASS' : 'FAIL'), r.scenario.padEnd(46), '| main:', r.main, '| sub:', r.sub, '| is-you:', r.you.join(','), '| switch:', r.switchShown ? r.switchChecked.join() : '-');
console.log(results.every((r) => r.pass) ? 'ALL PASS' : 'SOME FAILED');
process.exit(results.every((r) => r.pass) ? 0 : 1);
