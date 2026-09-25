# SpaceCorps 2027: downloads

The download page of **SpaceCorps 2027**, a space MMO for macOS, Windows and Linux:
**https://spacecorps.github.io/play/**

Get the game from the page, or straight from the [latest release](https://github.com/SpaceCorps/play/releases/latest).

This repository holds only the static site (GitHub Pages, `main` branch, no build step) and the
release packages. The game itself is developed in a private repository; releases are built and
published from there with `scripts/release-local.sh` and `scripts/publish-release.sh`, which
also update `release.json` (version, sizes and SHA-256 of every package) that the page reads.

| file | |
|---|---|
| `index.html`, `style.css`, `app.js` | the page: no frameworks, no trackers, no cookies |
| `i18n.js`, `i18n/<language>.json` | the game's ten languages: `?lang=de`, the menu, else the browser's; see [i18n/README.md](i18n/README.md), check with `python3 i18n/check.py` |
| `release.json` | the latest release's packages, written at release time |
| `img/` | screenshots taken headless from the game (WebP) and icons |

Found a problem with a download? [Open an issue](https://github.com/SpaceCorps/play/issues).
