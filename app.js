// SpaceCorps 2027 download site: offer the visitor's platform, fill in sizes and checksums from
// release.json (written by the game's scripts/publish-release.sh), show whether the game
// server is up, and write the patch notes' dates in the visitor's language. The patch notes
// page (patchnotes.html) has the top bar only: no downloads there. Texts come from i18n.js (keys in i18n/<language>.json), and are written again
// when the visitor switches languages. No cookies, no third parties: the only requests are
// release.json, web.json, the language files and the game server's /health; the only thing kept
// is the visitor's language pick (i18n.js). The hero's second button, Play in browser, opens the
// web version of the game: its address is web.json's "url" (DEFAULT_WEB until that file says
// otherwise), and it always links, even while the web version isn't hosted yet.
(() => {
  'use strict';

  const RELEASES = 'https://github.com/SpaceCorps/play/releases';
  const LATEST = RELEASES + '/latest/download/';
  const DEFAULT_SERVER = 'https://spacecorps-game.sliplane.app';
  const DEFAULT_WEB = 'https://web.spacecorps.xyz/'; // placeholder until the web version is hosted
  const PLATFORMS = {
    macos: { asset: 'SpaceCorps2027-macos-universal.dmg', name: 'macOS', sub: 'hero.sub.macos', help: 'help-macos' },
    windows: { asset: 'SpaceCorps2027-windows-x86_64.zip', name: 'Windows', sub: 'hero.sub.windows', help: 'help-windows' },
    linux: { asset: 'SpaceCorps2027-linux-x86_64.AppImage', name: 'Linux', sub: 'hero.sub.linux', help: 'help-linux' },
    // The ARM64 builds of Windows and Linux: offered when the browser says the computer is ARM.
    'windows-arm': { asset: 'SpaceCorps2027-windows-aarch64.zip', name: 'Windows', sub: 'hero.sub.windows-arm', help: 'help-windows' },
    android: { asset: 'SpaceCorps2027-android-aarch64.apk', name: 'Android', sub: 'hero.sub.android', help: 'help-android' },
    'linux-arm': { asset: 'SpaceCorps2027-linux-aarch64.AppImage', name: 'Linux', sub: 'hero.sub.linux-arm', help: 'help-linux' },
  };

  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  // ----- texts -----
  // Until i18n.js has its dictionaries in, the English in the HTML stays; paint() then writes
  // every text this file owns, and again after each language switch.
  const I18N = window.SpaceCorpsI18n;
  let texts = false;
  const t = (key, vars) => (I18N ? I18N.t(key, vars) : null);
  const setText = (el, text) => { if (el && typeof text === 'string') el.textContent = text; };
  const setLabel = (el, text) => { if (el && typeof text === 'string') el.setAttribute('aria-label', text); };

  function detectOS() {
    const uaData = navigator.userAgentData;
    const platform = (uaData && uaData.platform) || navigator.platform || '';
    const ua = navigator.userAgent || '';
    // Android phones and tablets get the APK; iPhone and iPad (no app yet) stay 'mobile'.
    if ((uaData && /android/i.test(uaData.platform || '')) || /android/i.test(ua)) return 'android';
    if ((uaData && uaData.mobile) || /iphone|ipad|ipod/i.test(ua)) return 'mobile';
    // iPadOS asks for desktop pages as a Mac with a touch screen.
    if (/mac/i.test(platform) && navigator.maxTouchPoints > 1) return 'mobile';
    if (/win/i.test(platform) || /windows nt/i.test(ua)) return 'windows';
    if (/mac/i.test(platform) || /mac os x/i.test(ua)) return 'macos';
    if (/cros/i.test(ua)) return 'other';
    if (/linux|x11/i.test(platform) || /linux/i.test(ua)) return 'linux';
    return 'other';
  }

  // ----- copy buttons -----
  async function copyText(text) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch {
      const area = document.createElement('textarea');
      area.value = text;
      area.setAttribute('readonly', '');
      area.style.position = 'fixed';
      area.style.opacity = '0';
      document.body.appendChild(area);
      area.select();
      let ok = false;
      try { ok = document.execCommand('copy'); } catch { ok = false; }
      area.remove();
      return ok;
    }
  }

  // label(): the button's name in the current language, for when "Copied" is over.
  function wireCopy(button, getText, label) {
    button.addEventListener('click', async () => {
      if (!(await copyText(getText()))) return;
      button.classList.add('done');
      setLabel(button, t('copy.done'));
      $('use', button).setAttribute('href', '#i-check');
      clearTimeout(button.copyReset);
      button.copyReset = setTimeout(() => {
        button.classList.remove('done');
        setLabel(button, label());
        $('use', button).setAttribute('href', '#i-copy');
      }, 1600);
    });
  }

  function copyButton() {
    const b = document.createElement('button');
    b.type = 'button';
    b.className = 'copy';
    b.innerHTML = '<svg class="icon" aria-hidden="true"><use href="#i-copy"/></svg>';
    return b;
  }

  $$('button[data-copy]').forEach((b) => wireCopy(b, () => $(b.dataset.copy).textContent, () => t('help.copy-command')));

  // The processor. Chromium browsers say it (userAgentData.getHighEntropyValues), a Linux user agent
  // names aarch64/arm; Firefox and Safari never do (they claim 'Win64; x64' even on Windows on ARM),
  // so on Windows a WebGL renderer of a Qualcomm GPU is taken as a hint. The visitor's own pick
  // (the x64 | ARM64 switch, remembered) beats all of it. Nothing known: the x64 package stays the
  // big button and the ARM64 ones are in the list, always visible.
  const ARCH_KEY = 'sc-arch';
  function readArch() {
    try { const v = localStorage.getItem(ARCH_KEY); return v === 'x64' || v === 'arm64' ? v : ''; } catch { return ''; }
  }
  function saveArch(v) {
    try { localStorage.setItem(ARCH_KEY, v); } catch { /* private mode: the pick lasts for this visit */ }
  }
  let archPicked = readArch(); // the visitor's choice
  let archSaid = ''; // 'arm64' | 'x64' | '': what the browser says
  let archHint = ''; // 'arm64' | '': the WebGL hint
  const ARM_GPU = /adreno|qualcomm|snapdragon/i;
  function archFromUserAgent() {
    return /aarch64|arm64|armv8/i.test(navigator.userAgent || '') ? 'arm64' : '';
  }
  async function detectArch() {
    const uaData = navigator.userAgentData;
    if (uaData && typeof uaData.getHighEntropyValues === 'function') {
      try {
        const v = await uaData.getHighEntropyValues(['architecture', 'bitness']);
        if (/arm/i.test(v.architecture || '')) return 'arm64';
        if (/x86/i.test(v.architecture || '')) return 'x64';
      } catch { /* denied or unsupported: fall through */ }
    }
    return archFromUserAgent();
  }
  function webglRenderer() {
    try {
      const gl = document.createElement('canvas').getContext('webgl');
      if (!gl) return '';
      const info = gl.getExtension('WEBGL_debug_renderer_info');
      return String((info && gl.getParameter(info.UNMASKED_RENDERER_WEBGL)) || '');
    } catch { return ''; }
  }
  const currentArch = () => archPicked || archSaid || archHint || 'x64';

  // ----- platform and release -----
  const downloads = Boolean($('#dl-main')); // the main page, not patchnotes.html
  const os = detectOS();
  const platformFor = () => (currentArch() === 'arm64' && PLATFORMS[os + '-arm']) || PLATFORMS[os];
  let mine = platformFor();
  let release = null; // release.json once it is in
  let assets = null; // name -> {size, sha256}

  // The big button: the visitor's package when the release has it (or before release.json is
  // in, trusting the static links), else a jump to the platform list.
  function offered() {
    if (!mine) return null;
    if (!assets) return {};
    return assets[mine.asset] || null;
  }

  function renderMain() {
    const main = $('#dl-main');
    const a = offered();
    $$('.platform.is-you').forEach((c) => c.classList.remove('is-you'));
    if (a) {
      main.href = LATEST + mine.asset;
      const card = $(`.platform[data-asset="${mine.asset}"]`);
      if (card) card.classList.add('is-you');
    } else {
      main.href = '#download';
    }
    paintMain();
    paintSwitch();
  }

  function paintMain() {
    if (!texts || !downloads) return;
    const a = offered();
    if (a) {
      setText($('#dl-main-label'), t('hero.download'));
      // The system's name first, unless the package line already starts with it (Windows 10 and 11).
      const sub = t(mine.sub);
      const parts = [sub && sub.startsWith(mine.name) ? null : mine.name, sub, Number.isFinite(a.size) ? I18N.size(a.size).replace(/ /g, '\u00a0') : null];
      setText($('#dl-main-sub'), parts.filter(Boolean).join(' · '));
      setText($('#dl-other'), t('hero.other-platforms'));
    } else {
      setText($('#dl-main-label'), os === 'mobile' ? t('hero.download-mobile') : t('hero.download'));
      setText($('#dl-main-sub'), 'macOS · Windows · Linux');
      setText($('#dl-other'), t('hero.all-platforms'));
    }
    if (os === 'mobile' || os === 'android') {
      setText($('#dl-note'), t(os === 'android' ? 'hero.note-android' : 'hero.note-mobile'));
      // The web version needs a desktop browser: on a phone the button stays, but quieter.
      setText($('#play-web .btn-sub'), t('hero.play-web-sub-mobile'));
    }
  }

  // The x64 | ARM64 switch under the big button (Windows only): shows the current processor, and a
  // click is the visitor's own pick, kept for the next visit.
  const archSwitch = $('#arch-switch');
  function paintSwitch() {
    if (!archSwitch) return;
    archSwitch.hidden = !(downloads && os === 'windows');
    $$('[role=radio]', archSwitch).forEach((b) => {
      const on = b.dataset.arch === currentArch();
      b.setAttribute('aria-checked', on ? 'true' : 'false');
      b.tabIndex = on ? 0 : -1;
    });
  }
  function archChanged() {
    mine = platformFor();
    renderMain();
    paintSwitch();
  }
  if (archSwitch) {
    archSwitch.addEventListener('click', (e) => {
      const b = e.target.closest('[role=radio]');
      if (!b) return;
      archPicked = b.dataset.arch;
      saveArch(archPicked);
      archChanged();
    });
    archSwitch.addEventListener('keydown', (e) => {
      if (!['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(e.key)) return;
      e.preventDefault();
      const next = currentArch() === 'arm64' ? 'x64' : 'arm64';
      archPicked = next;
      saveArch(next);
      archChanged();
      const b = $(`[data-arch="${next}"]`, archSwitch);
      if (b) b.focus();
    });
  }

  // Windows or Linux on ARM64: the big button and the highlighted card switch to the ARM64 package.
  if (downloads && (os === 'windows' || os === 'linux')) {
    detectArch().then((arch) => {
      archSaid = arch;
      if (os === 'windows' && !arch) archHint = ARM_GPU.test(webglRenderer()) ? 'arm64' : '';
      archChanged();
    });
  }

  function renderRelease(json) {
    release = json && typeof json === 'object' ? json : {};
    const list = Array.isArray(release.assets) ? release.assets : [];
    assets = {};
    list.forEach((a) => { if (a && a.name) assets[a.name] = a; });
    $$('.platform').forEach((card) => {
      const a = assets[card.dataset.asset];
      const link = $('.dl', card);
      if (!a) {
        card.classList.add('is-missing');
        link.removeAttribute('href');
        link.setAttribute('aria-disabled', 'true');
        return;
      }
      const dd = $('.sha', card);
      const code = $('code', dd);
      code.textContent = a.sha256;
      code.title = a.sha256;
      const b = copyButton();
      wireCopy(b, () => a.sha256, () => t('download.copy-sha', { file: a.name }));
      dd.appendChild(b);
    });
    if (release.server) setServer(release.server);
    renderMain();
    paintRelease();
  }

  function paintRelease() {
    if (!texts || !release) return;
    const list = Array.isArray(release.assets) ? release.assets : [];
    if (release.version && list.length) {
      setText($('#release-line'), release.date
        ? t('download.version-date', { version: release.version, date: I18N.date(release.date) })
        : t('download.version', { version: release.version }));
    }
    if (!list.length) {
      const n = $('#release-notice');
      setText(n, t('download.coming'));
      n.hidden = false;
    }
    $$('.platform').forEach((card) => {
      const a = assets[card.dataset.asset];
      if (!a) {
        setText($('.dl span', card), t('download.unavailable'));
        return;
      }
      if (Number.isFinite(a.size)) {
        const el = $('.size', card);
        setText(el, I18N.size(a.size));
        if (el) el.title = I18N.sizeTitle(a.size);
      }
      const b = $('.sha .copy', card);
      if (b && !b.classList.contains('done')) setLabel(b, t('download.copy-sha', { file: a.name }));
    });
  }

  if (downloads) {
    // Opening the matching first-launch help when the download starts.
    $('#dl-main').addEventListener('click', () => {
      if (offered()) {
        const help = document.getElementById(mine.help);
        if (help) help.open = true;
      }
    });

    renderMain();
    $('#play-web').href = DEFAULT_WEB;
    if (os === 'mobile') {
      $('#play-web').classList.replace('btn-play', 'btn-secondary');
      $('#play-web .btn-sub').setAttribute('data-i18n', 'hero.play-web-sub-mobile');
    }
    fetch('web.json', { cache: 'no-cache' })
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(r.status))))
      .then((json) => {
        const url = json && json.url;
        if (typeof url === 'string' && /^https:\/\//.test(url)) $('#play-web').href = url;
      })
      .catch(() => { /* keep DEFAULT_WEB */ });
    fetch('release.json', { cache: 'no-cache' })
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(r.status))))
      .then(renderRelease)
      .catch(() => { /* keep the static links */ });
  }

  // ----- patch notes -----
  // The dates are written in English (25 September 2026) when the notes are generated; each is
  // written out again in the page's language. The notes themselves stay English.
  function paintDates() {
    if (!texts) return;
    $$('time[data-date]').forEach((el) => setText(el, I18N.date(el.getAttribute('datetime'))));
  }

  // ----- game server status -----
  let server = DEFAULT_SERVER;
  let timer = null;
  let status = { state: 'checking', pilots: null };
  const STATUS = {
    checking: { pill: 'status.pill.checking', inline: 'status.inline.checking', tip: 'status.tip.checking' },
    online: { pill: 'status.pill.online', inline: 'status.inline.online', tip: 'status.tip.online' },
    offline: { pill: 'status.pill.offline', inline: 'status.inline.offline', tip: 'status.tip.offline' },
  };

  function setServer(url) {
    if (typeof url !== 'string' || !/^https?:\/\//.test(url)) return;
    const next = url.replace(/\/+$/, '');
    if (next === server) return;
    server = next;
    $$('.server-url').forEach((el) => { el.textContent = server; });
    setStatus('checking', null);
    check();
  }

  function setStatus(state, pilots) {
    status = { state, pilots };
    $$('[data-status]').forEach((el) => { el.dataset.status = state; });
    paintStatus();
  }

  function paintStatus() {
    if (!texts) return;
    const { state, pilots } = status;
    const keys = STATUS[state];
    const count = state === 'online' && pilots !== null ? I18N.plural('status.pilots', pilots) : null;
    $$('[data-status]').forEach((el) => {
      const text = $('.status-text', el);
      if (el.classList.contains('status-inline')) {
        setText(text, t('status.inline.wrap', { state: count || t(keys.inline) }));
      } else {
        setText(text, t(keys.pill));
      }
    });
    const tip = count ? t('status.tip.online-pilots', { pilots: count }) : t(keys.tip);
    if (tip) $('.status').title = tip;
  }

  async function probe(path) {
    const ctrl = new AbortController();
    const timeout = setTimeout(() => ctrl.abort(), 8000);
    try {
      return await fetch(server + path, { cache: 'no-store', signal: ctrl.signal, credentials: 'omit' });
    } finally {
      clearTimeout(timeout);
    }
  }

  function pilotsOnline(json) {
    if (!json || typeof json !== 'object') return null;
    const n = [json.playersOnline, json.players_online, json.online, json.players].find((v) => Number.isFinite(v));
    return n === undefined ? null : n;
  }

  let run = 0; // only the latest check reports and schedules the next one
  async function check() {
    clearTimeout(timer);
    const ticket = ++run;
    let state = 'offline';
    let pilots = null;
    try {
      let r = await probe('/health');
      // Servers from before /health existed still answer the company list.
      if (r.status === 404) r = await probe('/api/company');
      if (r.ok) {
        state = 'online';
        try { pilots = pilotsOnline(await r.json()); } catch { pilots = null; }
      }
    } catch {
      state = 'offline';
    }
    if (ticket !== run) return;
    setStatus(state, pilots);
    timer = setTimeout(check, 60000);
  }

  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible') check();
    else clearTimeout(timer);
  });
  check();

  // ----- languages -----
  // i18n.js has just put the page's own texts in (which resets the ones below to their
  // defaults); write this file's texts over them.
  if (I18N) {
    I18N.subscribe(() => {
      texts = true;
      paintMain();
      paintRelease();
      paintStatus();
      paintDates();
    });
  }
})();
