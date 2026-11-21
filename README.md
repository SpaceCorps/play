# SpaceCorps 2027: downloads

The download page of **SpaceCorps 2027**, a space MMO for macOS, Windows and Linux:
**https://play.spacecorps.tech/**

Get the game from the page, or straight from the [latest release](https://github.com/SpaceCorps/play/releases/latest).

This repository holds only the static site (GitHub Pages, `main` branch, no build step) and the
release packages. The game itself is developed in a private repository; releases are built and
published from there with `scripts/release-local.sh` and `scripts/publish-release.sh`, which
also update `release.json` (version, sizes and SHA-256 of every package) that the page reads.

| file | |
|---|---|
| `index.html`, `style.css`, `app.js` | the page: no frameworks, no trackers, no cookies |
| `i18n.js`, `i18n/<language>.json` | the game's ten languages: `?lang=de`, the menu, else the browser's; see [i18n/README.md](i18n/README.md), check with `python3 i18n/check.py` |
| `premium/index.html`, `premium.js`, `premium.css`, `terms/` | the Premium page (sign in with the game account, buy Premium through Stripe Checkout) and its terms of sale; no build step, no cookies. `scripts/mock-premium-api.py` is a local stand-in for the game server's payment routes to try it, and `scripts/serve-premium-page.py` serves the page for it (the page's Content-Security-Policy lets it talk to the real game server only; that script widens it to this machine's mock): their docstrings have the commands |
| `status/` | The Server status page: pilots online per server over time (Today, Week, Month, 3 months, Year, All time) and, once the game reports it (0.5.11), by platform (Steam, desktop, iOS, Android, web, unknown) for all servers or one: the "By platform" switch only appears when the API has platform history (`platform_since`). A plain-SVG chart in `status.js` with its helpers in `status-chart.js` (tests: `node --test scripts/`). The numbers come from the status service, `https://spacecorps.tech/api/status/series` (read-only, CORS `*`; the recorder is in the `spacecorps.github.io` repository, folder `status/`); the page's CSP allows only that address. No build step, no cookies. |
| `privacy/`, `terms/` | the Privacy Policy and the Terms of Use of the game: hand-written, English only, no build step. Other places link their addresses and the id `deleting-your-account` of the privacy page, so keep them. The Premium terms of sale are `premium/terms/` |
| `release.json` | the latest release's packages, written at release time |
| `web.json` | the web version's address (`url`), opened by the hero's *Play in browser* button; `app.js` falls back to `https://web.spacecorps.xyz/`. Set it by hand when the web game is hosted. Merge the browser button to `main` only after `https://web.spacecorps.xyz/health` answers, or every visitor gets a button that opens a DNS error |
| `patchnotes.html`, `patchnotes.md`, `patchnotes.json` | every release's patch notes, newest first; the latest one is also on the main page (`index.html`, `index.md`). Written at release time by the game repository's `scripts/release/patchnotes.py`, between `<!-- patchnotes:… -->` markers: edit the notes there (`docs/releases/v<version>.md`), not here |
| `img/` | screenshots taken headless from the game (WebP) and icons |
| `wiki.html`, `wiki.json`, `wiki/` | the game's own wiki: every article as HTML in the page and the catalog, as Markdown in `wiki/<NN-Category>/`, its pictures in `wiki/img/`, and the languages it is translated into (`wiki/i18n/<language>.json`, `wiki/<language>/`; an article a language lacks shows in English). Rebuilt at every release by `scripts/build-wiki.py` from the game's `assets/wiki` (the game repository's `scripts/marketing/sitedocs.py` runs it): edit the articles in the game, not here. `python3 scripts/test-build-wiki.py` tests the script |
| `llms.txt`, `llms-full.txt`, `index.md` | what agents and crawlers read: the blocks between `<!-- release:NAME -->` markers (`# release:front` in `index.md`'s front matter) are written at release time by `sitedocs.py` (packages, checksums, languages, the wiki's list); the text around them is hand-written |

Found a problem with a download? [Open an issue](https://github.com/SpaceCorps/play/issues).
