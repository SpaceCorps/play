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
| `patchnotes.html`, `patchnotes.md`, `patchnotes.json` | every release's patch notes, newest first; the latest one is also on the main page (`index.html`, `index.md`). Written at release time by the game repository's `scripts/release/patchnotes.py`, between `<!-- patchnotes:… -->` markers: edit the notes there (`docs/releases/v<version>.md`), not here |
| `img/` | screenshots taken headless from the game (WebP) and icons |
| `wiki.html`, `wiki.json`, `wiki/` | the game's own wiki: every article as HTML in the page and the catalog, as Markdown in `wiki/<NN-Category>/`, its pictures in `wiki/img/`, and the languages it is translated into (`wiki/i18n/<language>.json`, `wiki/<language>/`; an article a language lacks shows in English). Rebuilt at every release by `scripts/build-wiki.py` from the game's `assets/wiki` (the game repository's `scripts/marketing/sitedocs.py` runs it): edit the articles in the game, not here. `python3 scripts/test-build-wiki.py` tests the script |
| `llms.txt`, `llms-full.txt`, `index.md` | what agents and crawlers read: the blocks between `<!-- release:NAME -->` markers (`# release:front` in `index.md`'s front matter) are written at release time by `sitedocs.py` (packages, checksums, languages, the wiki's list); the text around them is hand-written |

Found a problem with a download? [Open an issue](https://github.com/SpaceCorps/play/issues).
