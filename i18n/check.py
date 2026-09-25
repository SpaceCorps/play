#!/usr/bin/env python3
"""Checks the page's translations: python3 i18n/check.py (from the repository root or anywhere).

- every language of i18n.js has i18n/<code>.json, an hreflang alternate and a menu link in
  index.html, and nothing else is there;
- each translation has exactly English's keys (notes starting with @ aside), the same
  {placeholders}, only <strong>, <em> and <code> (balanced), the plural forms its language
  needs, and keeps the glossary names (docs/LOCALIZATION.md in the game repository);
- French puts a no-break space (U+00A0) before : ; ? ! and inside « »;
- index.html's English (the no-JavaScript fallback) is exactly en.json's, every key it uses
  exists, and every English key is used by index.html, app.js or i18n.js.

Exit status 1 on any problem.
"""

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"
SOURCE = "en"
GLOSSARY = ["SpaceCorps", "Thulium", "Skylab", "Chrono-Gate", "P.E.T."]
# CLDR cardinal plural categories the page's languages use for whole numbers.
PLURALS = {
    "en": {"one", "other"}, "de": {"one", "other"}, "es": {"one", "other"},
    "fr": {"one", "other"}, "pt-BR": {"one", "other"}, "sv": {"one", "other"},
    "ru": {"one", "few", "many", "other"},
    "ja": {"other"}, "ko": {"other"}, "zh-CN": {"other"},
}
OPTIONAL_PLURALS = {"es": {"many"}, "fr": {"many"}, "pt-BR": {"many"}}
PLACEHOLDER = re.compile(r"\{([\w-]+)\}")
TAG = re.compile(r"</?([a-zA-Z][\w-]*)[^>]*>")
ALLOWED_TAGS = {"strong", "em", "code"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
ATTRIBUTES = {"data-i18n-alt": "alt", "data-i18n-title": "title", "data-i18n-aria-label": "aria-label", "data-i18n-content": "content"}

problems = []


def problem(where, message):
    problems.append(f"{where}: {message}")


def messages(dict_):
    return {k: v for k, v in dict_.items() if not k.startswith("@")}


def forms(value):
    return list(value.values()) if isinstance(value, dict) else [value]


def placeholders(value):
    names = set()
    for text in forms(value):
        names |= set(PLACEHOLDER.findall(text))
    return names


def check_markup(where, text):
    stack = []
    for m in TAG.finditer(text):
        name = m.group(1).lower()
        if name not in ALLOWED_TAGS or m.group(0) not in (f"<{name}>", f"</{name}>"):
            problem(where, f"markup {m.group(0)!r}: only <strong>, <em> and <code>, without attributes")
            continue
        if m.group(0).startswith("</"):
            if not stack or stack.pop() != name:
                problem(where, f"unbalanced {m.group(0)}")
        else:
            stack.append(name)
    if stack:
        problem(where, f"unclosed <{stack[-1]}>")


def languages_in_js():
    js = (ROOT / "i18n.js").read_text(encoding="utf-8")
    block = js[js.index("const LANGUAGES"):js.index("];", js.index("const LANGUAGES"))]
    return re.findall(r"code: '([\w-]+)'", block)


class Page(HTMLParser):
    """Collects the keyed elements of index.html with their English as a message: text, the
    allowed markup, and {slot} for data-slot children."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []  # [tag, attrs, parts or None]
        self.texts = []  # (key, english, args, line)
        self.attrs = []  # (key, english, args, line)
        self.hreflang = []
        self.menu = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        line = self.getpos()[0]
        if tag == "link" and a.get("rel") == "alternate" and "hreflang" in a:
            self.hreflang.append((a["hreflang"], a.get("href", "")))
        if tag == "a" and "hreflang" in a:
            self.menu.append((a["hreflang"], a.get("href", ""), a.get("lang")))
        args = json.loads(a["data-i18n-args"]) if "data-i18n-args" in a else None
        for attr, target in ATTRIBUTES.items():
            if attr in a:
                self.attrs.append((a[attr], a.get(target, ""), args, line))
        parent = self.collecting()
        if parent is not None:
            if "data-slot" in a:
                parent.append("{" + a["data-slot"] + "}")
            elif tag in ALLOWED_TAGS:
                parent.append(f"<{tag}>")
            else:
                problem(f"index.html:{line}", f"<{tag}> inside a data-i18n element (only strong, em, code and data-slot)")
        if tag in VOID:
            return
        if "data-i18n" in a and parent is None:
            self.stack.append([tag, a, [], line])
        else:
            self.stack.append([tag, a, None, line])

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        while self.stack:
            open_tag, a, parts, line = self.stack.pop()
            if parts is not None:
                args = json.loads(a["data-i18n-args"]) if "data-i18n-args" in a else None
                self.texts.append((a["data-i18n"], "".join(parts), args, line))
            elif self.collecting() is not None and "data-slot" not in a and open_tag in ALLOWED_TAGS:
                self.collecting().append(f"</{open_tag}>")
            if open_tag == tag:
                break

    def handle_data(self, data):
        parent = self.collecting()
        if parent is not None:
            parent.append(data)

    def collecting(self):
        """The parts list of the keyed element being read, unless inside one of its slots."""
        for tag, a, parts, line in reversed(self.stack):
            if "data-slot" in a:
                return None
            if parts is not None:
                return parts
        return None


def normalize(text):
    return re.sub(r"\s+", " ", text).strip()


def fill(text, args):
    if not args:
        return text
    return PLACEHOLDER.sub(lambda m: str(args.get(m.group(1), m.group(0))), text)


def main():
    codes = languages_in_js()
    files = sorted(p.stem for p in I18N.glob("*.json"))
    if sorted(codes) != files:
        problem("i18n/", f"files {files} but i18n.js has {codes}")
    if SOURCE not in files:
        problem("i18n/", "no en.json")
        return

    dicts = {}
    for code in files:
        try:
            dicts[code] = json.loads((I18N / f"{code}.json").read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as err:
            problem(f"i18n/{code}.json", f"doesn't parse: {err}")
    en = messages(dicts.get(SOURCE, {}))

    for key, value in en.items():
        where = f"en.json {key}"
        if isinstance(value, dict):
            if not PLURALS[SOURCE] <= set(value) or not set(value) <= PLURALS[SOURCE]:
                problem(where, f"plural forms {sorted(value)}, English needs {sorted(PLURALS[SOURCE])}")
        elif not isinstance(value, str):
            problem(where, "neither text nor plural forms")
            continue
        for text in forms(value):
            check_markup(where, text)

    for code, dict_ in dicts.items():
        if code == SOURCE:
            continue
        tr = messages(dict_)
        for key in sorted(set(en) - set(tr)):
            problem(f"{code}.json", f"missing {key}")
        for key in sorted(set(tr) - set(en)):
            problem(f"{code}.json", f"{key} is not an English key")
        for key in sorted(set(en) & set(tr)):
            value, source = tr[key], en[key]
            where = f"{code}.json {key}"
            if isinstance(value, dict):
                need = PLURALS.get(code, {"other"})
                have = set(value)
                if not need <= have:
                    problem(where, f"plural forms {sorted(have)}, {code} needs {sorted(need)}")
                extra = have - need - OPTIONAL_PLURALS.get(code, set())
                if extra:
                    problem(where, f"plural forms {sorted(extra)} that {code} doesn't use")
            elif not isinstance(value, str):
                problem(where, "neither text nor plural forms")
                continue
            elif isinstance(source, dict):
                problem(where, "English has plural forms here")
            for text in forms(value):
                if not text.strip():
                    problem(where, "empty")
                check_markup(where, text)
                if PLACEHOLDER.findall(text) and set(PLACEHOLDER.findall(text)) != placeholders(source):
                    problem(where, f"placeholders {sorted(set(PLACEHOLDER.findall(text)))}, English has {sorted(placeholders(source))}")
                elif not PLACEHOLDER.findall(text) and placeholders(source):
                    problem(where, f"lost the placeholders {sorted(placeholders(source))}")
                for name in GLOSSARY:
                    if any(name in s for s in forms(source)) and name not in text:
                        problem(where, f"lost the name {name} (glossary: never translated)")
                if code == "fr":
                    plain = TAG.sub("", text)
                    if re.search(r"[ ][:;?!»]", plain) or re.search(r"«[ ]", plain):
                        problem(where, "a plain space before : ; ? ! » or after «: use \\u00a0")
                    if re.search(r"\w[:;?!]", plain.replace("://", "")) and "{" not in plain:
                        problem(where, "no space before : ; ? !: use \\u00a0")

    # index.html
    page = Page()
    page.feed((ROOT / "index.html").read_text(encoding="utf-8"))
    used = set()
    for key, english, args, line in page.texts + page.attrs:
        used.add(key)
        where = f"index.html:{line} {key}"
        if key not in en:
            problem(where, "not in en.json")
            continue
        want = en[key] if isinstance(en[key], str) else en[key].get("other", "")
        if normalize(english) != normalize(fill(want, args)) and normalize(english) != normalize(want):
            problem(where, f"English in the page {normalize(english)!r} differs from en.json {normalize(fill(want, args))!r}")

    alternates = dict(page.hreflang)
    if set(alternates) != set(codes) | {"x-default"}:
        problem("index.html", f"hreflang alternates {sorted(alternates)}, languages {codes} + x-default")
    for code in codes:
        if code in alternates and not alternates[code].endswith(f"?lang={code}"):
            problem("index.html", f"hreflang {code} points at {alternates[code]}")
    menu = {code: (href, lang) for code, href, lang in page.menu}
    if list(menu) != codes:
        problem("index.html", f"language menu {list(menu)}, i18n.js {codes} (same order)")
    for code, (href, lang) in menu.items():
        if href != f"?lang={code}" or lang != code:
            problem("index.html", f"menu link {code}: href {href}, lang {lang}")

    code_text = (ROOT / "app.js").read_text(encoding="utf-8") + (ROOT / "i18n.js").read_text(encoding="utf-8")
    for key in en:
        if key not in used and f"'{key}'" not in code_text:
            problem("en.json", f"{key} is used by neither index.html nor app.js / i18n.js")
    for key in re.findall(r"""\bt\('([\w.-]+)'|plural\('([\w.-]+)'|: '((?:status|hero|download|help|copy)\.[\w.-]+)'""", code_text):
        key = next(k for k in key if k)
        if key not in en:
            problem("app.js / i18n.js", f"{key} is not in en.json")


main()
for p in problems:
    print(p)
if problems:
    print(f"\n{len(problems)} problem(s)")
    sys.exit(1)
print(f"i18n: {len(messages(json.loads((I18N / 'en.json').read_text(encoding='utf-8'))))} messages, all languages complete")
