#!/usr/bin/env python3
"""The SpaceCorps 2027 wiki on the web, built from the game's own wiki.

Reads the game's articles (assets/wiki/<NN-Category>/<Title>.md), the pictures they show
(`![caption](path)` on a line of its own, the path relative to the article as on GitHub and in
the game: ../../skylab/wiki/level-01.jpg is assets/skylab/wiki/level-01.jpg) and, when there are
any, their translations (assets/wiki-i18n/<language>/<NN-Category>/<Title>.md, the same folder
and file name as the English article), and writes, in the site (this script's parent folder):

  wiki.json                  the English catalog: every article's HTML, outline and Markdown, the
                             version and date of the site's release.json, the languages the wiki
                             is translated into
  wiki.html                  the page: the English articles in it, a language's loaded on demand
  wiki/<NN-Category>/*.md    the English articles as Markdown (their pictures in wiki/img/)
  wiki/img/<path>            the pictures, at their path under the game's assets/
  wiki/i18n/<language>.json  a language's catalog: its translated articles, category names and
                             notes (an article it lacks shows in English, with a note)
  wiki/<language>/<NN-Category>/*.md   the translated articles as Markdown

Everything else under wiki/ is removed: the folder is the build's.

The game's release job runs this at every release (scripts/marketing/sitedocs.py in the game's
repository, on a copy of the site; see its docs/DEVELOPMENT.md, "The site's machine-readable
files"), so the wiki follows the game's. By hand, from the site, with release.json the release's:

    python3 scripts/build-wiki.py ../SpaceCorps2027/assets/wiki

  --i18n DIR     the translations (default: wiki-i18n next to the wiki folder, when it is there)
  --locales DIR  the game's client/locales: category names, notes and callout titles per language
                 (default: ../../client/locales from the wiki folder, when it is there)
  --assets DIR   the folder picture paths end up in (default: the wiki folder's parent)
  --no-i18n      English only

The Markdown is the game's subset (client/src/ui/pages/wiki/markdown.rs), read the same way:
headings with the game's anchors (or a translation's {#anchor}), paragraphs, nested lists,
tables, block quotes and [!NOTE] callouts, rules, fenced code (```spacemap is the game's live
galaxy map), one-line formulas, pictures (a run of them is a gallery), HTML comments hidden;
bold, italic, code, links and backslash escapes inline. Links between articles
(/wiki/05-Items/Lasers.md#anchor) open the article at that heading; a link or picture that lands
nowhere is a warning.

Exit status 0 built, 1 failed (no articles, no release.json, a folder that isn't there).
Python 3.9, standard library only.
"""

import argparse
import hashlib
import html
import json
import os
import re
import string
import struct
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
PLAY_ROOT = os.path.abspath(os.path.join(HERE, ".."))

# What the game's release job (scripts/marketing/sitedocs.py) may hand this script: 1 = the
# articles only, without their picture lines (the first version of this script); 2 = the game's
# wiki folder as it is, with --assets, --i18n and --locales.
SITEDOCS_INTERFACE = 2

CANDIDATE_DIRS = [
    os.path.join(PLAY_ROOT, "..", "SpaceCorps2027-release", "assets", "wiki"),
    os.path.join(PLAY_ROOT, "..", "SpaceCorps2027", "assets", "wiki"),
    os.path.join(PLAY_ROOT, "..", "..", "SpaceCorps2027-release", "assets", "wiki"),
    os.path.join(PLAY_ROOT, "..", "..", "SpaceCorps2027", "assets", "wiki"),
    os.path.expanduser("~/git/spacecorps/SpaceCorps2027-release/assets/wiki"),
    os.path.expanduser("~/git/spacecorps/SpaceCorps2027/assets/wiki"),
]

# The game's languages in its picker's order (client/src/i18n/languages.rs), with their own names.
GAME_LANGUAGES = [
    ("en", "English"), ("de", "Deutsch"), ("es", "Español"), ("fr", "Français"),
    ("it", "Italiano"), ("hu", "Magyar"), ("pt-BR", "Português (Brasil)"), ("sv", "Svenska"),
    ("ru", "Русский"), ("ja", "日本語"), ("ko", "한국어"), ("zh-CN", "简体中文"),
]
# The languages of the download page (i18n.js): the language menu offers these, and the wiki's
# own languages besides.
SITE_LANGUAGES = ["en", "de", "es", "fr", "pt-BR", "sv", "ru", "ja", "ko", "zh-CN"]
LANGUAGE_CODE = re.compile(r"[a-z]{2,3}(-[A-Za-z0-9]{2,8})*")

PICTURE_TYPES = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
PICTURE_DIR = "wiki/img"

# The page's own words in English: the game's wiki.* texts (client/locales/en/wiki.toml), used
# where --locales has none.
UI_KEYS = {
    "onThisPage": ("page", "on-this-page", "On this page"),
    "englishOnly": ("translation", "english-only", "This page is not translated yet, so it shows in English."),
    "stale": ("translation", "stale", "The English page has changed since this translation was made: some details may be out of date."),
    "readEnglish": ("translation", "read-english", "Read the English page"),
    "showingEnglish": ("translation", "showing-english", "You are reading the English page."),
    "back": ("translation", "back", "Back to the translation"),
}
CALLOUTS = {"NOTE": "Note", "TIP": "Tip", "IMPORTANT": "Important", "WARNING": "Warning", "CAUTION": "Caution"}

WARNINGS = []


def warn(text):
    WARNINGS.append(text)
    print("warning: %s" % text)


class BuildError(Exception):
    pass


# ----- names and anchors (the game's client/src/ui/pages/wiki/mod.rs and markdown.rs)


def slugify(text):
    """The site's article ids ("Black-Hole" -> "black-hole"): stable addresses, ?article=<id>."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[-\s]+", "-", text)


def category_info(dir_name):
    """"01-General" -> (1, "General", "general"): the order, the name, the id."""
    digits = "".join(c for c in dir_name if c.isdigit())
    order = int(digits) if digits else 99
    name = dir_name[len(digits):].lstrip("-") if digits else dir_name
    name = name.replace("-", " ")
    return order, name, slugify(name)


def file_slug(filename):
    stem = filename[:-3] if filename.endswith(".md") else filename
    return slugify(re.sub(r"^\d+-", "", stem))


def title_of(filename):
    """"Getting-Started.md" -> "Getting Started": the article's name in the game's list."""
    stem = filename[:-3] if filename.endswith(".md") else filename
    m = re.match(r"\d+-", stem)
    if m:
        stem = stem[m.end():]
    return stem.replace("-", " ").strip()


def game_slug(text):
    """A heading's anchor, as the game makes it: lowercase, every run of other characters than
    letters, digits and _ one -."""
    out = []
    gap = False
    for c in plain(text).lower():
        if c.isalnum() or c == "_":
            out.append(c)
            gap = False
        elif not gap:
            out.append("-")
            gap = True
    return "".join(out)


def heading_anchor(text):
    """(text, anchor) of a heading: a translation's ends with the English anchor, {#anchor}."""
    t = text.rstrip()
    m = re.search(r"(^|[ \t])\{#([^\s{}]+)\}$", t)
    if m:
        return t[:m.start()].strip(), m.group(2)
    return text.strip(), game_slug(text)


# ----- inline Markdown


def spans(text):
    """The game's inline parser: [("text", text, bold, italic, code)] and [("link", text, url)]."""
    out = []
    buf = []
    state = {"bold": False, "italic": False}
    n = len(text)

    def flush():
        if buf:
            out.append(("text", "".join(buf), state["bold"], state["italic"], False))
            del buf[:]

    def word(c):
        return c is not None and c.isalnum()

    i = 0
    while i < n:
        c = text[i]
        nxt = text[i + 1] if i + 1 < n else None
        if c == "\\" and nxt is not None and nxt in string.punctuation:
            buf.append(nxt)
            i += 2
            continue
        if c == "`":
            end = text.find("`", i + 1)
            if end >= 0:
                flush()
                out.append(("text", text[i + 1:end], state["bold"], state["italic"], True))
                i = end + 1
                continue
        elif c in "*_" and nxt == c:
            flush()
            state["bold"] = not state["bold"]
            i += 2
            continue
        elif c in "*_":
            prev = text[i - 1] if i > 0 else None
            italic = state["italic"]
            opens = not italic and nxt is not None and not nxt.isspace() and (c == "*" or not word(prev))
            closes = italic and prev is not None and not prev.isspace() and (c == "*" or not word(nxt))
            if opens or closes:
                flush()
                state["italic"] = not italic
                i += 1
                continue
        elif c == "[":
            close = text.find("]", i + 1)
            if close >= 0 and close + 1 < n and text[close + 1] == "(":
                end = text.find(")", close + 2)
                if end >= 0:
                    flush()
                    out.append(("link", plain(text[i + 1:close]), text[close + 2:end].strip()))
                    i = end + 1
                    continue
        buf.append(c)
        i += 1
    flush()
    return out


def plain(text):
    """Inline text without its Markdown (outlines, titles)."""
    return "".join(s[1] for s in spans(text))


def esc(text):
    """Text for HTML, also inside a "double-quoted" attribute (an apostrophe stays as it is)."""
    return html.escape(text, quote=True).replace("&#x27;", "'")


# ----- blocks


def split_lines(text):
    """Rust's str::lines(): split at \\n, a \\r before it dropped, no last empty line."""
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    return [l[:-1] if l.endswith("\r") else l for l in lines]


def heading(line):
    hashes = len(line) - len(line.lstrip("#"))
    if not 1 <= hashes <= 6:
        return None
    rest = line[hashes:]
    if not rest.startswith((" ", "\t")):
        return None
    return hashes, rest.strip()


def image_line(line):
    """(caption, path) of a line that is only a picture, ![caption](path)."""
    if not line.startswith("!["):
        return None
    rest = line[2:]
    close = rest.find("](")
    if close < 0 or not rest.endswith(")"):
        return None
    src = rest[close + 2:-1]
    if ")" in src or " " in src:
        return None
    return rest[:close].strip(), src.strip()


def display_math(line):
    for a, b in (("\\[", "\\]"), ("$$", "$$")):
        if line.startswith(a) and line.endswith(b) and len(line) >= len(a) + len(b):
            body = line[len(a):len(line) - len(b)]
            if body.strip():
                return body
    return None


MATH_SYMBOLS = {
    "times": "×", "cdot": "·", "div": "÷", "pm": "±", "le": "≤", "leq": "≤", "ge": "≥", "geq": "≥",
    "ne": "≠", "neq": "≠", "approx": "≈", "to": "→", "rightarrow": "→", "quad": "  ", "qquad": "  ",
}
MATH_DROPPED = {"left", "right", "displaystyle", "text", "textbf", "textit", "mathrm", "mathbf", "mathit", "operatorname"}


def math_text(tex):
    """The wiki's formulas as plain text (the game's markdown::math_text)."""
    out = []
    i = 0
    while i < len(tex):
        c = tex[i]
        i += 1
        if c == "\\":
            j = i
            while j < len(tex) and tex[j].isascii() and tex[j].isalpha():
                j += 1
            name = tex[i:j]
            i = j
            if not name:
                if i < len(tex):
                    nxt = tex[i]
                    i += 1
                    out.append(" " if nxt in ",; :" else nxt)
                continue
            if name in MATH_SYMBOLS:
                out.append(MATH_SYMBOLS[name])
            elif name not in MATH_DROPPED:
                out.append("\\" + name)
        elif c in "{}":
            continue
        else:
            out.append(c)
    return " ".join("".join(out).split())


def list_item(line):
    """(indent, marker or None, text) of a list item line."""
    indent = 0
    for c in line:
        if not c.isspace():
            break
        indent += 4 if c == "\t" else 1
    t = line.lstrip()
    for bullet in ("- ", "* ", "+ "):
        if t.startswith(bullet):
            return indent, None, t[len(bullet):].strip()
    m = re.match(r"([0-9]+)\. ", t)
    if m:
        return indent, m.group(1) + ".", t[m.end():].strip()
    return None


def is_rule(t):
    s = "".join(c for c in t if not c.isspace())
    return len(s) >= 3 and (set(s) == {"-"} or set(s) == {"*"} or set(s) == {"_"})


def table_cells(line):
    t = line.strip().lstrip("|").rstrip("|")
    return [c.strip() for c in t.split("|")]


def is_table_separator(cells):
    return bool(cells) and all(c and all(ch in "-: " for ch in c) for c in cells)


def parse(text):
    """The game's block parser (markdown::parse): a list of blocks, as tuples."""
    lines = split_lines(text)
    blocks = []
    para = []

    def flush_para():
        if para:
            blocks.append(("p", " ".join(l.strip() for l in para)))
            del para[:]

    i = 0
    while i < len(lines):
        line = lines[i]
        t = line.strip()
        if t.startswith("```"):
            flush_para()
            lang = t[3:].strip().lower()
            body = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                body.append(lines[i])
                i += 1
            i += 1
            blocks.append(("code", lang, "\n".join(body)))
            continue
        if t.startswith("<!--"):
            flush_para()
            while i < len(lines) and "-->" not in lines[i]:
                i += 1
            i += 1
            continue
        if not t:
            flush_para()
            i += 1
            continue
        h = heading(t)
        if h:
            flush_para()
            text_, anchor = heading_anchor(h[1])
            blocks.append(("h", h[0], text_, anchor))
            i += 1
            continue
        img = image_line(t)
        if img:
            flush_para()
            blocks.append(("img", plain(img[0]), img[1]))
            i += 1
            continue
        if t.startswith("|"):
            flush_para()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = table_cells(lines[i])
                if not is_table_separator(cells):
                    rows.append(cells)
                i += 1
            header = rows.pop(0) if rows else []
            blocks.append(("table", header, rows))
            continue
        body = display_math(t)
        if body is not None:
            flush_para()
            blocks.append(("math", math_text(body)))
            i += 1
            continue
        if is_rule(t):
            flush_para()
            blocks.append(("hr",))
            i += 1
            continue
        if t.startswith(">"):
            flush_para()
            paragraphs = []
            current = []
            callout = None
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                b = lines[i].lstrip()[1:].strip()
                m = re.fullmatch(r"\[!(.*)\]", b)
                if not paragraphs and not current and callout is None and m:
                    callout = m.group(1).upper()
                elif not b:
                    if current:
                        paragraphs.append(" ".join(current))
                        current = []
                else:
                    current.append(b)
                i += 1
            if current:
                paragraphs.append(" ".join(current))
            blocks.append(("quote", callout, paragraphs))
            continue
        if list_item(line):
            flush_para()
            items = []
            indents = []
            while i < len(lines):
                l = lines[i]
                if not l.strip():
                    if i + 1 < len(lines) and list_item(lines[i + 1]):
                        i += 1
                        continue
                    break
                it = list_item(l)
                if it:
                    indent, marker, text_ = it
                    if indents and indent <= indents[0] and items and (items[0][1] is not None) != (marker is not None):
                        break
                    while indents and indent < indents[-1]:
                        indents.pop()
                    if not indents or indent > indents[-1]:
                        indents.append(indent)
                    items.append([len(indents) - 1, marker, text_])
                elif l.startswith((" ", "\t")) and items:
                    items[-1][2] += " " + l.strip()
                else:
                    break
                i += 1
            blocks.append(("list", items))
            continue
        para.append(line)
        i += 1
    flush_para()
    return blocks


def outline(blocks):
    """Every heading as (level, plain text, anchor)."""
    return [(b[1], plain(b[2]), b[3]) for b in blocks if b[0] == "h"]


# ----- pictures


def resolve_picture(cat_dir, src):
    """The path under the assets of a picture written in assets/wiki/<cat_dir>/ (the game's
    images::resolve): None for a URL, an absolute path or one out of the assets."""
    if "://" in src or src.startswith("/") or src.startswith("data:"):
        return None
    parts = ["wiki", cat_dir]
    for p in urllib.parse.unquote(src).split("/"):
        if p in ("", "."):
            continue
        if p == "..":
            if not parts:
                return None
            parts.pop()
        else:
            parts.append(p)
    name = src.rsplit("/", 1)[-1]
    if not parts or name in ("", ".", ".."):
        return None
    return "/".join(parts)


def picture_size(data):
    """(width, height) of a PNG or JPEG, else None."""
    if data[:8] == b"\x89PNG\r\n\x1a\n" and data[12:16] == b"IHDR":
        return struct.unpack(">II", data[16:24])
    if data[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker == 0xFF:
                i += 1
                continue
            if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                i += 2
                continue
            length = struct.unpack(">H", data[i + 2:i + 4])[0]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                height, width = struct.unpack(">HH", data[i + 5:i + 9])
                return width, height
            i += 2 + length
    return None


class Pictures:
    """The pictures the articles show, copied to wiki/img/<path under the assets>."""

    def __init__(self, assets_dir):
        self.assets = assets_dir
        self.files = {}  # site path -> bytes
        self.sizes = {}
        self.missing = set()

    def get(self, asset_path, where):
        """The site path of the picture at asset_path (copied once), None when it isn't one."""
        site_path = "%s/%s" % (PICTURE_DIR, asset_path)
        if site_path in self.files:
            return site_path
        ext = os.path.splitext(asset_path)[1].lower()
        full = os.path.normpath(os.path.join(self.assets, *asset_path.split("/")))
        inside = os.path.commonpath([os.path.abspath(self.assets), os.path.abspath(full)]) == os.path.abspath(self.assets)
        if ext not in PICTURE_TYPES or not inside or not os.path.isfile(full):
            if asset_path not in self.missing:
                self.missing.add(asset_path)
                warn("%s: the picture %s is not in %s" % (where, asset_path, self.assets))
            return None
        with open(full, "rb") as f:
            data = f.read()
        self.files[site_path] = data
        self.sizes[site_path] = picture_size(data)
        return site_path


# ----- rendering


class Renderer:
    """Blocks to HTML for one article (cat_dir/filename), in one language."""

    def __init__(self, site, cat_dir, where, callouts):
        self.site = site  # the Site: links and pictures
        self.cat_dir = cat_dir
        self.where = where
        self.callouts = callouts
        self.links = []  # (slug or None, anchor or None, url) of every link, for the checks

    def link(self, text, url):
        label = esc(text)
        if url.startswith("#"):
            self.links.append(("", url[1:], url))
            return '<a href="#%s">%s</a>' % (esc(url[1:]), label)
        if "://" in url or url.startswith("mailto:"):
            return '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>' % (esc(url), label)
        slug, anchor = self.site.resolve(url)
        self.links.append((slug, anchor, url))
        if slug:
            href = "?article=%s" % slug + ("#" + anchor if anchor else "")
            return '<a href="%s" class="wiki-link" data-article="%s"%s>%s</a>' % (
                esc(href), esc(slug), ' data-anchor="%s"' % esc(anchor) if anchor else "", label)
        return '<a href="%s">%s</a>' % (esc(url), label)

    def inline(self, text):
        out = []
        for s in spans(text):
            if s[0] == "link":
                out.append(self.link(s[1], s[2]))
                continue
            _, t, bold, italic, code = s
            h = esc(t)
            if code:
                h = "<code>%s</code>" % h
            if italic:
                h = "<em>%s</em>" % h
            if bold:
                h = "<strong>%s</strong>" % h
            out.append(h)
        return "".join(out)

    def picture(self, alt, src):
        asset = resolve_picture(self.cat_dir, src)
        path = self.site.pictures.get(asset, self.where) if asset else None
        if asset is None:
            warn("%s: the picture %s is not under the assets" % (self.where, src))
        if not path:
            return '<figure class="wiki-figure wiki-figure-missing"><figcaption>%s</figcaption></figure>' % esc(alt)
        size = self.site.pictures.sizes.get(path)
        dims = ' width="%d" height="%d"' % size if size else ""
        return ('<figure class="wiki-figure"><a href="%s" target="_blank" rel="noopener">'
                '<img src="%s" alt="%s"%s loading="lazy" decoding="async"></a>'
                '<figcaption>%s</figcaption></figure>') % (esc(path), esc(path), esc(alt), dims, esc(alt))

    def list_html(self, items):
        out = []
        stack = []  # (depth, tag)
        for depth, marker, text in items:
            tag = "ol" if marker else "ul"
            while stack and stack[-1][0] > depth:
                out.append("</li></%s>" % stack.pop()[1])
            if stack and stack[-1][0] == depth:
                if stack[-1][1] != tag:
                    out.append("</li></%s><%s>" % (stack.pop()[1], tag))
                    stack.append((depth, tag))
                else:
                    out.append("</li>")
            else:
                out.append("<%s>" % tag)
                stack.append((depth, tag))
            value = ' value="%s"' % marker[:-1] if marker else ""
            out.append("<li%s>%s" % (value, self.inline(text)))
        while stack:
            out.append("</li></%s>" % stack.pop()[1])
        return "".join(out)

    def render(self, blocks):
        out = []
        gallery = []

        def end_gallery():
            if gallery:
                cls = "wiki-gallery" if len(gallery) > 1 else "wiki-gallery wiki-gallery-one"
                out.append('<div class="%s">%s</div>' % (cls, "".join(gallery)))
                del gallery[:]

        for b in blocks:
            kind = b[0]
            if kind == "img":
                gallery.append(self.picture(b[1], b[2]))
                continue
            end_gallery()
            if kind == "h":
                out.append('<h%d id="%s">%s</h%d>' % (b[1], esc(b[3]), self.inline(b[2]), b[1]))
            elif kind == "p":
                out.append("<p>%s</p>" % self.inline(b[1]))
            elif kind == "list":
                out.append(self.list_html(b[1]))
            elif kind == "table":
                head = "".join("<th>%s</th>" % self.inline(c) for c in b[1])
                rows = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % self.inline(c) for c in r) for r in b[2])
                out.append('<div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (head, rows))
            elif kind == "quote":
                callout, paragraphs = b[1], b[2]
                body = "".join("<p>%s</p>" % self.inline(p) for p in paragraphs)
                if callout:
                    title = self.callouts.get(callout, callout.title())
                    out.append('<blockquote class="wiki-callout wiki-callout-%s"><p class="wiki-callout-title">%s</p>%s</blockquote>' % (
                        esc(callout.lower()), esc(title), body))
                else:
                    out.append("<blockquote>%s</blockquote>" % body)
            elif kind == "code":
                if b[1] == "spacemap":
                    out.append('<div class="wiki-spacemap" role="note">The game draws its live galaxy map here: '
                               'every sector and the jumps between them (Spacemap Travel in the game\'s wiki).</div>')
                else:
                    out.append("<pre><code>%s</code></pre>" % esc(b[2]))
            elif kind == "math":
                out.append('<p class="wiki-math">%s</p>' % esc(b[1]))
            elif kind == "hr":
                out.append("<hr>")
        end_gallery()
        return "\n".join(out)


def mirror_text(text, cat_dir, depth, pictures):
    """The article as the site's Markdown mirror has it: picture paths pointing at wiki/img/
    (depth: the mirror file's folders below wiki/)."""
    out = []
    for line in text.split("\n"):
        img = image_line(line.strip().rstrip("\r"))
        if img:
            asset = resolve_picture(cat_dir, img[1])
            site_path = "%s/%s" % (PICTURE_DIR, asset) if asset else None
            if site_path and site_path in pictures.files:
                new = "../" * depth + site_path[len("wiki/"):]
                line = line.replace("](%s)" % img[1], "](%s)" % new, 1)
        out.append(line)
    return "\n".join(out)


# ----- translations


def blank_generated(page):
    """The page without what its generated blocks hold (the marker lines stay): what a
    translation's source hash is taken of (the game's translations::source_hash)."""
    out = []
    open_name = None
    for line in page.split("\n"):
        if line.endswith("\r"):
            line = line[:-1]
        m = re.fullmatch(r"<!-- ([a-z0-9-]+):(begin|start|end) -->", line.strip())
        if open_name is None:
            out.append(line)
            if m and m.group(2) != "end":
                open_name = m.group(1)
        elif m and m.group(2) == "end" and m.group(1) == open_name:
            out.append(line)
            open_name = None
    return "\n".join(out)


def source_hash(english):
    return hashlib.sha256(blank_generated(english).encode("utf-8")).hexdigest()[:16]


def translation_head(text):
    """(source hash, list title) of a translation's first two lines (None when missing)."""
    lines = text.split("\n")

    def value(i, name):
        if len(lines) <= i:
            return None
        m = re.fullmatch(r"<!--\s*wiki-i18n %s:\s*(.*?)\s*-->" % name, lines[i].strip())
        return m.group(1) if m and m.group(1) else None

    return value(0, "source"), value(1, "title")


def read_toml_strings(path):
    """{"section.key": "value"} of the plain `key = "value"` lines of a locale file (what this
    script needs of client/locales/<language>/wiki.toml)."""
    out = {}
    section = ""
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.read().split("\n")
    except OSError:
        return out
    for line in lines:
        t = line.strip()
        m = re.fullmatch(r"\[([A-Za-z0-9_.-]+)\]", t)
        if m:
            section = m.group(1)
            continue
        m = re.fullmatch(r'([A-Za-z0-9_-]+)\s*=\s*"((?:[^"\\]|\\.)*)"\s*(#.*)?', t)
        if not m:
            continue
        value = toml_unescape(m.group(2))
        if value is not None:
            out["%s.%s" % (section, m.group(1))] = value
    return out


def toml_unescape(s):
    """A TOML basic string's escapes resolved; None for one this script doesn't know."""
    simple = {"n": "\n", "t": "\t", '"': '"', "\\": "\\", "r": "\r", "b": "\b", "f": "\f", "e": "\x1b"}
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c != "\\":
            out.append(c)
            i += 1
            continue
        n = s[i + 1:i + 2]
        if n in simple:
            out.append(simple[n])
            i += 2
            continue
        k = {"u": 4, "U": 8}.get(n)
        digits = s[i + 2:i + 2 + k] if k else ""
        if not k or not re.fullmatch(r"[0-9A-Fa-f]{%d}" % k, digits):
            return None
        out.append(chr(int(digits, 16)))
        i += 2 + k
    return "".join(out)


class Language:
    """A language's texts from the game's locales (English's where it has none)."""

    def __init__(self, code, locales_dir, english=None):
        self.code = code
        self.name = dict(GAME_LANGUAGES).get(code, code)
        texts = read_toml_strings(os.path.join(locales_dir, code, "wiki.toml")) if locales_dir else {}
        self.texts = {k: v for k, v in texts.items() if v}
        self.english = english

    def text(self, section, key, default):
        v = self.texts.get("%s.%s" % (section, key))
        if v:
            return v
        return self.english.text(section, key, default) if self.english else default

    def ui(self):
        return {name: self.text(sec, key, default) for name, (sec, key, default) in UI_KEYS.items()}

    def callouts(self):
        return {kind: self.text("callout", kind.lower(), title) for kind, title in CALLOUTS.items()}

    def category(self, cat_id, default):
        return self.text("category", cat_id, default)


# ----- the wiki


class Site:
    """The articles, their links and pictures."""

    def __init__(self, wiki_dir, assets_dir):
        self.wiki_dir = wiki_dir
        self.pictures = Pictures(assets_dir)
        self.categories = []  # {id, name, order, dir, article_slugs}
        self.articles = []  # {slug, dir, file, path, text}
        self.by_path = {}
        self.by_stem = {}

    def read(self):
        dirs = sorted(d for d in os.listdir(self.wiki_dir) if os.path.isdir(os.path.join(self.wiki_dir, d)))
        found = []
        stems = {}
        for d in dirs:
            files = [f for f in os.listdir(os.path.join(self.wiki_dir, d)) if f.endswith(".md")]
            # The game's order: by the name in its list, case aside.
            files.sort(key=lambda f: (title_of(f).lower(), title_of(f)))
            for f in files:
                found.append((d, f))
                stems[file_slug(f)] = stems.get(file_slug(f), 0) + 1
        found.sort(key=lambda df: category_info(df[0])[0])
        cats = {}
        for d, f in found:
            order, name, cat_id = category_info(d)
            stem = file_slug(f)
            slug = "%s-%s" % (cat_id, stem) if stems[stem] > 1 else stem
            with open(os.path.join(self.wiki_dir, d, f), encoding="utf-8") as fh:
                text = fh.read()
            art = {"slug": slug, "dir": d, "file": f, "path": "%s/%s" % (d, f), "text": text}
            self.articles.append(art)
            self.by_path[art["path"].lower()] = slug
            self.by_stem.setdefault(f[:-3].lower(), slug)
            if d not in cats:
                cats[d] = {"id": cat_id, "name": name, "order": order, "dir": d, "article_slugs": []}
                self.categories.append(cats[d])
            cats[d]["article_slugs"].append(slug)
        if not self.articles:
            raise BuildError("no articles in %s" % self.wiki_dir)

    def resolve(self, url):
        """(slug, anchor) of a wiki link (/wiki/01-General/Getting-Started.md#x, Getting-Started.md,
        getting-started), as the game resolves it; (None, anchor) when it lands nowhere."""
        path, _, anchor = url.partition("#")
        path = urllib.parse.unquote(path).strip().lstrip("/")
        if path.startswith("wiki/"):
            path = path[5:]
        slug = self.by_path.get(path.lower())
        if not slug:
            stem = path.rsplit("/", 1)[-1]
            stem = (stem[:-3] if stem.endswith(".md") else stem).lower()
            slug = self.by_stem.get(stem) or self.by_stem.get(stem.replace("-", " "))
        return slug, (anchor or None)


def article_entry(site, art, text, cat, language, where):
    """An article's catalog entry in one language, and its renderer (for the link checks)."""
    blocks = parse(text)
    r = Renderer(site, art["dir"], where, language.callouts())
    title, anchor = art["file"][:-3].replace("-", " "), None
    body = blocks
    if blocks and blocks[0][0] == "h" and blocks[0][1] == 1:
        title, anchor = plain(blocks[0][2]), blocks[0][3]
        body = blocks[1:]
    html_body = r.render(body)
    words = len(text.split())
    entry = {
        "id": art["slug"],
        "title": title,
        "anchor": anchor,
        "category": language.category(cat["id"], cat["name"]),
        "categoryId": cat["id"],
        "filename": art["file"],
        "path": art["path"],
        "html": html_body,
        "toc": [{"level": lv, "title": t, "anchor": a} for lv, t, a in outline(body) if lv in (2, 3)],
        "wordCount": words,
        "readingTime": "%d min read" % max(1, round(words / 200)),
    }
    return entry, r, outline(blocks)


def check_links(site, renderers, anchors_of, label):
    """Warn about every link of the language `label` that lands on no article or heading."""
    for slug, r in renderers.items():
        for target, anchor, url in r.links:
            if target is None:
                warn("%s: the link %s lands on no article" % (r.where, url))
                continue
            target = target or slug
            if anchor and anchor not in anchors_of(target):
                warn("%s: the link %s lands on no heading of %s" % (r.where, url, target))


def build(wiki_dir, assets_dir, i18n_dir, locales_dir, out_dir):
    release = read_release(out_dir)
    site = Site(wiki_dir, assets_dir)
    site.read()
    english = Language("en", locales_dir)
    files = {}
    articles = {}
    renderers = {}
    anchors = {}
    cats = {c["dir"]: c for c in site.categories}
    for art in site.articles:
        cat = cats[art["dir"]]
        entry, r, heads = article_entry(site, art, art["text"], cat, english, "wiki/" + art["path"])
        mirror = mirror_text(art["text"], art["dir"], 1, site.pictures)
        entry["listTitle"] = title_of(art["file"])
        entry["markdown"] = mirror
        articles[art["slug"]] = entry
        renderers[art["slug"]] = r
        anchors[art["slug"]] = {a for _, _, a in heads}
        files["wiki/" + art["path"]] = mirror.encode("utf-8")
    check_links(site, renderers, lambda s: anchors.get(s, set()), "en")

    languages = []
    for code, pack, mirrors in translations(site, i18n_dir, locales_dir, english, anchors):
        files.update(mirrors)
        files["wiki/i18n/%s.json" % code] = (json.dumps(pack, indent=1, ensure_ascii=False) + "\n").encode("utf-8")
        languages.append({
            "code": code, "name": pack["name"], "articles": len(pack["articles"]),
            "stale": sum(1 for a in pack["articles"].values() if a.get("stale")),
            "catalog": "wiki/i18n/%s.json" % code, "markdown": "wiki/%s/" % code,
        })
    files.update(site.pictures.files)

    catalog = {
        "version": release["version"],
        "date": release["date"],
        "title": "SpaceCorps 2027 Wiki & Codex",
        "description": "The game's own wiki (assets/wiki of the release), rebuilt at every release: "
                       "ships, mechanics, aliens and items, with the pictures the game shows.",
        "source": "assets/wiki of SpaceCorps 2027 %s" % release["version"],
        "languages": languages,
        "categories": [{k: c[k] for k in ("id", "name", "order", "dir", "article_slugs")} for c in site.categories],
        "articles": articles,
    }
    files["wiki.json"] = (json.dumps(catalog, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    files["wiki.html"] = page(catalog, english).encode("utf-8")
    write(out_dir, files)
    summary = ", ".join("%s %d/%d" % (l["code"], l["articles"], len(articles)) for l in languages)
    print("Generated wiki.json, wiki.html and wiki/: %d articles, %d pictures%s, version %s" % (
        len(articles), len(site.pictures.files), "; translations: " + summary if summary else "", release["version"]))
    return catalog


def translations(site, i18n_dir, locales_dir, english, english_anchors):
    """(code, catalog, {mirror path: bytes}) of every language with a translated article."""
    if not i18n_dir or not os.path.isdir(i18n_dir):
        return []
    out = []
    by_path = {a["path"]: a for a in site.articles}
    cats = {c["dir"]: c for c in site.categories}
    order = {c: n for n, (c, _) in enumerate(GAME_LANGUAGES)}
    codes = sorted((d for d in os.listdir(i18n_dir) if os.path.isdir(os.path.join(i18n_dir, d))),
                   key=lambda c: (order.get(c, 99), c))
    for code in codes:
        if code == "en" or not LANGUAGE_CODE.fullmatch(code):
            continue
        root = os.path.join(i18n_dir, code)
        lang = Language(code, locales_dir, english)
        entries, renderers, anchors, mirrors = {}, {}, {}, {}
        for d in sorted(os.listdir(root)):
            if not os.path.isdir(os.path.join(root, d)):
                continue
            for f in sorted(os.listdir(os.path.join(root, d))):
                if not f.endswith(".md"):
                    continue
                art = by_path.get("%s/%s" % (d, f))
                where = "wiki-i18n/%s/%s/%s" % (code, d, f)
                if not art:
                    warn("%s: no English article %s/%s: left out" % (where, d, f))
                    continue
                with open(os.path.join(root, d, f), encoding="utf-8") as fh:
                    text = fh.read()
                source, list_title = translation_head(text)
                entry, r, heads = article_entry(site, art, text, cats[d], lang, where)
                mirror = mirror_text(text, d, 2, site.pictures)
                entry["listTitle"] = list_title or title_of(f)
                entry["markdown"] = mirror
                entry["stale"] = source != source_hash(art["text"])
                entries[art["slug"]] = entry
                renderers[art["slug"]] = r
                anchors[art["slug"]] = {a for _, _, a in heads}
                mirrors["wiki/%s/%s/%s" % (code, d, f)] = mirror.encode("utf-8")
        if not entries:
            continue
        # A link lands on the target's translation, or on the English page when it has none.
        check_links(site, renderers, lambda s: anchors.get(s, english_anchors.get(s, set())), code)
        ordered = {a["slug"]: entries[a["slug"]] for a in site.articles if a["slug"] in entries}
        pack = {
            "lang": code,
            "name": lang.name,
            "ui": lang.ui(),
            "categories": {c["id"]: lang.category(c["id"], c["name"]) for c in site.categories},
            "articles": ordered,
        }
        out.append((code, pack, mirrors))
    return out


def read_release(out_dir):
    path = os.path.join(out_dir, "release.json")
    try:
        with open(path, encoding="utf-8") as f:
            rel = json.load(f)
    except (OSError, ValueError) as err:
        raise BuildError("%s: %s (the wiki takes the version and date from it)" % (path, err))
    version = str(rel.get("version") or "").lstrip("v") if isinstance(rel, dict) else ""
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise BuildError("%s has no version" % path)
    date = rel.get("date") if isinstance(rel.get("date"), str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", rel.get("date")) else None
    return {"version": version, "date": date}


def write(out_dir, files):
    """Writes the files; removes what else wiki/ has (the folder is the build's)."""
    wiki = os.path.join(out_dir, "wiki")
    if os.path.isdir(wiki):
        for dirpath, dirnames, filenames in os.walk(wiki, topdown=False):
            for name in filenames:
                rel = os.path.relpath(os.path.join(dirpath, name), out_dir).replace(os.sep, "/")
                if rel not in files:
                    os.remove(os.path.join(dirpath, name))
            if dirpath != wiki and not os.listdir(dirpath):
                os.rmdir(dirpath)
    for rel, data in files.items():
        path = os.path.join(out_dir, *rel.split("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        try:
            with open(path, "rb") as f:
                if f.read() == data:
                    continue
        except OSError:
            pass
        with open(path, "wb") as f:
            f.write(data)


def find_wiki_dir(specified=None):
    if specified:
        if os.path.isdir(specified):
            return os.path.abspath(specified)
        raise BuildError("no folder %s" % specified)
    for c in CANDIDATE_DIRS:
        if os.path.isdir(c):
            return os.path.abspath(c)
    raise BuildError("found no assets/wiki of the game: python3 scripts/build-wiki.py <path to assets/wiki>")


def main(argv):
    ap = argparse.ArgumentParser(prog="build-wiki.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("wiki", nargs="?", help="the game's assets/wiki")
    ap.add_argument("--assets", help="the folder picture paths end up in (default: the wiki's parent)")
    ap.add_argument("--i18n", help="the translations (default: wiki-i18n next to the wiki, if any)")
    ap.add_argument("--locales", help="the game's client/locales (default: next to assets/, if any)")
    ap.add_argument("--no-i18n", action="store_true", help="English only")
    ap.add_argument("--out", default=PLAY_ROOT, help=argparse.SUPPRESS)
    args = ap.parse_args(argv)
    try:
        wiki_dir = find_wiki_dir(args.wiki)
        print("Reading the game's wiki from %s" % wiki_dir)
        parent = os.path.dirname(wiki_dir)
        assets_dir = os.path.abspath(args.assets) if args.assets else parent
        i18n_dir = None
        if not args.no_i18n:
            i18n_dir = args.i18n or os.path.join(parent, "wiki-i18n")
            if args.i18n and not os.path.isdir(args.i18n):
                raise BuildError("no folder %s" % args.i18n)
        locales_dir = args.locales or os.path.join(os.path.dirname(parent), "client", "locales")
        if args.locales and not os.path.isdir(args.locales):
            raise BuildError("no folder %s" % args.locales)
        if not os.path.isdir(locales_dir):
            locales_dir = None
        build(wiki_dir, assets_dir, i18n_dir, locales_dir, os.path.abspath(args.out))
        return 0
    except (BuildError, OSError, UnicodeDecodeError) as err:
        print("error: %s" % err, file=sys.stderr)
        return 1


# ----- the page

def json_for_script(value):
    """JSON safe inside <script>: no </script>, no <!--."""
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")


def page(catalog, english):
    arts = catalog["articles"]
    default = "getting-started" if "getting-started" in arts else next(iter(arts))
    first = arts[default]
    languages = [{"code": "en", "name": "English"}] + [
        {"code": l["code"], "name": l["name"], "catalog": l["catalog"]} for l in catalog["languages"]]
    data = {
        "version": catalog["version"],
        "default": default,
        "ui": english.ui(),
        "languages": languages,
        "categories": [{"id": c["id"], "name": c["name"], "article_slugs": c["article_slugs"]} for c in catalog["categories"]],
        "articles": {s: {k: a[k] for k in ("id", "title", "listTitle", "anchor", "category", "categoryId", "path",
                                            "html", "toc", "wordCount", "readingTime")}
                     for s, a in arts.items()},
    }
    wiki_codes = {l["code"] for l in languages}
    menu = []
    for code, name in GAME_LANGUAGES:
        if code in SITE_LANGUAGES or code in wiki_codes:
            menu.append('        <li><a href="?lang=%s" hreflang="%s" lang="%s"%s>%s<svg class="icon" aria-hidden="true">'
                        '<use href="#i-check"/></svg></a></li>' % (code, code, code, ' aria-current="true"' if code == "en" else "", esc(name)))
    sidebar = []
    for c in catalog["categories"]:
        sidebar.append('<div class="wiki-cat-group"><div class="wiki-cat-title">%s (%d)</div><ul class="wiki-nav-list">' % (
            esc(c["name"]), len(c["article_slugs"])))
        for s in c["article_slugs"]:
            sidebar.append('<li class="wiki-nav-item%s" data-slug="%s"><a href="?article=%s">%s</a></li>' % (
                " active" if s == default else "", esc(s), esc(s), esc(arts[s]["listTitle"])))
        sidebar.append("</ul></div>")
    toc = "".join('<li class="wiki-toc-item level-%d"><a href="#%s">%s</a></li>' % (t["level"], esc(t["anchor"]), esc(t["title"]))
                  for t in first["toc"])
    in_language = json.dumps([l["code"] for l in languages])
    values = {
        "VERSION": esc(catalog["version"]),
        "DATE_MODIFIED": catalog["date"] or "2026-09-28",
        "IN_LANGUAGE": in_language,
        "LANG_MENU": "\n".join(menu),
        "SIDEBAR": "".join(sidebar),
        "ON_THIS_PAGE": esc(english.ui()["onThisPage"]),
        "TOC": toc,
        "ARTICLE_CATEGORY": esc(first["category"]),
        "ARTICLE_READTIME": esc(first["readingTime"]),
        "ARTICLE_WORDS": str(first["wordCount"]),
        "ARTICLE_ANCHOR": esc(first["anchor"] or ""),
        "ARTICLE_TITLE": esc(first["title"]),
        "ARTICLE_HTML": first["html"],
        "ARTICLE_COUNT": str(len(arts)),
        "DATA": json_for_script(data),
    }
    out = PAGE
    for key, value in values.items():
        out = out.replace("%%" + key + "%%", value)
    left = re.findall(r"%%[A-Z_]+%%", out)
    if left:
        raise BuildError("the page template has no value for %s" % ", ".join(sorted(set(left))))
    return out


PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SpaceCorps 2027 · Game Wiki &amp; Pilot Codex</title>
<meta name="description" content="The SpaceCorps 2027 wiki, the game's own: ship specifications, abilities, aliens, mechanics, weapons and the Skylab, rebuilt from the game at every release.">
<meta name="color-scheme" content="dark">
<meta name="theme-color" content="#141312">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta name="bingbot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta name="is-agentic-site-type" content="content">
<meta name="author" content="SpaceCorps">
<meta name="keywords" content="SpaceCorps 2027 wiki, SpaceCorps ships, Protos, Kitefin, Wraith, Paragon, Ostirion, Ironclad, Skylab guide, Black Hole, SpaceCorps mechanics, alien guide">
<link rel="canonical" href="https://spacecorps.github.io/play/wiki.html">
<link rel="alternate" type="application/json" href="https://spacecorps.github.io/play/wiki.json">
<link rel="help" href="https://spacecorps.github.io/play/llms.txt">
<link rel="icon" href="favicon.ico" sizes="32x32">
<link rel="icon" type="image/svg+xml" href="img/favicon.svg">
<link rel="icon" type="image/png" sizes="48x48" href="img/favicon-48.png">
<link rel="icon" type="image/png" sizes="96x96" href="img/favicon-96.png">
<link rel="icon" type="image/png" sizes="32x32" href="img/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="img/favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="img/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<meta property="og:type" content="website">
<meta property="og:site_name" content="SpaceCorps">
<meta property="og:title" content="SpaceCorps 2027 · Game Wiki &amp; Pilot Codex">
<meta property="og:description" content="The game's own wiki: ship specifications, mechanics, aliens, weapons and the Skylab, rebuilt at every release.">
<meta property="og:url" content="https://spacecorps.github.io/play/wiki.html">
<meta property="og:image" content="https://spacecorps.github.io/play/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@SpaceCorps">
<meta name="twitter:creator" content="@SpaceCorps">
<meta name="twitter:title" content="SpaceCorps 2027 · Game Wiki &amp; Pilot Codex">
<meta name="twitter:description" content="The game's own wiki: ship specifications, mechanics, aliens, weapons and the Skylab, rebuilt at every release.">
<meta name="twitter:image" content="https://spacecorps.github.io/play/img/og.jpg">
<link rel="stylesheet" href="style.css">
<style>
  /* Wiki Layout & Typography */
  .wiki-container {
    max-width: calc(var(--page) + 2 * var(--gutter));
    margin: 0 auto;
    padding: 24px var(--gutter) 80px;
  }
  .wiki-header {
    padding: 32px 0 24px;
    border-bottom: 1px solid var(--separator);
    margin-bottom: 28px;
    display: flex;
    flex-wrap: wrap;
    align-items: flex-end;
    justify-content: space-between;
    gap: 16px;
  }
  .wiki-header-copy h1 {
    font-size: clamp(28px, 4vw, 40px);
    font-weight: 700;
    letter-spacing: -0.02em;
    line-height: 1.1;
  }
  .wiki-header-copy p {
    color: var(--text-2);
    margin-top: 6px;
    font-size: 15px;
  }
  .wiki-version {
    display: inline-block;
    margin-left: 10px;
    padding: 2px 8px;
    border: 1px solid var(--separator);
    border-radius: 4px;
    font-family: var(--mono);
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0;
    color: var(--text-2);
    vertical-align: middle;
  }
  .wiki-search-box {
    position: relative;
    width: 100%;
    max-width: 320px;
  }
  .wiki-search-input {
    width: 100%;
    height: 40px;
    padding: 0 36px 0 38px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-control);
    color: var(--text);
    font-family: var(--font);
    font-size: 14px;
    transition: border-color 0.15s ease, background 0.15s ease;
  }
  .wiki-search-input:focus {
    background: var(--elevated);
    border-color: var(--accent);
    outline: none;
  }
  .wiki-search-icon {
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-3);
    pointer-events: none;
    width: 16px;
    height: 16px;
  }
  .wiki-search-badge {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 11px;
    color: var(--text-3);
    border: 1px solid var(--separator);
    border-radius: 4px;
    padding: 1px 5px;
    pointer-events: none;
  }
  .wiki-layout {
    display: grid;
    grid-template-columns: 260px minmax(0, 1fr) 220px;
    gap: 36px;
    align-items: start;
  }
  @media (max-width: 1040px) {
    .wiki-layout {
      grid-template-columns: 240px minmax(0, 1fr);
    }
    .wiki-toc-pane {
      display: none;
    }
  }
  @media (max-width: 760px) {
    .wiki-layout {
      grid-template-columns: minmax(0, 1fr);
    }
  }

  /* Sidebar */
  .wiki-sidebar {
    position: sticky;
    top: 80px;
    max-height: calc(100vh - 100px);
    overflow-y: auto;
    padding-right: 12px;
    scrollbar-width: thin;
    scrollbar-color: var(--separator) transparent;
  }
  @media (max-width: 760px) {
    /* One column: the list above the article, scrolling with the page (after the rule above). */
    .wiki-sidebar {
      position: static;
      max-height: none;
      margin-bottom: 24px;
    }
  }
  .wiki-cat-group {
    margin-bottom: 20px;
  }
  .wiki-cat-title {
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-3);
    margin-bottom: 8px;
    padding-left: 10px;
  }
  .wiki-nav-list {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .wiki-nav-item a {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 6px 10px;
    border-radius: var(--radius-control);
    color: var(--text-2);
    font-size: 13.5px;
    line-height: 1.35;
    transition: background 0.12s ease, color 0.12s ease;
  }
  .wiki-nav-item a:hover {
    color: var(--text);
    background: rgba(255, 255, 255, 0.05);
    text-decoration: none;
  }
  .wiki-nav-item.active a {
    color: var(--accent);
    background: var(--accent-soft);
    font-weight: 600;
  }

  /* Center Article Pane */
  .wiki-article-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-card);
    padding: 36px 40px;
    box-shadow: var(--shadow);
  }
  @media (max-width: 600px) {
    .wiki-article-card {
      padding: 24px 20px;
    }
  }
  .wiki-meta-row {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
    font-size: 13px;
    color: var(--text-3);
  }
  .wiki-tag {
    background: rgba(255, 255, 255, 0.06);
    color: var(--accent);
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
    font-size: 12px;
  }
  .wiki-note {
    margin: 0 0 16px;
    padding: 8px 12px;
    border: 1px solid var(--separator);
    border-radius: var(--radius-control);
    background: rgba(255, 255, 255, 0.04);
    color: var(--text-2);
    font-size: 13.5px;
    line-height: 1.5;
  }
  .wiki-note[hidden] {
    display: none;
  }
  .wiki-note button {
    margin-left: 4px;
    padding: 0;
    border: 0;
    background: none;
    color: var(--accent);
    font: inherit;
    text-decoration: underline;
    cursor: pointer;
  }
  .wiki-article-title {
    font-size: clamp(26px, 3.5vw, 36px);
    font-weight: 700;
    letter-spacing: -0.02em;
    line-height: 1.15;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--separator);
    scroll-margin-top: 84px;
  }
  .wiki-content {
    color: var(--text);
    font-size: 15.5px;
    line-height: 1.7;
  }
  .wiki-content p {
    margin-bottom: 16px;
  }
  .wiki-content :is(h1, h2, h3, h4, h5, h6) {
    scroll-margin-top: 84px;
  }
  .wiki-content h1, .wiki-content h2 {
    font-size: 22px;
    font-weight: 700;
    margin: 32px 0 14px;
    padding-bottom: 6px;
    border-bottom: 1px solid var(--separator);
  }
  .wiki-content h3 {
    font-size: 17px;
    font-weight: 600;
    margin: 24px 0 10px;
  }
  .wiki-content :is(h4, h5, h6) {
    font-size: 15.5px;
    font-weight: 600;
    margin: 20px 0 8px;
  }
  .wiki-content ul, .wiki-content ol {
    margin: 0 0 20px 24px;
    padding: 0;
  }
  .wiki-content li > :is(ul, ol) {
    margin: 6px 0 6px 22px;
  }
  .wiki-content li {
    margin-bottom: 6px;
  }
  .wiki-content hr {
    border: none;
    border-top: 1px solid var(--separator);
    margin: 28px 0;
  }
  .wiki-content pre, .wiki-content .wiki-math {
    background: var(--elevated);
    border: 1px solid var(--border);
    border-radius: var(--radius-control);
    padding: 14px 16px;
    overflow-x: auto;
    font-size: 13.5px;
    line-height: 1.45;
    margin-bottom: 20px;
  }
  .wiki-content .wiki-math {
    font-family: var(--mono);
  }
  .wiki-content blockquote {
    margin: 0 0 20px;
    padding: 10px 16px;
    border-left: 3px solid var(--separator);
    color: var(--text-2);
  }
  .wiki-content blockquote p:last-child {
    margin-bottom: 0;
  }
  .wiki-content .wiki-callout {
    border-left-color: var(--accent);
    background: rgba(255, 255, 255, 0.03);
    border-radius: 0 var(--radius-control) var(--radius-control) 0;
  }
  .wiki-content .wiki-callout-warning, .wiki-content .wiki-callout-caution {
    border-left-color: var(--warn);
  }
  .wiki-content .wiki-callout-title {
    margin-bottom: 4px;
    color: var(--text);
    font-weight: 700;
  }
  .wiki-spacemap {
    margin: 0 0 20px;
    padding: 18px 16px;
    border: 1px dashed var(--border);
    border-radius: var(--radius-control);
    color: var(--text-3);
    font-size: 14px;
    text-align: center;
  }
  .wiki-gallery {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
    margin: 4px 0 24px;
  }
  .wiki-gallery-one {
    grid-template-columns: minmax(0, 1fr);
  }
  @media (max-width: 600px) {
    .wiki-gallery {
      grid-template-columns: minmax(0, 1fr);
    }
  }
  .wiki-figure {
    margin: 0;
  }
  .wiki-figure img {
    display: block;
    width: 100%;
    height: auto;
    border: 1px solid var(--border);
    border-radius: var(--radius-control);
    background: var(--elevated);
  }
  .wiki-figure figcaption {
    margin-top: 6px;
    color: var(--text-2);
    font-size: 13px;
    line-height: 1.4;
  }
  .wiki-figure-missing figcaption {
    font-style: italic;
  }
  .table-wrap {
    width: 100%;
    overflow-x: auto;
    margin: 20px 0;
    border: 1px solid var(--border);
    border-radius: var(--radius-control);
  }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    text-align: left;
  }
  th, td {
    padding: 10px 14px;
    border-bottom: 1px solid var(--separator);
  }
  th {
    background: rgba(255, 255, 255, 0.04);
    font-weight: 600;
    color: var(--text-2);
  }
  tr:last-child td {
    border-bottom: none;
  }
  tr:hover td {
    background: rgba(255, 255, 255, 0.02);
  }
  .wiki-pagination {
    margin-top: 36px;
    padding-top: 24px;
    border-top: 1px solid var(--separator);
    display: flex;
    justify-content: space-between;
    gap: 16px;
  }
  .wiki-page-btn {
    display: inline-flex;
    flex-direction: column;
    padding: 10px 16px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--border);
    border-radius: var(--radius-control);
    font-size: 13px;
    color: var(--text-2);
    transition: background 0.15s ease, border-color 0.15s ease;
  }
  .wiki-page-btn:hover {
    background: rgba(255, 255, 255, 0.06);
    border-color: var(--accent);
    color: var(--text);
    text-decoration: none;
  }
  .wiki-page-btn-title {
    font-weight: 600;
    color: var(--text);
    font-size: 14px;
    margin-top: 2px;
  }

  /* Right TOC */
  .wiki-toc-pane {
    position: sticky;
    top: 80px;
    max-height: calc(100vh - 100px);
    overflow-y: auto;
    font-size: 13px;
  }
  .wiki-toc-title {
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-3);
    margin-bottom: 12px;
  }
  .wiki-toc-list {
    list-style: none;
    margin: 0;
    padding: 0;
    border-left: 1px solid var(--separator);
  }
  .wiki-toc-item a {
    display: block;
    padding: 4px 0 4px 14px;
    color: var(--text-2);
    line-height: 1.35;
    margin-left: -1px;
    border-left: 2px solid transparent;
  }
  .wiki-toc-item a:hover {
    color: var(--text);
    text-decoration: none;
    border-left-color: var(--text-3);
  }
  .wiki-toc-item.level-3 a {
    padding-left: 24px;
    font-size: 12px;
  }
  .wiki-toc-item.active a {
    color: var(--accent);
    border-left-color: var(--accent);
    font-weight: 600;
  }
</style>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "SpaceCorps",
          "item": "https://spacecorps.github.io/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "SpaceCorps 2027",
          "item": "https://spacecorps.github.io/play/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Wiki &amp; Pilot Codex",
          "item": "https://spacecorps.github.io/play/wiki.html"
        }
      ]
    },
    {
      "@type": "TechArticle",
      "@id": "https://spacecorps.github.io/play/wiki.html#codex",
      "url": "https://spacecorps.github.io/play/wiki.html",
      "name": "SpaceCorps 2027 Game Wiki &amp; Pilot Codex",
      "headline": "SpaceCorps 2027 Game Wiki &amp; Pilot Codex",
      "description": "Comprehensive reference of ship statistics, combat mechanics, Skylab production, alien species, and equipment loadouts for SpaceCorps 2027.",
      "version": "%%VERSION%%",
      "inLanguage": %%IN_LANGUAGE%%,
      "datePublished": "2026-09-26",
      "dateModified": "%%DATE_MODIFIED%%",
      "author": {
        "@type": "Organization",
        "name": "SpaceCorps",
        "url": "https://spacecorps.github.io/"
      },
      "publisher": {
        "@type": "Organization",
        "name": "SpaceCorps",
        "url": "https://spacecorps.github.io/",
        "logo": "https://spacecorps.github.io/play/img/icon-128.png"
      }
    }
  ]
}
</script>
<script>
if (typeof document !== 'undefined') {
  const mcp = document.modelContext || (typeof navigator !== 'undefined' && navigator.modelContext);
  if (mcp && typeof mcp.registerTool === 'function') {
    mcp.registerTool({
      name: 'get_wiki_article',
      description: 'Get structured markdown and HTML content for a SpaceCorps 2027 wiki article by slug (e.g. "protos", "quests", "skylab").',
      inputSchema: { type: 'object', properties: { article: { type: 'string' } }, required: ['article'] },
      execute: async ({ article }) => {
        const res = await fetch('wiki.json');
        const data = await res.json();
        return data.articles[article] || { error: 'Not found', available: Object.keys(data.articles) };
      }
    });
    mcp.registerTool({
      name: 'list_wiki_articles',
      description: 'List all available SpaceCorps 2027 wiki categories and article slugs.',
      inputSchema: { type: 'object', properties: {} },
      execute: async () => {
        const res = await fetch('wiki.json');
        const data = await res.json();
        return { categories: data.categories, articles: Object.keys(data.articles) };
      }
    });
  }
}
</script>
<script src="i18n.js"></script>
<script src="app.js" defer></script>
</head>
<body>
<a class="skip" href="#wiki-main" data-i18n="skip">Skip to content</a>

<svg width="0" height="0" class="sprite" aria-hidden="true" focusable="false">
  <symbol id="i-download" viewBox="0 0 24 24"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 19.5h14"/></symbol>
  <symbol id="i-copy" viewBox="0 0 24 24"><rect x="8.5" y="8.5" width="11.5" height="11.5" rx="2"/><path d="M15.5 8.5V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v7.5a2 2 0 0 0 2 2h2.5"/></symbol>
  <symbol id="i-check" viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></symbol>
  <symbol id="i-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></symbol>
  <symbol id="i-globe" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.8 5.5 3.8 9s-1.3 6.5-3.8 9c-2.5-2.5-3.8-5.5-3.8-9S9.5 5.5 12 3z"/></symbol>
  <symbol id="i-chevron" viewBox="0 0 24 24"><path d="m7 10 5 5 5-5"/></symbol>
  <symbol id="i-book" viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></symbol>
</svg>

<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="./" aria-label="SpaceCorps 2027, back to download" data-i18n-aria-label="nav.home">
      <img src="img/icon-128.png" width="28" height="28" alt="">
      <span class="brand-name">SpaceCorps <span class="brand-year">2027</span></span>
    </a>
    <nav class="nav" aria-label="Sections" data-i18n-aria-label="nav.label">
      <a href="./#screenshots" data-i18n="nav.screenshots">Screenshots</a>
      <a href="./#features" data-i18n="nav.features">Features</a>
      <a href="./#download" data-i18n="nav.download">Download</a>
      <a href="./#help" data-i18n="nav.help">Help</a>
      <a href="wiki.html" style="color:var(--text);font-weight:600" data-i18n="nav.wiki">Wiki</a>
      <a href="patchnotes.html" data-i18n="nav.patchnotes">Patch notes</a>
    </nav>
    <a class="status" href="./#server" data-status="checking" title="Game server status" data-i18n-title="status.title">
      <span class="status-dot" aria-hidden="true"></span>
      <span class="status-text" role="status" aria-live="polite" data-i18n="status.pill.checking">Server</span>
    </a>
    <details class="lang" id="lang">
      <summary class="lang-button" aria-label="Language: English">
        <svg class="icon" aria-hidden="true"><use href="#i-globe"/></svg>
        <span class="lang-name" aria-hidden="true">English</span>
        <span class="lang-code" aria-hidden="true">EN</span>
        <svg class="icon lang-chevron" aria-hidden="true"><use href="#i-chevron"/></svg>
      </summary>
      <ul class="lang-menu" role="list">
%%LANG_MENU%%
      </ul>
    </details>
  </div>
</header>

<main class="wiki-container" id="wiki-main">
  <div class="wiki-header">
    <div class="wiki-header-copy">
      <h1>Pilot Codex &amp; Wiki <span class="wiki-version" title="The game version this wiki is from">v%%VERSION%%</span></h1>
      <p>Ships, mechanics, aliens, items and the Skylab: the game's own wiki, rebuilt from the game at every release.</p>
    </div>
    <div class="wiki-search-box">
      <svg class="icon wiki-search-icon" aria-hidden="true"><use href="#i-search"/></svg>
      <input type="search" class="wiki-search-input" id="wiki-search" placeholder="Search articles, ships, aliens..." aria-label="Search Wiki articles">
      <span class="wiki-search-badge">/</span>
    </div>
  </div>

  <div class="wiki-layout">
    <!-- Left Navigation Sidebar -->
    <aside class="wiki-sidebar" id="wiki-nav" aria-label="Wiki articles">
      <div id="wiki-sidebar-content">%%SIDEBAR%%</div>
    </aside>

    <!-- Center Article Reader -->
    <article class="wiki-article-card" id="wiki-article-pane" lang="en">
      <div class="wiki-meta-row">
        <span class="wiki-tag" id="article-category">%%ARTICLE_CATEGORY%%</span>
        <span id="article-readtime">%%ARTICLE_READTIME%%</span>
        <span>•</span>
        <span id="article-wordcount">%%ARTICLE_WORDS%% words</span>
      </div>
      <p class="wiki-note" id="article-note" hidden></p>
      <h2 class="wiki-article-title" id="article-title" data-anchor="%%ARTICLE_ANCHOR%%">%%ARTICLE_TITLE%%</h2>
      <div class="wiki-content" id="article-body">
%%ARTICLE_HTML%%
      </div>
      <div class="wiki-pagination" id="article-pagination"></div>
    </article>

    <!-- Right "On this page" TOC -->
    <aside class="wiki-toc-pane" id="wiki-toc-pane" aria-label="On this page">
      <div class="wiki-toc-title" id="wiki-toc-title">%%ON_THIS_PAGE%%</div>
      <ul class="wiki-toc-list" id="wiki-toc-list">%%TOC%%</ul>
    </aside>
  </div>
</main>

<footer class="footer">
  <div class="footer-inner">
    <div class="footer-brand">
      <img src="img/icon-128.png" width="24" height="24" alt="">
      <span>SpaceCorps © 2026</span>
    </div>
    <nav class="footer-links" aria-label="Elsewhere" data-i18n-aria-label="footer.label">
      <a href="./#download" data-i18n="nav.download">Download</a>
      <a href="wiki.html" data-i18n="nav.wiki">Wiki</a>
      <a href="patchnotes.html" data-i18n="nav.patchnotes">Patch notes</a>
      <a href="https://discord.gg/VjW67tkrTb">Discord</a>
      <a href="https://github.com/SpaceCorps/play">GitHub</a>
      <a href="wiki.json">wiki.json</a>
      <a href="llms.txt">llms.txt</a>
      <a href="https://spacecorps.github.io/">SpaceCorps Hub</a>
    </nav>
    <p class="footer-note" data-i18n="footer.note">Built on the Space3d engine. No cookies, no trackers. Articles programmatically synced from base game assets/wiki.</p>
  </div>
</footer>

<script type="application/json" id="wiki-data">%%DATA%%</script>
<script>
// The wiki's articles in the reader's language: the English ones are in the page (wiki-data), a
// translation's are loaded from wiki/i18n/<code>.json when the language is picked. An article a
// language lacks shows in English with a note; one whose English page changed since it was
// translated says so and offers the English page. The language: ?lang= (any of the wiki's), else
// the download page's (i18n.js), else English. Written by scripts/build-wiki.py: edit it there.
(() => {
  'use strict';
  const WIKI = JSON.parse(document.getElementById('wiki-data').textContent);
  const EN = 'en';
  const packs = { en: { ui: WIKI.ui, categories: {}, articles: {} } };
  const loading = {};
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);
  const byCode = (code) => WIKI.languages.find((l) => l.code.toLowerCase() === String(code || '').toLowerCase());
  const site = () => window.SpaceCorpsI18n;
  const siteKnows = (code) => !!(site() && site().languages.some((l) => l.code.toLowerCase() === String(code).toLowerCase()));

  let lang = EN;
  let slug = WIKI.default;
  let english = false; // the reader asked for the English page of a translated article
  let wikiOnly = false; // the language is one the download page doesn't have (picked here)
  let titleEl = null; // the article's title: its id is the article's own anchor

  function loadPack(code) {
    if (packs[code]) return Promise.resolve(packs[code]);
    const l = byCode(code);
    if (!l || !l.catalog) return Promise.resolve(null);
    if (!loading[code]) {
      loading[code] = fetch(l.catalog)
        .then((r) => (r.ok ? r.json() : Promise.reject(new Error(`${l.catalog}: ${r.status}`))))
        .then((p) => { packs[code] = p; return p; })
        .catch((err) => { console.warn(err); delete loading[code]; return null; });
    }
    return loading[code];
  }

  const pack = () => (lang !== EN && packs[lang]) || null;
  const ui = (key) => { const p = pack(); return (p && p.ui && p.ui[key]) || WIKI.ui[key] || ''; };
  const translated = (s) => { const p = pack(); return p && p.articles ? p.articles[s] || null : null; };
  const listTitle = (s) => { const t = translated(s); return (t && t.listTitle) || WIKI.articles[s].listTitle; };
  const categoryName = (c) => { const p = pack(); return (p && p.categories && p.categories[c.id]) || c.name; };

  // What shows for the article s: the translation, or the English page and why.
  function shown(s) {
    const en = WIKI.articles[s];
    if (lang === EN) return { a: en, lang: EN, note: null };
    const t = translated(s);
    if (t && !english) return { a: t, lang, note: t.stale ? 'stale' : null };
    if (t) return { a: en, lang: EN, note: 'english' };
    return { a: en, lang: EN, note: 'missing' };
  }

  // An article's words for the search: its HTML without the tags.
  const texts = new WeakMap();
  function textOf(a) {
    if (!texts.has(a)) texts.set(a, a.html.replace(/<[^>]+>/g, ' ').replace(/&amp;/g, '&').toLowerCase());
    return texts.get(a);
  }

  function renderSidebar() {
    const query = $('wiki-search').value.toLowerCase().trim();
    let out = '';
    WIKI.categories.forEach((cat) => {
      const slugs = cat.article_slugs.filter((s) => {
        if (!WIKI.articles[s]) return false;
        if (!query) return true;
        const t = translated(s);
        return [WIKI.articles[s], t].some((a) => a && (
          a.title.toLowerCase().includes(query) || (a.listTitle || '').toLowerCase().includes(query)
          || (a.category || '').toLowerCase().includes(query) || textOf(a).includes(query)));
      });
      if (!slugs.length) return;
      out += `<div class="wiki-cat-group"><div class="wiki-cat-title">${esc(categoryName(cat))} (${slugs.length})</div><ul class="wiki-nav-list">`;
      slugs.forEach((s) => {
        out += `<li class="wiki-nav-item${s === slug ? ' active' : ''}" data-slug="${esc(s)}"><a href="${esc(articleUrl(s))}" data-article="${esc(s)}">${esc(listTitle(s))}</a></li>`;
      });
      out += '</ul></div>';
    });
    if (!out) out = `<p style="padding:12px;color:var(--text-3);font-size:13px">No articles match "${esc($('wiki-search').value)}"</p>`;
    const nav = $('wiki-sidebar-content');
    nav.innerHTML = out;
    nav.lang = lang;
  }

  function articleUrl(s, anchor) {
    const url = new URL(location.href);
    url.searchParams.set('article', s);
    url.hash = anchor ? `#${anchor}` : '';
    return url.pathname.split('/').pop() + url.search + url.hash;
  }

  function renderNote(note) {
    const el = $('article-note');
    if (!note) {
      el.hidden = true;
      el.textContent = '';
      return;
    }
    const text = { missing: ui('englishOnly'), stale: ui('stale'), english: ui('showingEnglish') }[note];
    const button = { stale: ui('readEnglish'), english: ui('back') }[note];
    el.innerHTML = esc(text) + (button ? ` <button type="button" id="article-note-switch">${esc(button)}</button>` : '');
    el.lang = lang;
    el.hidden = false;
    const b = $('article-note-switch');
    if (b) b.addEventListener('click', () => { english = note === 'stale'; open(slug, { keepScroll: true }); });
  }

  function open(s, opts) {
    const o = opts || {};
    if (!WIKI.articles[s]) return;
    if (s !== slug) english = false;
    slug = s;
    const view = shown(s);
    const a = view.a;
    $('article-category').textContent = categoryName({ id: WIKI.articles[s].categoryId, name: WIKI.articles[s].category });
    $('article-readtime').textContent = a.readingTime;
    $('article-wordcount').textContent = `${a.wordCount} words`;
    titleEl.textContent = a.title;
    titleEl.id = a.anchor || 'article-title';
    $('article-body').innerHTML = a.html;
    $('wiki-article-pane').lang = view.lang;
    renderNote(view.note);
    document.title = `${a.title} · SpaceCorps 2027 Wiki`;

    $('wiki-toc-title').textContent = ui('onThisPage');
    const toc = $('wiki-toc-list');
    if (a.toc && a.toc.length) {
      $('wiki-toc-pane').style.display = '';
      toc.innerHTML = a.toc.map((t) => `<li class="wiki-toc-item level-${t.level}"><a href="#${esc(t.anchor)}">${esc(t.title)}</a></li>`).join('');
      toc.lang = view.lang;
    } else {
      $('wiki-toc-pane').style.display = 'none';
    }

    const all = [];
    WIKI.categories.forEach((c) => c.article_slugs.forEach((x) => all.push(x)));
    const i = all.indexOf(s);
    const prev = i > 0 ? all[i - 1] : null;
    const next = i >= 0 && i < all.length - 1 ? all[i + 1] : null;
    let pag = prev ? `<a href="${esc(articleUrl(prev))}" class="wiki-page-btn" data-article="${esc(prev)}"><span>&larr; Previous</span><span class="wiki-page-btn-title">${esc(listTitle(prev))}</span></a>` : '<div></div>';
    if (next) pag += `<a href="${esc(articleUrl(next))}" class="wiki-page-btn" style="text-align:right" data-article="${esc(next)}"><span>Next &rarr;</span><span class="wiki-page-btn-title">${esc(listTitle(next))}</span></a>`;
    $('article-pagination').innerHTML = pag;
    $('article-pagination').lang = lang;

    document.querySelectorAll('.wiki-nav-item').forEach((el) => el.classList.toggle('active', el.getAttribute('data-slug') === s));
    if (o.push) history.pushState({ article: s }, '', articleUrl(s, o.anchor));
    else if (o.replace) history.replaceState({ article: s }, '', articleUrl(s, o.anchor));

    const target = o.anchor && document.getElementById(o.anchor);
    if (target) target.scrollIntoView();
    else if (o.push) window.scrollTo({ top: $('wiki-main').offsetTop - 20, behavior: 'smooth' });
  }

  async function setLanguage(code) {
    const l = byCode(code);
    let next = l ? l.code : EN;
    if (next !== EN && !(await loadPack(next))) next = EN;
    if (next === lang) return;
    lang = next;
    english = false;
    renderSidebar();
    open(slug, { keepScroll: true });
    markMenu();
  }

  // The menu's button and tick for a language the download page doesn't have (i18n.js does
  // its own).
  function markMenu() {
    const menu = $('lang');
    if (!menu || !wikiOnly) return;
    const l = byCode(lang);
    const name = menu.querySelector('.lang-name');
    if (name && l) name.textContent = l.name;
    const code = menu.querySelector('.lang-code');
    if (code && l) code.textContent = l.code.split('-')[0].toUpperCase();
    menu.querySelectorAll('a[hreflang]').forEach((a) => {
      if (a.getAttribute('hreflang') === lang) a.setAttribute('aria-current', 'true');
      else a.removeAttribute('aria-current');
    });
  }

  function start() {
    titleEl = $('article-title');
    const params = new URLSearchParams(location.search);
    const asked = params.get('article') || location.hash.slice(1);
    const anchor = params.get('article') ? location.hash.slice(1) : '';
    slug = WIKI.articles[asked] ? asked : WIKI.default;
    renderSidebar();
    open(slug, { anchor: anchor || null });

    const wanted = byCode(params.get('lang'));
    if (wanted && wanted.code !== EN) {
      wikiOnly = !siteKnows(wanted.code);
      setLanguage(wanted.code).then(() => { if (anchor) open(slug, { anchor }); });
    }
    let siteReady = false;
    if (site()) {
      site().subscribe((code) => {
        // The first call is the page's own choice: a wiki-only language from the address stays.
        if (!siteReady) {
          siteReady = true;
          if (wikiOnly || (wanted && wanted.code !== EN)) return;
        }
        wikiOnly = false;
        setLanguage(byCode(code) ? code : EN);
      });
    }

    $('wiki-search').addEventListener('input', renderSidebar);
    window.addEventListener('keydown', (e) => {
      if (e.key === '/' && document.activeElement !== $('wiki-search')) {
        e.preventDefault();
        $('wiki-search').focus();
      }
    });
    // Links between articles, the list and the page buttons: in place.
    document.addEventListener('click', (e) => {
      const a = e.target.closest('a[data-article]');
      if (!a || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      e.preventDefault();
      open(a.getAttribute('data-article'), { push: true, anchor: a.getAttribute('data-anchor') });
    });
    // A language the download page doesn't have: the wiki switches by itself.
    const menu = $('lang');
    if (menu) {
      menu.addEventListener('click', (e) => {
        const a = e.target.closest('a[hreflang]');
        if (!a || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
        const code = a.getAttribute('hreflang');
        if (siteKnows(code)) return; // i18n.js switches the page, and with it the wiki
        e.preventDefault();
        menu.open = false;
        wikiOnly = true;
        try {
          const url = new URL(location.href);
          url.searchParams.set('lang', code);
          history.replaceState(history.state, '', url);
        } catch { /* keep the address */ }
        setLanguage(code);
      });
    }
    window.addEventListener('popstate', () => {
      const p = new URLSearchParams(location.search);
      const s = p.get('article') || WIKI.default;
      if (WIKI.articles[s]) open(s, { anchor: location.hash.slice(1) || null });
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, { once: true });
  else start();
})();
</script>
<div style="display:none" aria-hidden="true">
  <form tool="get_wiki_article" toolname="get_wiki_article" data-tool="get_wiki_article" tooldescription="Get structured content for a SpaceCorps 2027 wiki article" action="/play/wiki.json" method="GET">
    <input name="article" placeholder="article slug (e.g. protos, quests, skylab)">
    <button type="submit">Get Wiki Article</button>
  </form>
  <form tool="list_wiki_articles" toolname="list_wiki_articles" data-tool="list_wiki_articles" tooldescription="List all available SpaceCorps 2027 wiki categories and article slugs" action="/play/wiki.json" method="GET">
    <button type="submit">List Wiki Articles</button>
  </form>
</div>
</body>
</html>
"""


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
