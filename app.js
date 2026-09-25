// SpaceCorps 2027 download site: offer the visitor's platform, fill in sizes and checksums from
// release.json (written by the game's scripts/publish-release.sh), and show whether the game
// server is up. No cookies, no storage, no third parties: the only requests are release.json
// and the game server's /health.
(() => {
  'use strict';

  const RELEASES = 'https://github.com/SpaceCorps/play/releases';
  const LATEST = RELEASES + '/latest/download/';
  const DEFAULT_SERVER = 'https://spacecorps-game.sliplane.app';
  const PLATFORMS = {
    macos: { asset: 'SpaceCorps2027-macos-universal.dmg', label: 'Download for macOS', sub: 'Apple silicon and Intel', help: 'help-macos' },
    windows: { asset: 'SpaceCorps2027-windows-x86_64.zip', label: 'Download for Windows', sub: 'Windows 10 and 11, x64', help: 'help-windows' },
    linux: { asset: 'SpaceCorps2027-linux-x86_64.AppImage', label: 'Download for Linux', sub: 'x86_64 AppImage', help: 'help-linux' },
  };

  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  function detectOS() {
    const uaData = navigator.userAgentData;
    const platform = (uaData && uaData.platform) || navigator.platform || '';
    const ua = navigator.userAgent || '';
    if ((uaData && uaData.mobile) || /android|iphone|ipad|ipod/i.test(ua)) return 'mobile';
    // iPadOS asks for desktop pages as a Mac with a touch screen.
    if (/mac/i.test(platform) && navigator.maxTouchPoints > 1) return 'mobile';
    if (/win/i.test(platform) || /windows nt/i.test(ua)) return 'windows';
    if (/mac/i.test(platform) || /mac os x/i.test(ua)) return 'macos';
    if (/cros/i.test(ua)) return 'other';
    if (/linux|x11/i.test(platform) || /linux/i.test(ua)) return 'linux';
    return 'other';
  }

  function formatSize(bytes) {
    const mb = bytes / (1024 * 1024);
    return (mb < 10 ? mb.toFixed(1) : Math.round(mb)) + ' MB';
  }

  function formatDate(iso) {
    const d = new Date(iso + 'T00:00:00Z');
    if (Number.isNaN(d.getTime())) return iso;
    return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' });
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

  function wireCopy(button, getText) {
    const label = button.getAttribute('aria-label') || 'Copy';
    button.addEventListener('click', async () => {
      if (!(await copyText(getText()))) return;
      button.classList.add('done');
      button.setAttribute('aria-label', 'Copied');
      $('use', button).setAttribute('href', '#i-check');
      setTimeout(() => {
        button.classList.remove('done');
        button.setAttribute('aria-label', label);
        $('use', button).setAttribute('href', '#i-copy');
      }, 1600);
    });
  }

  function copyButton(label) {
    const b = document.createElement('button');
    b.type = 'button';
    b.className = 'copy';
    b.setAttribute('aria-label', label);
    b.innerHTML = '<svg class="icon" aria-hidden="true"><use href="#i-copy"/></svg>';
    return b;
  }

  $$('button[data-copy]').forEach((b) => wireCopy(b, () => $(b.dataset.copy).textContent));

  // ----- platform and release -----
  const os = detectOS();
  const mine = PLATFORMS[os];
  let assets = null; // name -> {size, sha256} once release.json is in

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
      $('#dl-main-label').textContent = mine.label;
      $('#dl-main-sub').textContent = a.size ? `${mine.sub} · ${formatSize(a.size)}` : mine.sub;
      $('#dl-other').textContent = 'Other platforms';
      const card = $(`.platform[data-asset="${mine.asset}"]`);
      if (card) card.classList.add('is-you');
      return;
    }
    main.href = '#download';
    $('#dl-main-label').textContent = os === 'mobile' ? 'Get it on your computer' : 'Download';
    $('#dl-main-sub').textContent = 'macOS · Windows · Linux';
    $('#dl-other').textContent = 'All platforms';
    if (os === 'mobile') {
      $('#dl-note').textContent = 'SpaceCorps 2027 is a desktop game for macOS, Windows and Linux.';
    }
  }

  function renderRelease(release) {
    const list = Array.isArray(release.assets) ? release.assets : [];
    assets = {};
    list.forEach((a) => { if (a && a.name) assets[a.name] = a; });
    if (release.version && list.length) {
      const date = release.date ? ` · ${formatDate(release.date)}` : '';
      $('#release-line').textContent = `Version ${release.version}${date}, for every platform.`;
    }
    if (!list.length) {
      const n = $('#release-notice');
      n.textContent = 'The first release is on its way: the downloads appear here as soon as it is out.';
      n.hidden = false;
    }
    $$('.platform').forEach((card) => {
      const a = assets[card.dataset.asset];
      const link = $('.dl', card);
      if (!a) {
        card.classList.add('is-missing');
        link.removeAttribute('href');
        link.setAttribute('aria-disabled', 'true');
        $('span', link).textContent = 'Not available yet';
        return;
      }
      $('.size', card).textContent = formatSize(a.size);
      const dd = $('.sha', card);
      const code = $('code', dd);
      code.textContent = a.sha256;
      code.title = a.sha256;
      const b = copyButton(`Copy the SHA-256 of ${a.name}`);
      wireCopy(b, () => a.sha256);
      dd.appendChild(b);
    });
    if (release.server) setServer(release.server);
    renderMain();
  }

  // Opening the matching first-launch help when the download starts.
  $('#dl-main').addEventListener('click', () => {
    if (offered()) {
      const help = document.getElementById(mine.help);
      if (help) help.open = true;
    }
  });

  renderMain();
  fetch('release.json', { cache: 'no-cache' })
    .then((r) => (r.ok ? r.json() : Promise.reject(new Error(r.status))))
    .then(renderRelease)
    .catch(() => { /* keep the static links */ });

  // ----- game server status -----
  let server = DEFAULT_SERVER;
  let timer = null;

  function setServer(url) {
    if (typeof url !== 'string' || !/^https?:\/\//.test(url)) return;
    const next = url.replace(/\/+$/, '');
    if (next === server) return;
    server = next;
    $$('.server-url').forEach((el) => { el.textContent = server; });
    setStatus('checking');
    check();
  }

  function setStatus(state, detail) {
    const texts = {
      checking: ['Server', 'checking…'],
      online: ['Server online', 'online'],
      offline: ['Server offline', 'not answering right now'],
    }[state];
    $$('[data-status]').forEach((el) => {
      el.dataset.status = state;
      const t = $('.status-text', el);
      const inline = el.classList.contains('status-inline');
      t.textContent = inline ? `(${state === 'online' && detail ? detail : texts[1]})` : texts[0];
    });
    const pill = $('.status');
    pill.title = state === 'online'
      ? `The game server is up${detail ? ': ' + detail : ''}`
      : state === 'offline' ? 'The game server is not answering' : 'Checking the game server';
  }

  async function probe(path) {
    const ctrl = new AbortController();
    const t = setTimeout(() => ctrl.abort(), 8000);
    try {
      return await fetch(server + path, { cache: 'no-store', signal: ctrl.signal, credentials: 'omit' });
    } finally {
      clearTimeout(t);
    }
  }

  function describe(json) {
    if (!json || typeof json !== 'object') return '';
    const n = [json.playersOnline, json.players_online, json.online, json.players].find((v) => Number.isFinite(v));
    return n === undefined ? '' : `${n} ${n === 1 ? 'pilot' : 'pilots'} online`;
  }

  let run = 0; // only the latest check reports and schedules the next one
  async function check() {
    clearTimeout(timer);
    const ticket = ++run;
    let state = 'offline';
    let detail = '';
    try {
      let r = await probe('/health');
      // Servers from before /health existed still answer the company list.
      if (r.status === 404) r = await probe('/api/company');
      if (r.ok) {
        state = 'online';
        try { detail = describe(await r.json()); } catch { detail = ''; }
      }
    } catch {
      state = 'offline';
    }
    if (ticket !== run) return;
    setStatus(state, detail);
    timer = setTimeout(check, 60000);
  }

  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible') check();
    else clearTimeout(timer);
  });
  check();
})();
