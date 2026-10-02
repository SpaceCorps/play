#!/usr/bin/env python3
"""Tests of scripts/build-wiki.py on a small wiki of its own (no game checkout needed):

    python3 scripts/test-build-wiki.py

The Markdown as the game reads it (anchors, comments, lists, formulas, callouts, pictures), the
links between articles and their checks, the version and date of release.json, the pictures
copied, the translations (fallback, stale, names from the locales) and wiki/ owned by the build.
Python 3.9, standard library only.
"""

import importlib.util
import io
import json
import os
import re
import shutil
import struct
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("build_wiki", os.path.join(HERE, "build-wiki.py"))
bw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bw)

PNG = b"\x89PNG\r\n\x1a\n" + struct.pack(">I", 13) + b"IHDR" + struct.pack(">II", 900, 578) + b"\x08\x02\x00\x00\x00" + b"\x00" * 16
JPEG = b"\xff\xd8\xff\xe0" + struct.pack(">H", 16) + b"JFIF\x00" + b"\x00" * 9 + b"\xff\xc0" + struct.pack(">H", 17) + b"\x08" + struct.pack(">HH", 300, 400) + b"\x03" + b"\x00" * 9 + b"\xff\xd9"

GETTING_STARTED = """# Getting Started in SpaceCorps

Welcome, *pilot*. See [Protos](/wiki/02-Ships/Protos.md#lore), [travel](/wiki/01-General/Spacemap%20Travel.md)
and [the stats](#first-steps).

## First steps

1. Fly.
2. Shoot.
   - with lasers
   - with rockets
3. Loot.

## Pilot's Guide (Part 2)

Escaped \\*stars\\* stay.
"""

SPACEMAP = """# Spacemap Travel

```spacemap
```

> [!NOTE]
> Jumps cost nothing.

\\[\\text{Speed} = a \\times b\\]
"""

PROTOS = """# Protos

The starter ship.

## Stats

| Stat | Value |
| :--- | ---: |
| HP | 8,000 |

## Lore

Old.

<!-- quests:begin -->
<!-- Generated: don't edit by hand. -->
### Level 1: Flight School

Generated text.
<!-- quests:end -->

![Level 1](../../skylab/wiki/level-01.png)
![Level 2](../../skylab/wiki/level-02.jpg)

![Gone](../../skylab/wiki/missing.jpg)
"""

DRONES_MECH = "# Drone Mechanics\n\nSee [the items](/wiki/05-Items/Drones.md) and [nothing](/wiki/05-Items/Nope.md) and [no heading](/wiki/02-Ships/Protos.md#nope).\n"
DRONES_ITEMS = "# Drones\n\nItems.\n"


class WikiTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="test-build-wiki.")
        self.game = os.path.join(self.tmp, "game")
        self.site = os.path.join(self.tmp, "site")
        self.write("game/assets/wiki/01-General/Getting-Started.md", GETTING_STARTED)
        self.write("game/assets/wiki/01-General/Spacemap Travel.md", SPACEMAP)
        self.write("game/assets/wiki/02-Ships/Protos.md", PROTOS)
        self.write("game/assets/wiki/03-Mechanics/Drones.md", DRONES_MECH)
        self.write("game/assets/wiki/05-Items/Drones.md", DRONES_ITEMS)
        self.write("game/assets/skylab/wiki/level-01.png", PNG)
        self.write("game/assets/skylab/wiki/level-02.jpg", JPEG)
        self.write("site/release.json", json.dumps({"version": "0.4.6", "date": "2026-10-01", "assets": []}))

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def write(self, rel, data):
        path = os.path.join(self.tmp, *rel.split("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(data if isinstance(data, bytes) else data.encode("utf-8"))

    def build(self, *extra):
        bw.WARNINGS.clear()
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = bw.main([os.path.join(self.game, "assets", "wiki"), "--out", self.site] + list(extra))
        self.out = out.getvalue() + err.getvalue()
        return code

    def read(self, *parts):
        with open(os.path.join(self.site, *parts), encoding="utf-8") as f:
            return f.read()

    def catalog(self, rel="wiki.json"):
        with open(os.path.join(self.site, rel), encoding="utf-8") as f:
            return json.load(f)

    def test_version_date_and_articles(self):
        self.assertEqual(self.build(), 0, self.out)
        c = self.catalog()
        self.assertEqual((c["version"], c["date"]), ("0.4.6", "2026-10-01"))
        self.assertEqual(len(c["articles"]), 5)
        self.assertEqual([x["dir"] for x in c["categories"]], ["01-General", "02-Ships", "03-Mechanics", "05-Items"])
        # Two articles named Drones: their category tells them apart (the site's addresses so far).
        self.assertIn("mechanics-drones", c["articles"])
        self.assertIn("items-drones", c["articles"])
        self.assertEqual(c["articles"]["getting-started"]["title"], "Getting Started in SpaceCorps")
        self.assertEqual(c["articles"]["getting-started"]["listTitle"], "Getting Started")
        page = self.read("wiki.html")
        self.assertIn('"version": "0.4.6"', page)
        self.assertIn('"dateModified": "2026-10-01"', page)
        self.assertIn(">v0.4.6</span>", page)
        self.assertNotRegex(page, r"%%[A-Z_]+%%")
        data = re.search(r'<script type="application/json" id="wiki-data">(.*?)</script>', page, re.S).group(1)
        self.assertNotIn("<", data)
        self.assertEqual(json.loads(data)["default"], "getting-started")

    def test_no_release_json_fails(self):
        os.remove(os.path.join(self.site, "release.json"))
        self.assertEqual(self.build(), 1)
        self.assertIn("release.json", self.out)

    def test_a_wiki_folder_that_is_not_there_fails(self):
        bw.WARNINGS.clear()
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            self.assertEqual(bw.main([os.path.join(self.tmp, "nowhere"), "--out", self.site]), 1)

    def test_markdown_as_the_game_reads_it(self):
        self.build()
        a = self.catalog()["articles"]
        gs = a["getting-started"]["html"]
        self.assertIn('<h2 id="first-steps">First steps</h2>', gs)
        # The game's anchor: every run of other characters one -, a trailing one kept.
        self.assertIn('<h2 id="pilot-s-guide-part-2-">', gs)
        self.assertIn('<ol><li value="1">Fly.</li><li value="2">Shoot.<ul><li>with lasers</li><li>with rockets</li></ul></li><li value="3">Loot.</li></ol>', gs)
        self.assertIn("<em>pilot</em>", gs)
        self.assertIn("Escaped *stars* stay.", gs)
        self.assertNotIn("<h1", gs)  # the title is shown above the article
        sm = a["spacemap-travel"]["html"]
        self.assertIn('class="wiki-spacemap"', sm)
        self.assertIn('<blockquote class="wiki-callout wiki-callout-note"><p class="wiki-callout-title">Note</p><p>Jumps cost nothing.</p></blockquote>', sm)
        self.assertIn('<p class="wiki-math">Speed = a × b</p>', sm)
        p = a["protos"]["html"]
        self.assertNotIn("quests:begin", p)
        self.assertNotIn("don't edit", p)
        self.assertIn('<h3 id="level-1-flight-school">Level 1: Flight School</h3>', p)
        self.assertIn("<thead><tr><th>Stat</th><th>Value</th></tr></thead><tbody><tr><td>HP</td><td>8,000</td></tr>", p)
        self.assertEqual([t["anchor"] for t in a["protos"]["toc"]], ["stats", "lore", "level-1-flight-school"])

    def test_links_between_articles(self):
        self.build()
        a = self.catalog()["articles"]
        gs = a["getting-started"]["html"]
        self.assertIn('<a href="?article=protos#lore" class="wiki-link" data-article="protos" data-anchor="lore">Protos</a>', gs)
        self.assertIn('data-article="spacemap-travel">travel</a>', gs)
        self.assertIn('<a href="#first-steps">the stats</a>', gs)
        self.assertIn('data-article="items-drones">the items</a>', a["mechanics-drones"]["html"])
        self.assertIn("warning: wiki/03-Mechanics/Drones.md: the link /wiki/05-Items/Nope.md lands on no article", self.out)
        self.assertIn("warning: wiki/03-Mechanics/Drones.md: the link /wiki/02-Ships/Protos.md#nope lands on no heading of protos", self.out)
        self.assertEqual(len(bw.WARNINGS), 3, bw.WARNINGS)  # the two above and the missing picture

    def test_pictures(self):
        self.build()
        img = os.path.join(self.site, "wiki", "img", "skylab", "wiki")
        self.assertEqual(sorted(os.listdir(img)), ["level-01.png", "level-02.jpg"])
        p = self.catalog()["articles"]["protos"]
        self.assertIn('<div class="wiki-gallery"><figure class="wiki-figure"><a href="wiki/img/skylab/wiki/level-01.png"', p["html"])
        self.assertIn('alt="Level 1" width="900" height="578"', p["html"])
        self.assertIn('alt="Level 2" width="400" height="300"', p["html"])
        self.assertIn('<figure class="wiki-figure wiki-figure-missing"><figcaption>Gone</figcaption></figure>', p["html"])
        self.assertIn("warning: wiki/02-Ships/Protos.md: the picture skylab/wiki/missing.jpg is not in", self.out)
        mirror = self.read("wiki", "02-Ships", "Protos.md")
        self.assertIn("![Level 1](../img/skylab/wiki/level-01.png)", mirror)
        self.assertIn("![Gone](../../skylab/wiki/missing.jpg)", mirror)
        self.assertEqual(p["markdown"], mirror)

    def test_wiki_folder_is_the_builds(self):
        self.write("site/wiki/09-Old/Old.md", "# Old\n")
        self.write("site/wiki/img/old.png", PNG)
        self.build()
        self.assertFalse(os.path.exists(os.path.join(self.site, "wiki", "09-Old")))
        self.assertFalse(os.path.exists(os.path.join(self.site, "wiki", "img", "old.png")))
        self.assertTrue(os.path.isfile(os.path.join(self.site, "wiki", "01-General", "Spacemap Travel.md")))

    def translate(self):
        english = PROTOS
        fresh = bw.source_hash(english)
        self.write("game/assets/wiki-i18n/de/02-Ships/Protos.md",
                   "<!-- wiki-i18n source: %s -->\n<!-- wiki-i18n title: Protos DE -->\n# Protos {#protos}\n\nDas Startschiff. "
                   "Siehe [Start](/wiki/01-General/Getting-Started.md#first-steps).\n\n## Werte {#stats}\n\n## Hintergrund {#lore}\n\n"
                   "<!-- quests:begin -->\n<!-- quests:end -->\n\n![Stufe 1](../../skylab/wiki/level-01.png)\n" % fresh)
        self.write("game/assets/wiki-i18n/de/01-General/Getting-Started.md",
                   "<!-- wiki-i18n source: 0000000000000000 -->\n<!-- wiki-i18n title: Erste Schritte -->\n# Erste Schritte {#getting-started-in-spacecorps}\n\n"
                   "## Los geht's {#first-steps}\n\n[Kaputt](/wiki/02-Ships/Protos.md#nirgends)\n")
        self.write("game/assets/wiki-i18n/de/09-Nope/Gone.md", "# Gone\n")
        self.write("game/assets/wiki-i18n/de/generated.toml", "[common]\n")
        self.write("game/assets/wiki-i18n/sv/generated.toml", "[common]\n")
        self.write("game/assets/wiki-i18n/generated.toml", "[common]\n")
        self.write("game/client/locales/en/wiki.toml", '[page]\non-this-page = "On this page"\n[category]\ngeneral = "General"\n')
        self.write("game/client/locales/de/wiki.toml",
                   '[page]\non-this-page = "Auf dieser Seite"\n[category]\ngeneral = "Allgemein"\nships = ""\n'
                   '[translation]\nenglish-only = "Noch nicht \\u00FCbersetzt."\n[callout]\nnote = "Hinweis"\n')

    def test_translations(self):
        self.translate()
        self.assertEqual(self.build(), 0, self.out)
        c = self.catalog()
        self.assertEqual([(l["code"], l["articles"], l["stale"]) for l in c["languages"]], [("de", 2, 1)])
        self.assertIn("translations: de 2/5", self.out)
        de = self.catalog("wiki/i18n/de.json")
        self.assertEqual(list(de["articles"]), ["getting-started", "protos"])
        p = de["articles"]["protos"]
        self.assertFalse(p["stale"])
        self.assertTrue(de["articles"]["getting-started"]["stale"])
        self.assertEqual((p["title"], p["listTitle"], p["anchor"]), ("Protos", "Protos DE", "protos"))
        self.assertIn('<h2 id="stats">Werte</h2>', p["html"])
        self.assertIn('data-article="getting-started" data-anchor="first-steps">Start</a>', p["html"])
        self.assertIn('src="wiki/img/skylab/wiki/level-01.png"', p["html"])
        self.assertEqual(de["categories"]["general"], "Allgemein")
        self.assertEqual(de["categories"]["ships"], "Ships")  # empty in the locale: English
        self.assertEqual(de["ui"]["onThisPage"], "Auf dieser Seite")
        self.assertEqual(de["ui"]["englishOnly"], "Noch nicht übersetzt.")
        self.assertEqual(de["ui"]["back"], "Back to the translation")
        mirror = self.read("wiki", "de", "02-Ships", "Protos.md")
        self.assertIn("![Stufe 1](../../img/skylab/wiki/level-01.png)", mirror)
        self.assertIn("warning: wiki-i18n/de/09-Nope/Gone.md: no English article 09-Nope/Gone.md: left out", self.out)
        self.assertIn("warning: wiki-i18n/de/01-General/Getting-Started.md: the link /wiki/02-Ships/Protos.md#nirgends lands on no heading of protos", self.out)
        self.assertFalse(os.path.exists(os.path.join(self.site, "wiki", "i18n", "sv.json")))
        page = self.read("wiki.html")
        self.assertIn('hreflang="de"', page)
        self.assertNotIn('hreflang="hu"', page)  # neither the page's language nor the wiki's

    def test_a_wiki_only_language_is_in_the_menu(self):
        self.translate()
        os.rename(os.path.join(self.game, "assets", "wiki-i18n", "de"), os.path.join(self.game, "assets", "wiki-i18n", "hu"))
        self.build()
        page = self.read("wiki.html")
        self.assertIn('<a href="?lang=hu" hreflang="hu" lang="hu">Magyar', page)

    def test_no_i18n(self):
        self.translate()
        self.build("--no-i18n")
        self.assertEqual(self.catalog()["languages"], [])
        self.assertFalse(os.path.exists(os.path.join(self.site, "wiki", "de")))

    def test_source_hash_blanks_the_generated_blocks(self):
        a = "# T\n\n<!-- x:begin -->\none\n<!-- x:end -->\n"
        b = "# T\r\n\r\n<!-- x:begin -->\r\ntwo\r\nthree\r\n<!-- x:end -->\r\n"
        self.assertEqual(bw.source_hash(a), bw.source_hash(b))
        self.assertNotEqual(bw.source_hash(a), bw.source_hash(a.replace("# T", "# U")))


if __name__ == "__main__":
    unittest.main(verbosity=1)
