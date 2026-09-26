// SpaceCorps 2027 download site: the page's language, one of the game's ten.
//
// The English texts stay in index.html, so the page reads fine without JavaScript and for
// crawlers. Every text carries a key (data-i18n, data-i18n-alt, -title, -aria-label, -content);
// this script picks the language, loads i18n/<code>.json plus i18n/en.json (the fallback for a
// key a translation lacks, and the source of the texts app.js writes) and puts the texts in place.
//
// Which language: ?lang= in the address (shareable), else the visitor's last pick (localStorage),
// else the browser's languages (navigator.languages, matched like the game: de-AT is de, pt-PT
// pt-BR, zh-TW zh-CN), else English.
//
// Loaded without defer in <head>: <html lang>, and with it the CJK font order in style.css, is
// right before the first paint, and for a language other than English the page stays hidden
// until its texts are in (at most HOLD_MS), so nobody sees English flash by.
(() => {
  'use strict';

  // As in the game's language picker (client/src/i18n/languages.rs), in its order. short: the
  // name on the menu button where the full one is long. intl: the locale for numbers and dates
  // when it isn't the code (English dates as the page always wrote them: 25 September 2026).
  const LANGUAGES = [
    { code: 'en', name: 'English', intl: 'en-GB' },
    { code: 'de', name: 'Deutsch' },
    { code: 'es', name: 'Español' },
    { code: 'fr', name: 'Français' },
    { code: 'pt-BR', name: 'Português (Brasil)', short: 'Português' },
    { code: 'sv', name: 'Svenska' },
    { code: 'ru', name: 'Русский' },
    { code: 'ja', name: '日本語' },
    { code: 'ko', name: '한국어' },
    { code: 'zh-CN', name: '简体中文' },
  ];
  const SOURCE = 'en';
  const STORE_KEY = 'spacecorps.lang';
  const HOLD_MS = 1500;
  const root = document.documentElement;
  const has = (obj, key) => Object.prototype.hasOwnProperty.call(obj, key);

  // ----- which language -----
  function match(tag) {
    if (typeof tag !== 'string' || !tag.trim()) return null;
    const wanted = tag.split(';')[0].trim().replace(/_/g, '-').toLowerCase(); // de_AT, de;q=0.9
    const exact = LANGUAGES.find((l) => l.code.toLowerCase() === wanted);
    if (exact) return exact.code;
    const base = wanted.split('-')[0];
    const same = LANGUAGES.find((l) => l.code.toLowerCase().split('-')[0] === base);
    return same ? same.code : null;
  }

  function fromAddress() {
    try { return match(new URLSearchParams(location.search).get('lang')); } catch { return null; }
  }

  function fromStorage() {
    try { return match(localStorage.getItem(STORE_KEY)); } catch { return null; }
  }

  function remember(code) {
    try { localStorage.setItem(STORE_KEY, code); } catch { /* private window, blocked storage */ }
  }

  function fromBrowser() {
    const tags = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language];
    for (const tag of tags) {
      const code = match(tag);
      if (code) return code;
    }
    return null;
  }

  let lang = fromAddress() || fromStorage() || fromBrowser() || SOURCE;
  root.lang = lang;
  updateCanonical(); // <head> is parsed down to this script, the hreflang alternates included

  const info = (code) => LANGUAGES.find((l) => l.code === code) || LANGUAGES[0];

  // ----- dictionaries -----
  const dicts = Object.create(null); // code -> {key: text}
  const loading = Object.create(null); // code -> Promise

  function load(code) {
    if (!loading[code]) {
      loading[code] = fetch(`i18n/${code}.json`)
        .then((r) => (r.ok ? r.json() : Promise.reject(new Error(`i18n/${code}.json: ${r.status}`))))
        .then((dict) => { dicts[code] = dict && typeof dict === 'object' ? dict : {}; })
        .catch((err) => {
          console.warn(err);
          dicts[code] = dicts[code] || {};
          delete loading[code]; // try again on the next switch
        });
    }
    return loading[code];
  }

  // The current language's text, else English's, else undefined (the HTML keeps its English).
  function raw(key) {
    const dict = dicts[lang];
    if (dict && has(dict, key) && dict[key] !== '') return dict[key];
    const en = dicts[SOURCE];
    return en && has(en, key) ? en[key] : undefined;
  }

  const PLACEHOLDER = /\{([\w-]+)\}/g;

  function fill(text, vars) {
    if (!vars) return text;
    return text.replace(PLACEHOLDER, (whole, name) => (has(vars, name) ? String(vars[name]) : whole));
  }

  function locale() {
    return info(lang).intl || lang;
  }

  // ----- the texts app.js writes -----
  function t(key, vars) {
    let text = raw(key);
    if (text && typeof text === 'object') text = text.other;
    return typeof text === 'string' ? fill(text, vars) : null;
  }

  // A message with plural forms ({"one": "{n} pilot online", "other": "{n} pilots online"}),
  // chosen by the language's CLDR rules; {n} is the number, formatted.
  function plural(key, n, vars) {
    let text = raw(key);
    if (text && typeof text === 'object') {
      let form = 'other';
      try { form = new Intl.PluralRules(locale()).select(n); } catch { /* keep other */ }
      text = typeof text[form] === 'string' ? text[form] : text.other;
    }
    return typeof text === 'string' ? fill(text, Object.assign({}, vars, { n: number(n) })) : null;
  }

  function number(n, options) {
    try { return new Intl.NumberFormat(locale(), options).format(n); } catch { return String(n); }
  }

  // Package sizes: the file's real size in decimal megabytes (1 MB = 1,000,000 bytes), as Finder,
  // the GitHub release page and download managers show them, with one decimal: 81,818,270 bytes is
  // 81.8 MB. The exact byte count goes in the element's title (see sizeTitle).
  function size(bytes) {
    const mb = bytes / 1e6;
    const digits = mb < 100 ? 1 : 0;
    try {
      return new Intl.NumberFormat(locale(), {
        style: 'unit', unit: 'megabyte', unitDisplay: 'short',
        minimumFractionDigits: digits, maximumFractionDigits: digits,
      }).format(mb);
    } catch {
      return `${mb.toFixed(digits)} MB`;
    }
  }

  // The exact size for a tooltip: "81,818,270 bytes" in the language's digit grouping.
  function sizeTitle(bytes) {
    try {
      return `${new Intl.NumberFormat(locale()).format(bytes)} B`;
    } catch {
      return `${bytes} B`;
    }
  }

  // A release date (2026-09-25) written out: 25 September 2026, 25. September 2026, 2026年9月25日.
  function date(iso) {
    const d = new Date(/T/.test(String(iso)) ? iso : `${iso}T00:00:00Z`);
    if (Number.isNaN(d.getTime())) return String(iso);
    try {
      return new Intl.DateTimeFormat(locale(), { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' }).format(d);
    } catch {
      return String(iso);
    }
  }

  // ----- the texts in the page -----
  // A message may hold <strong>, <em> and <code> (built as elements, never parsed as HTML), and
  // {name} placeholders: an element of the page marked data-slot="name" (a file name, the server
  // address: kept as it is, only moved), or a value from data-i18n-args.
  const TOKEN = /<(\/?)(strong|em|code)>|\{([\w-]+)\}/g;
  const slotCache = new WeakMap();

  function slotsOf(el) {
    let slots = slotCache.get(el);
    if (!slots) {
      slots = Object.create(null);
      el.querySelectorAll('[data-slot]').forEach((slot) => {
        if (slot.parentElement.closest('[data-i18n]') === el) slots[slot.dataset.slot] = slot;
      });
      slotCache.set(el, slots);
    }
    return slots;
  }

  function render(el, text, vars) {
    if (!/[<{]/.test(text)) {
      el.textContent = text;
      return;
    }
    const slots = slotsOf(el);
    const frag = document.createDocumentFragment();
    const open = [frag];
    const add = (node) => open[open.length - 1].appendChild(node);
    const addText = (s) => { if (s) add(document.createTextNode(s)); };
    let last = 0;
    TOKEN.lastIndex = 0;
    for (let m = TOKEN.exec(text); m; m = TOKEN.exec(text)) {
      addText(text.slice(last, m.index));
      last = TOKEN.lastIndex;
      if (m[2]) {
        if (!m[1]) {
          const tag = document.createElement(m[2]);
          add(tag);
          open.push(tag);
        } else if (open.length > 1) {
          open.pop();
        }
      } else if (slots[m[3]]) {
        add(slots[m[3]]);
      } else if (vars && has(vars, m[3])) {
        addText(String(vars[m[3]]));
      } else {
        addText(m[0]);
      }
    }
    addText(text.slice(last));
    el.textContent = '';
    el.appendChild(frag);
  }

  function argsOf(el) {
    const json = el.getAttribute('data-i18n-args');
    if (!json) return null;
    try { return JSON.parse(json); } catch { return null; }
  }

  const ATTRIBUTES = [['i18nAlt', 'alt'], ['i18nTitle', 'title'], ['i18nAriaLabel', 'aria-label'], ['i18nContent', 'content']];

  function applyPage() {
    document.querySelectorAll('[data-i18n]').forEach((el) => {
      const text = raw(el.dataset.i18n);
      if (typeof text !== 'string') return;
      if (el.tagName === 'TITLE') document.title = fill(text, argsOf(el));
      else render(el, text, argsOf(el));
    });
    document.querySelectorAll('[data-i18n-alt], [data-i18n-title], [data-i18n-aria-label], [data-i18n-content]').forEach((el) => {
      for (const [prop, attribute] of ATTRIBUTES) {
        const key = el.dataset[prop];
        const text = key ? raw(key) : undefined;
        if (typeof text === 'string') el.setAttribute(attribute, fill(text, argsOf(el)));
      }
    });
    root.lang = lang;
    updateMenu();
    updateCanonical();
  }

  // ?lang= pages are the hreflang alternates: each is its own canonical page. The link is made
  // here and not written in index.html: one there would name the English page as canonical for
  // every ?lang= page until this script changed it, and search engines then drop the page's
  // hreflang. The address comes from the x-default alternate.
  function updateCanonical() {
    let link = document.querySelector('link[rel="canonical"]');
    if (!link) {
      const home = document.querySelector('link[rel="alternate"][hreflang="x-default"]');
      if (!home) return;
      link = document.createElement('link');
      link.rel = 'canonical';
      link.dataset.base = home.getAttribute('href').split('?')[0];
      document.head.appendChild(link);
    }
    if (!link.dataset.base) link.dataset.base = link.getAttribute('href').split('?')[0];
    const chosen = fromAddress();
    link.setAttribute('href', chosen ? `${link.dataset.base}?lang=${chosen}` : link.dataset.base);
  }

  // ----- the language menu -----
  function updateMenu() {
    const menu = document.getElementById('lang');
    if (!menu) return;
    const current = info(lang);
    const label = t('lang.button', { language: current.name });
    if (label) menu.querySelector('summary').setAttribute('aria-label', label);
    const name = menu.querySelector('.lang-name');
    if (name) name.textContent = current.short || current.name;
    const code = menu.querySelector('.lang-code');
    if (code) code.textContent = current.code.split('-')[0].toUpperCase();
    menu.querySelectorAll('a[hreflang]').forEach((a) => {
      if (a.getAttribute('hreflang') === lang) a.setAttribute('aria-current', 'true');
      else a.removeAttribute('aria-current');
    });
  }

  function wireMenu() {
    const menu = document.getElementById('lang');
    if (!menu) return;
    const summary = menu.querySelector('summary');
    const items = () => Array.from(menu.querySelectorAll('a[hreflang]'));
    const close = (refocus) => {
      menu.open = false;
      if (refocus) summary.focus();
    };

    // The links work on their own (a new tab, no JavaScript); a plain click switches in place.
    menu.addEventListener('click', (e) => {
      const a = e.target.closest('a[hreflang]');
      if (!a || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      const code = match(a.getAttribute('hreflang'));
      if (!code) return;
      e.preventDefault();
      close(true);
      choose(code);
    });

    menu.addEventListener('keydown', (e) => {
      const list = items();
      const at = list.indexOf(document.activeElement);
      if (e.key === 'Escape' && menu.open) {
        e.preventDefault();
        close(true);
        return;
      }
      if (!['ArrowDown', 'ArrowUp', 'Home', 'End'].includes(e.key)) return;
      if (!menu.open && (e.key === 'Home' || e.key === 'End')) return; // the page's own keys
      e.preventDefault();
      if (!menu.open) menu.open = true;
      let next;
      if (e.key === 'Home') next = list[0];
      else if (e.key === 'End') next = list[list.length - 1];
      else if (at < 0) next = menu.querySelector('a[aria-current]') || list[0];
      else next = list[(at + (e.key === 'ArrowDown' ? 1 : list.length - 1)) % list.length];
      next.focus();
    });

    document.addEventListener('click', (e) => {
      if (menu.open && !menu.contains(e.target)) close(false);
    });
    menu.addEventListener('focusout', (e) => {
      if (menu.open && e.relatedTarget && !menu.contains(e.relatedTarget)) close(false);
    });
  }

  // ----- switching -----
  const listeners = [];
  let ready = false;
  let ticket = 0;

  function notify() {
    listeners.forEach((fn) => {
      try { fn(lang); } catch (err) { console.error(err); }
    });
  }

  // A pick from the menu: switch in place, remember it, and put it in the address to share.
  async function choose(code) {
    const mine = ++ticket;
    await Promise.all([load(SOURCE), load(code)]);
    if (mine !== ticket) return;
    lang = code;
    remember(code);
    try {
      const url = new URL(location.href);
      url.searchParams.set('lang', code);
      history.replaceState(history.state, '', url);
    } catch { /* keep the address */ }
    applyPage();
    notify();
  }

  let held = null;
  function release() {
    clearTimeout(held);
    root.classList.remove('i18n-pending');
  }
  if (lang !== SOURCE) {
    root.classList.add('i18n-pending');
    held = setTimeout(release, HOLD_MS);
  }

  const parsed = new Promise((resolve) => {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', resolve, { once: true });
    else resolve();
  });
  parsed.then(wireMenu);
  const first = ticket;
  Promise.all([load(SOURCE), lang === SOURCE ? null : load(lang), parsed]).then(() => {
    if (ticket === first) applyPage(); // else a pick from the menu got there first
    ready = true;
    release();
    notify();
  });

  window.SpaceCorpsI18n = {
    languages: LANGUAGES,
    get lang() { return lang; },
    get ready() { return ready; },
    t,
    plural,
    number,
    size,
    sizeTitle,
    date,
    choose: (code) => { const c = match(code); return c ? choose(c) : Promise.resolve(); },
    // fn(lang) once the texts are in, and again after every switch.
    subscribe(fn) {
      listeners.push(fn);
      if (ready) fn(lang);
    },
  };
})();
