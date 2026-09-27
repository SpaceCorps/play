// SpaceCorps 2027 download site: offer the visitor's platform, fill in sizes and checksums from
// release.json (written by the game's scripts/publish-release.sh), show whether the game
// server is up, and write the patch notes' dates in the visitor's language. The patch notes
// page (patchnotes.html) has the top bar only: no downloads there. Texts come from i18n.js (keys in i18n/<language>.json), and are written again
// when the visitor switches languages. No cookies, no third parties: the only requests are
// release.json, the language files and the game server's /health; the only thing kept is the
// visitor's language pick (i18n.js).
(() => {
  'use strict';

  const RELEASES = 'https://github.com/SpaceCorps/play/releases';
  const LATEST = RELEASES + '/latest/download/';
  const DEFAULT_SERVER = 'https://spacecorps-game.sliplane.app';
  const PLATFORMS = {
    macos: { asset: 'SpaceCorps2027-macos-universal.dmg', name: 'macOS', sub: 'hero.sub.macos', help: 'help-macos' },
    windows: { asset: 'SpaceCorps2027-windows-x86_64.zip', name: 'Windows', sub: 'hero.sub.windows', help: 'help-windows' },
    linux: { asset: 'SpaceCorps2027-linux-x86_64.AppImage', name: 'Linux', sub: 'hero.sub.linux', help: 'help-linux' },
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
    if ((uaData && uaData.mobile) || /android|iphone|ipad|ipod/i.test(ua)) return 'mobile';
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

  // ----- platform and release -----
  const downloads = Boolean($('#dl-main')); // the main page, not patchnotes.html
  const os = detectOS();
  const mine = PLATFORMS[os];
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
  }

  function paintMain() {
    if (!texts || !downloads) return;
    const a = offered();
    if (a) {
      setText($('#dl-main-label'), t('hero.download-for', { platform: mine.name }));
      const sub = t(mine.sub);
      setText($('#dl-main-sub'), sub && Number.isFinite(a.size) ? `${sub} · ${I18N.size(a.size)}` : sub);
      setText($('#dl-other'), t('hero.other-platforms'));
    } else {
      setText($('#dl-main-label'), os === 'mobile' ? t('hero.download-mobile') : t('hero.download'));
      setText($('#dl-main-sub'), 'macOS · Windows · Linux');
      setText($('#dl-other'), t('hero.all-platforms'));
    }
    if (os === 'mobile') setText($('#dl-note'), t('hero.note-mobile'));
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
