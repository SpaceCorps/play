# The page's languages

The download page speaks the game's ten languages: `en` (source), `de`, `es`, `fr`, `pt-BR`,
`sv`, `ru`, `ja`, `ko`, `zh-CN`. One file per language, `<code>.json`, key → text.

- **English** lives twice: in `index.html` (what crawlers and visitors without JavaScript read)
  and in `en.json` (the fallback for a key a translation lacks, and the texts `app.js` writes).
  `python3 i18n/check.py` fails if the two differ.
- **Which language:** `?lang=de` in the address, else the visitor's last pick from the menu
  (`localStorage`), else the browser's languages (`de-AT` → `de`, `pt-PT` → `pt-BR`, `zh-TW` →
  `zh-CN`), else English. `i18n.js` has the list, in the game's picker order.
- **In the page:** `data-i18n="key"` replaces an element's content; `data-i18n-alt`, `-title`,
  `-aria-label` and `-content` set that attribute. `{name}` in a text is either a value from
  `data-i18n-args` or a child element marked `data-slot="name"` (a file name, a command, the
  server address), which stays as it is and moves where the sentence puts it.
- **Release data stays out of the texts:** versions, sizes, checksums and file names come from
  `release.json` and the HTML; the texts only say where they go (`{version}`, `{format}`).
  Sizes, counts and dates are formatted per language with `Intl` (`12 Mo`, `25. September 2026`,
  `2026年9月25日`).

## Adding or changing a text

1. Change the English in `index.html` (or `app.js`) and `en.json` together; a note for
   translators goes in an `"@key"` entry next to it.
2. Translate it in all nine other files (the check wants every key in every language).
3. `python3 i18n/check.py`.

## Translating

The rules are the game's (`docs/LOCALIZATION.md`, Translator guide), so the page and the game
read the same:

- Reuse the game's wording where it has one (`landing.card.pitch` is the hero's first sentence,
  `landing.server.change` the help's *Change server*).
- Keep `{placeholders}` as they are; move them where your grammar wants them.
- Only `<strong>`, `<em>` and `<code>`, balanced, no attributes.
- Plurals are objects of CLDR forms: `{"one": "{n} pilot online", "other": "{n} pilots online"}`;
  Russian needs `one`, `few`, `many`, `other`; Japanese, Korean and Chinese only `other`.
- Glossary names are never translated: SpaceCorps, Thulium, Skylab, Chrono-Gate, P.E.T., ship,
  alien and company names (Wraith, Seeker, Mars Colonization), Mission Control, Discord. The
  game's fixed translations (Clan → 战队, Season → Saison, Galaxy Gates → Galaxietore) apply.
- Bold and italic words in the first-launch help are what macOS and Windows show: use the names
  of your language's system (*Programme*, *Dennoch öffnen*, *Weitere Informationen*).
- French: a no-break space (` `) before `:` `;` `?` `!` and inside `« »`.
- Japanese and Chinese: full-width punctuation, a space between Latin words and CJK text, none
  between a digit and its counter (`4文字`, `64ビット`). Korean: no particle right after a
  `{placeholder}`.
