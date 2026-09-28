#!/usr/bin/env python3
"""Programmatically fetch and build the SpaceCorps 2027 Wiki for the web.

Extracts markdown articles from the base game package (SpaceCorps2027/assets/wiki),
resolves cross-wiki links, extracts tables of contents, and generates:
1. wiki.json  (Machine-readable catalog and pre-rendered HTML for agents and tools)
2. wiki.html  (Interactive in-browser wiki matching the in-game wiki layout and design system)
3. wiki/      (Mirror of raw markdown articles for direct text/markdown content negotiation)

Usage:
    python3 scripts/build-wiki.py [PATH_TO_ASSETS_WIKI]
"""

import html
import json
import os
import re
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
PLAY_ROOT = os.path.abspath(os.path.join(HERE, ".."))

CANDIDATE_DIRS = [
    os.path.join(PLAY_ROOT, "..", "SpaceCorps2027-release", "assets", "wiki"),
    os.path.join(PLAY_ROOT, "..", "SpaceCorps2027", "assets", "wiki"),
    os.path.join(PLAY_ROOT, "..", "..", "SpaceCorps2027-release", "assets", "wiki"),
    os.path.join(PLAY_ROOT, "..", "..", "SpaceCorps2027", "assets", "wiki"),
    os.path.expanduser("~/git/spacecorps/SpaceCorps2027-release/assets/wiki"),
    os.path.expanduser("~/git/spacecorps/SpaceCorps2027/assets/wiki"),
]


def find_wiki_dir(specified=None):
    if specified and os.path.isdir(specified):
        return os.path.abspath(specified)
    for c in CANDIDATE_DIRS:
        if os.path.isdir(c):
            return os.path.abspath(c)
    raise FileNotFoundError(
        "Could not locate SpaceCorps 2027 base game assets/wiki directory. "
        "Provide path as argument: python3 scripts/build-wiki.py <path_to_assets_wiki>"
    )


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[-\s]+", "-", text)


def category_info(dir_name):
    # e.g. "01-General" -> (1, "General", "general")
    digits = "".join(c for c in dir_name if c.isdigit())
    order = int(digits) if digits else 99
    name = dir_name[len(digits) :].lstrip("-") if digits else dir_name
    name = name.replace("-", " ")
    cat_id = slugify(name)
    return order, name, cat_id


def file_slug(filename):
    stem = filename[:-3] if filename.endswith(".md") else filename
    # Drop numeric prefix if any
    stem = re.sub(r"^\d+-", "", stem)
    return slugify(stem)


def parse_markdown(md_text, link_map=None):
    lines = md_text.split("\n")
    out = []
    toc = []
    in_list = None
    in_table = False
    in_code = False
    code_block = []

    def close_list():
        nonlocal in_list
        if in_list:
            out.append(f"</{in_list}>")
            in_list = None

    def close_table():
        nonlocal in_table
        if in_table:
            out.append("</tbody></table></div>")
            in_table = False

    def format_inline(line):
        code_spans = []

        def save_code(m):
            code_spans.append(m.group(1))
            return f"__CODE_SPAN_{len(code_spans)-1}__"

        line = re.sub(r"`([^`]+)`", save_code, line)
        line = html.escape(line)

        # Bold
        line = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", line)
        # Italic
        line = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", line)

        # Links
        def replace_link(m):
            text = m.group(1)
            target = m.group(2).strip()
            # Check internal wiki link
            if link_map:
                # Handle anchor in link target e.g. /wiki/03-Mechanics/Quests.md#level-1
                target_path, sep, anchor = target.partition("#")
                target_norm = urllib.parse.unquote(target_path.strip().lstrip("/"))
                if target_norm.startswith("wiki/"):
                    target_norm = target_norm[5:]
                target_slug = link_map.get(target_norm)
                if not target_slug:
                    stem = os.path.splitext(os.path.basename(target_norm))[0]
                    target_slug = link_map.get(slugify(stem))
                if target_slug:
                    resolved = f"?article={target_slug}"
                    if anchor:
                        resolved += f"#{slugify(anchor)}"
                    return f'<a href="{resolved}" class="wiki-link" data-article="{target_slug}">{text}</a>'
            if target.startswith("http://") or target.startswith("https://"):
                return f'<a href="{target}" target="_blank" rel="noopener noreferrer">{text}</a>'
            return f'<a href="{target}">{text}</a>'

        line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", replace_link, line)

        # Restore code spans
        for i, code in enumerate(code_spans):
            line = line.replace(f"__CODE_SPAN_{i}__", f"<code>{html.escape(code)}</code>")
        return line

    for line in lines:
        stripped = line.strip()

        # Fenced code
        if stripped.startswith("```"):
            if in_code:
                out.append(f'<pre><code>{html.escape(chr(10).join(code_block))}</code></pre>')
                code_block = []
                in_code = False
            else:
                close_list()
                close_table()
                in_code = True
            continue

        if in_code:
            code_block.append(line)
            continue

        if not stripped:
            close_list()
            close_table()
            continue

        if stripped in ("---", "***"):
            close_list()
            close_table()
            out.append("<hr>")
            continue

        # Headings
        h_match = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if h_match:
            close_list()
            close_table()
            level = len(h_match.group(1))
            heading_text = h_match.group(2).strip()
            anchor = slugify(heading_text)
            if level in (2, 3):
                toc.append({"level": level, "title": heading_text, "anchor": anchor})
            out.append(f'<h{level} id="{anchor}">{format_inline(heading_text)}</h{level}>')
            continue

        # Table rows
        if stripped.startswith("|") and stripped.endswith("|"):
            close_list()
            cells = [c.strip() for c in stripped[1:-1].split("|")]
            if all(re.match(r"^:?-+:?$", c) for c in cells):
                continue
            if not in_table:
                in_table = True
                out.append('<div class="table-wrap"><table><thead><tr>')
                for c in cells:
                    out.append(f"<th>{format_inline(c)}</th>")
                out.append("</tr></thead><tbody>")
            else:
                out.append("<tr>")
                for c in cells:
                    out.append(f"<td>{format_inline(c)}</td>")
                out.append("</tr>")
            continue
        else:
            close_table()

        # Unordered list item
        ul_match = re.match(r"^[-*]\s+(.*)$", stripped)
        if ul_match:
            if in_list != "ul":
                close_list()
                out.append("<ul>")
                in_list = "ul"
            out.append(f"<li>{format_inline(ul_match.group(1))}</li>")
            continue

        # Ordered list item
        ol_match = re.match(r"^\d+\.\s+(.*)$", stripped)
        if ol_match:
            if in_list != "ol":
                close_list()
                out.append("<ol>")
                in_list = "ol"
            out.append(f"<li>{format_inline(ol_match.group(1))}</li>")
            continue

        close_list()
        out.append(f"<p>{format_inline(stripped)}</p>")

    close_list()
    close_table()
    return "\n".join(out), toc


def build_wiki():
    wiki_src = find_wiki_dir(sys.argv[1] if len(sys.argv) > 1 else None)
    print(f"Reading base game wiki from: {wiki_src}")

    categories = []
    articles = {}
    link_map = {}

    # Discover and build article links
    cat_dirs = sorted([d for d in os.listdir(wiki_src) if os.path.isdir(os.path.join(wiki_src, d))])

    # Pass 1: Count stem occurrences to detect collisions across categories
    stem_counts = {}
    for cat_dir in cat_dirs:
        cat_path = os.path.join(wiki_src, cat_dir)
        for md_file in sorted(os.listdir(cat_path)):
            if md_file.endswith(".md"):
                stem = file_slug(md_file)
                stem_counts[stem] = stem_counts.get(stem, 0) + 1

    # Pass 2: Assign unique slugs and populate comprehensive link_map
    for cat_dir in cat_dirs:
        order, cat_name, cat_id = category_info(cat_dir)
        cat_path = os.path.join(wiki_src, cat_dir)
        md_files = sorted([f for f in os.listdir(cat_path) if f.endswith(".md")])
        cat_articles = []

        for md_file in md_files:
            stem = file_slug(md_file)
            slug = f"{cat_id}-{stem}" if stem_counts[stem] > 1 else stem
            cat_articles.append({"file": md_file, "slug": slug, "stem": stem})

            raw_stem = os.path.splitext(md_file)[0]
            link_map[slug] = slug
            link_map[f"{cat_dir}/{md_file}"] = slug
            link_map[f"{cat_dir}/{raw_stem}"] = slug
            link_map[f"{cat_dir}/{stem}"] = slug
            link_map[f"{cat_id}/{stem}"] = slug
            if stem_counts[stem] == 1:
                link_map[stem] = slug
                link_map[raw_stem] = slug
                link_map[md_file] = slug

        categories.append(
            {
                "id": cat_id,
                "name": cat_name,
                "order": order,
                "dir": cat_dir,
                "article_slugs": [a["slug"] for a in cat_articles],
                "articles_meta": cat_articles,
            }
        )

    # Process each article
    wiki_mirror_dir = os.path.join(PLAY_ROOT, "wiki")
    os.makedirs(wiki_mirror_dir, exist_ok=True)

    for cat in categories:
        cat_path = os.path.join(wiki_src, cat["dir"])
        mirror_cat_dir = os.path.join(wiki_mirror_dir, cat["dir"])
        os.makedirs(mirror_cat_dir, exist_ok=True)

        for meta in cat["articles_meta"]:
            md_file = meta["file"]
            slug = meta["slug"]
            src_file = os.path.join(cat_path, md_file)
            with open(src_file, "r", encoding="utf-8") as f:
                raw_content = f.read()

            # Mirror raw markdown to play/wiki/
            dst_file = os.path.join(mirror_cat_dir, md_file)
            with open(dst_file, "w", encoding="utf-8") as f:
                f.write(raw_content)
            # Find title from first heading
            title_match = re.search(r"^#\s+(.+)$", raw_content, re.MULTILINE)
            if title_match:
                title = title_match.group(1).strip()
            else:
                title = os.path.splitext(md_file)[0].replace("-", " ")

            html_body, toc = parse_markdown(raw_content, link_map)

            word_count = len(raw_content.split())
            reading_time = max(1, round(word_count / 200))

            articles[slug] = {
                "id": slug,
                "title": title,
                "category": cat["name"],
                "categoryId": cat["id"],
                "filename": md_file,
                "path": f"{cat['dir']}/{md_file}",
                "html": html_body,
                "toc": toc,
                "wordCount": word_count,
                "readingTime": f"{reading_time} min read",
                "markdown": raw_content,
            }

    for c in categories:
        c.pop("articles_meta", None)

    # Save wiki.json
    catalog = {
        "version": "0.4.0",
        "title": "SpaceCorps 2027 Wiki & Codex",
        "description": "Comprehensive pilot manual, ship specifications, mechanics, alien encounter logs, and equipment data programmatically derived from the base game package.",
        "categories": categories,
        "articles": articles,
    }

    wiki_json_path = os.path.join(PLAY_ROOT, "wiki.json")
    with open(wiki_json_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
    print(f"Generated {wiki_json_path} ({len(articles)} articles)")

    # Build wiki.html
    generate_wiki_html(catalog)


def generate_wiki_html(catalog):
    # Pick default article
    default_slug = "getting-started" if "getting-started" in catalog["articles"] else list(catalog["articles"].keys())[0]
    default_article = catalog["articles"][default_slug]

    categories_json = json.dumps(catalog["categories"], ensure_ascii=False)
    articles_json = json.dumps(catalog["articles"], ensure_ascii=False)

    html_content = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SpaceCorps 2027 · Game Wiki &amp; Pilot Codex</title>
<meta name="description" content="Official game wiki and pilot codex for SpaceCorps 2027: ship specifications, active abilities, alien intelligence, mechanics, weapons and flight manuals.">
<meta name="color-scheme" content="dark">
<meta name="theme-color" content="#141312">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta name="bingbot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta name="is-agentic-site-type" content="content">
<meta name="author" content="SpaceCorps">
<meta name="keywords" content="SpaceCorps 2027 wiki, SpaceCorps ships, Protos, Kitefin, Wraith, Paragon, Ostirion, Skylab guide, SpaceCorps mechanics, alien guide">
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
<meta property="og:description" content="Official game wiki and pilot codex: ship specifications, mechanics, alien intelligence, weapons and flight manuals.">
<meta property="og:url" content="https://spacecorps.github.io/play/wiki.html">
<meta property="og:image" content="https://spacecorps.github.io/play/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@SpaceCorps">
<meta name="twitter:creator" content="@SpaceCorps">
<meta name="twitter:title" content="SpaceCorps 2027 · Game Wiki &amp; Pilot Codex">
<meta name="twitter:description" content="Official game wiki and pilot codex: ship specifications, mechanics, alien intelligence, weapons and flight manuals.">
<meta name="twitter:image" content="https://spacecorps.github.io/play/img/og.jpg">
<link rel="stylesheet" href="style.css">
<style>
  /* Wiki Layout & Typography */
  .wiki-container {{
    max-width: calc(var(--page) + 2 * var(--gutter));
    margin: 0 auto;
    padding: 24px var(--gutter) 80px;
  }}
  .wiki-header {{
    padding: 32px 0 24px;
    border-bottom: 1px solid var(--separator);
    margin-bottom: 28px;
    display: flex;
    flex-wrap: wrap;
    align-items: flex-end;
    justify-content: space-between;
    gap: 16px;
  }}
  .wiki-header-copy h1 {{
    font-size: clamp(28px, 4vw, 40px);
    font-weight: 700;
    letter-spacing: -0.02em;
    line-height: 1.1;
  }}
  .wiki-header-copy p {{
    color: var(--text-2);
    margin-top: 6px;
    font-size: 15px;
  }}
  .wiki-search-box {{
    position: relative;
    width: 100%;
    max-width: 320px;
  }}
  .wiki-search-input {{
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
  }}
  .wiki-search-input:focus {{
    background: var(--elevated);
    border-color: var(--accent);
    outline: none;
  }}
  .wiki-search-icon {{
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-3);
    pointer-events: none;
    width: 16px;
    height: 16px;
  }}
  .wiki-search-badge {{
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
  }}
  .wiki-layout {{
    display: grid;
    grid-template-columns: 260px minmax(0, 1fr) 220px;
    gap: 36px;
    align-items: start;
  }}
  @media (max-width: 1040px) {{
    .wiki-layout {{
      grid-template-columns: 240px minmax(0, 1fr);
    }}
    .wiki-toc-pane {{
      display: none;
    }}
  }}
  @media (max-width: 760px) {{
    .wiki-layout {{
      grid-template-columns: 1fr;
    }}
    .wiki-sidebar {{
      position: static;
      max-height: none;
      margin-bottom: 24px;
    }}
  }}

  /* Sidebar */
  .wiki-sidebar {{
    position: sticky;
    top: 80px;
    max-height: calc(100vh - 100px);
    overflow-y: auto;
    padding-right: 12px;
    scrollbar-width: thin;
    scrollbar-color: var(--separator) transparent;
  }}
  .wiki-cat-group {{
    margin-bottom: 20px;
  }}
  .wiki-cat-title {{
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-3);
    margin-bottom: 8px;
    padding-left: 10px;
  }}
  .wiki-nav-list {{
    list-style: none;
    margin: 0;
    padding: 0;
  }}
  .wiki-nav-item a {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 6px 10px;
    border-radius: var(--radius-control);
    color: var(--text-2);
    font-size: 13.5px;
    line-height: 1.35;
    transition: background 0.12s ease, color 0.12s ease;
  }}
  .wiki-nav-item a:hover {{
    color: var(--text);
    background: rgba(255, 255, 255, 0.05);
    text-decoration: none;
  }}
  .wiki-nav-item.active a {{
    color: var(--accent);
    background: var(--accent-soft);
    font-weight: 600;
  }}

  /* Center Article Pane */
  .wiki-article-card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-card);
    padding: 36px 40px;
    box-shadow: var(--shadow);
  }}
  @media (max-width: 600px) {{
    .wiki-article-card {{
      padding: 24px 20px;
    }}
  }}
  .wiki-meta-row {{
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
    font-size: 13px;
    color: var(--text-3);
  }}
  .wiki-tag {{
    background: rgba(255, 255, 255, 0.06);
    color: var(--accent);
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
    font-size: 12px;
  }}
  .wiki-article-title {{
    font-size: clamp(26px, 3.5vw, 36px);
    font-weight: 700;
    letter-spacing: -0.02em;
    line-height: 1.15;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--separator);
  }}
  .wiki-content {{
    color: var(--text);
    font-size: 15.5px;
    line-height: 1.7;
  }}
  .wiki-content p {{
    margin-bottom: 16px;
  }}
  .wiki-content h2 {{
    font-size: 22px;
    font-weight: 700;
    margin: 32px 0 14px;
    padding-bottom: 6px;
    border-bottom: 1px solid var(--separator);
  }}
  .wiki-content h3 {{
    font-size: 17px;
    font-weight: 600;
    margin: 24px 0 10px;
  }}
  .wiki-content ul, .wiki-content ol {{
    margin: 0 0 20px 24px;
    padding: 0;
  }}
  .wiki-content li {{
    margin-bottom: 6px;
  }}
  .wiki-content hr {{
    border: none;
    border-top: 1px solid var(--separator);
    margin: 28px 0;
  }}
  .wiki-content pre {{
    background: var(--elevated);
    border: 1px solid var(--border);
    border-radius: var(--radius-control);
    padding: 14px 16px;
    overflow-x: auto;
    font-size: 13.5px;
    line-height: 1.45;
    margin-bottom: 20px;
  }}
  .table-wrap {{
    width: 100%;
    overflow-x: auto;
    margin: 20px 0;
    border: 1px solid var(--border);
    border-radius: var(--radius-control);
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    text-align: left;
  }}
  th, td {{
    padding: 10px 14px;
    border-bottom: 1px solid var(--separator);
  }}
  th {{
    background: rgba(255, 255, 255, 0.04);
    font-weight: 600;
    color: var(--text-2);
  }}
  tr:last-child td {{
    border-bottom: none;
  }}
  tr:hover td {{
    background: rgba(255, 255, 255, 0.02);
  }}
  .wiki-pagination {{
    margin-top: 36px;
    padding-top: 24px;
    border-top: 1px solid var(--separator);
    display: flex;
    justify-content: space-between;
    gap: 16px;
  }}
  .wiki-page-btn {{
    display: inline-flex;
    flex-direction: column;
    padding: 10px 16px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--border);
    border-radius: var(--radius-control);
    font-size: 13px;
    color: var(--text-2);
    transition: background 0.15s ease, border-color 0.15s ease;
  }}
  .wiki-page-btn:hover {{
    background: rgba(255, 255, 255, 0.06);
    border-color: var(--accent);
    color: var(--text);
    text-decoration: none;
  }}
  .wiki-page-btn-title {{
    font-weight: 600;
    color: var(--text);
    font-size: 14px;
    margin-top: 2px;
  }}

  /* Right TOC */
  .wiki-toc-pane {{
    position: sticky;
    top: 80px;
    max-height: calc(100vh - 100px);
    overflow-y: auto;
    font-size: 13px;
  }}
  .wiki-toc-title {{
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-3);
    margin-bottom: 12px;
  }}
  .wiki-toc-list {{
    list-style: none;
    margin: 0;
    padding: 0;
    border-left: 1px solid var(--separator);
  }}
  .wiki-toc-item a {{
    display: block;
    padding: 4px 0 4px 14px;
    color: var(--text-2);
    line-height: 1.35;
    margin-left: -1px;
    border-left: 2px solid transparent;
  }}
  .wiki-toc-item a:hover {{
    color: var(--text);
    text-decoration: none;
    border-left-color: var(--text-3);
  }}
  .wiki-toc-item.level-3 a {{
    padding-left: 24px;
    font-size: 12px;
  }}
  .wiki-toc-item.active a {{
    color: var(--accent);
    border-left-color: var(--accent);
    font-weight: 600;
  }}
</style>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "SpaceCorps",
          "item": "https://spacecorps.github.io/"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "SpaceCorps 2027",
          "item": "https://spacecorps.github.io/play/"
        }},
        {{
          "@type": "ListItem",
          "position": 3,
          "name": "Wiki &amp; Pilot Codex",
          "item": "https://spacecorps.github.io/play/wiki.html"
        }}
      ]
    }},
    {{
      "@type": "TechArticle",
      "@id": "https://spacecorps.github.io/play/wiki.html#codex",
      "url": "https://spacecorps.github.io/play/wiki.html",
      "name": "SpaceCorps 2027 Game Wiki &amp; Pilot Codex",
      "headline": "SpaceCorps 2027 Game Wiki &amp; Pilot Codex",
      "description": "Comprehensive reference of ship statistics, combat mechanics, Skylab production, alien species, and equipment loadouts for SpaceCorps 2027.",
      "version": "0.4.0",
      "datePublished": "2026-09-26",
      "dateModified": "2026-09-28",
      "author": {{
        "@type": "Organization",
        "name": "SpaceCorps",
        "url": "https://spacecorps.github.io/"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "SpaceCorps",
        "url": "https://spacecorps.github.io/",
        "logo": "https://spacecorps.github.io/play/img/icon-128.png"
      }}
    }}
  ]
}}
</script>
<script>
if (typeof document !== 'undefined') {{
  const mcp = document.modelContext || (typeof navigator !== 'undefined' && navigator.modelContext);
  if (mcp && typeof mcp.registerTool === 'function') {{
    mcp.registerTool({{
      name: 'get_wiki_article',
      description: 'Get structured markdown and HTML content for a SpaceCorps 2027 wiki article by slug (e.g. "protos", "quests", "skylab").',
      inputSchema: {{ type: 'object', properties: {{ article: {{ type: 'string' }} }}, required: ['article'] }},
      execute: async ({{ article }}) => {{
        const res = await fetch('wiki.json');
        const data = await res.json();
        return data.articles[article] || {{ error: 'Not found', available: Object.keys(data.articles) }};
      }}
    }});
    mcp.registerTool({{
      name: 'list_wiki_articles',
      description: 'List all available SpaceCorps 2027 wiki categories and article slugs.',
      inputSchema: {{ type: 'object', properties: {{}} }},
      execute: async () => {{
        const res = await fetch('wiki.json');
        const data = await res.json();
        return {{ categories: data.categories, articles: Object.keys(data.articles) }};
      }}
    }});
  }}
}}
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
        <li><a href="?lang=en" hreflang="en" lang="en" aria-current="true">English<svg class="icon" aria-hidden="true"><use href="#i-check"/></svg></a></li>
        <li><a href="?lang=de" hreflang="de" lang="de">Deutsch<svg class="icon" aria-hidden="true"><use href="#i-check"/></svg></a></li>
        <li><a href="?lang=es" hreflang="es" lang="es">Español<svg class="icon" aria-hidden="true"><use href="#i-check"/></svg></a></li>
        <li><a href="?lang=fr" hreflang="fr" lang="fr">Français<svg class="icon" aria-hidden="true"><use href="#i-check"/></svg></a></li>
        <li><a href="?lang=pt-BR" hreflang="pt-BR" lang="pt-BR">Português (Brasil)<svg class="icon" aria-hidden="true"><use href="#i-check"/></svg></a></li>
        <li><a href="?lang=sv" hreflang="sv" lang="sv">Svenska<svg class="icon" aria-hidden="true"><use href="#i-check"/></svg></a></li>
        <li><a href="?lang=ru" hreflang="ru" lang="ru">Русский<svg class="icon" aria-hidden="true"><use href="#i-check"/></svg></a></li>
        <li><a href="?lang=ja" hreflang="ja" lang="ja">日本語<svg class="icon" aria-hidden="true"><use href="#i-check"/></svg></a></li>
        <li><a href="?lang=ko" hreflang="ko" lang="ko">한국어<svg class="icon" aria-hidden="true"><use href="#i-check"/></svg></a></li>
        <li><a href="?lang=zh-CN" hreflang="zh-CN" lang="zh-CN">简体中文<svg class="icon" aria-hidden="true"><use href="#i-check"/></svg></a></li>
      </ul>
    </details>
  </div>
</header>

<main class="wiki-container" id="wiki-main">
  <div class="wiki-header">
    <div class="wiki-header-copy">
      <h1>Pilot Codex &amp; Wiki</h1>
      <p>Flight systems, ship specifications, mechanics, alien encounters, and Skylab guides fetched directly from the base game package.</p>
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
      <div id="wiki-sidebar-content"></div>
    </aside>

    <!-- Center Article Reader -->
    <article class="wiki-article-card" id="wiki-article-pane">
      <div class="wiki-meta-row">
        <span class="wiki-tag" id="article-category">{default_article['category']}</span>
        <span id="article-readtime">{default_article['readingTime']}</span>
        <span>•</span>
        <span id="article-wordcount">{default_article['wordCount']} words</span>
      </div>
      <h2 class="wiki-article-title" id="article-title">{default_article['title']}</h2>
      <div class="wiki-content" id="article-body">
        {default_article['html']}
      </div>
      <div class="wiki-pagination" id="article-pagination"></div>
    </article>

    <!-- Right "On this page" TOC -->
    <aside class="wiki-toc-pane" id="wiki-toc-pane" aria-label="On this page">
      <div class="wiki-toc-title">On this page</div>
      <ul class="wiki-toc-list" id="wiki-toc-list"></ul>
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

<script>
const WIKI_DATA = {{
  categories: {categories_json},
  articles: {articles_json}
}};

let currentArticleId = "{default_slug}";

function renderSidebar(filterQuery = "") {{
  const container = document.getElementById("wiki-sidebar-content");
  const query = filterQuery.toLowerCase().trim();
  let html = "";

  WIKI_DATA.categories.forEach(cat => {{
    const matchedArticles = cat.article_slugs.filter(slug => {{
      const a = WIKI_DATA.articles[slug];
      if (!a) return false;
      if (!query) return true;
      return a.title.toLowerCase().includes(query) ||
             a.category.toLowerCase().includes(query) ||
             (a.markdown && a.markdown.toLowerCase().includes(query));
    }});

    if (matchedArticles.length === 0) return;

    html += `<div class="wiki-cat-group">`;
    html += `<div class="wiki-cat-title">${{cat.name}} (${{matchedArticles.length}})</div>`;
    html += `<ul class="wiki-nav-list">`;
    matchedArticles.forEach(slug => {{
      const a = WIKI_DATA.articles[slug];
      const isActive = slug === currentArticleId;
      html += `<li class="wiki-nav-item ${{isActive ? "active" : ""}}" data-slug="${{slug}}">`;
      html += `<a href="?article=${{slug}}" onclick="handleNavClick(event, '${{slug}}')">${{a.title}}</a>`;
      html += `</li>`;
    }});
    html += `</ul></div>`;
  }});

  if (!html) {{
    html = `<p style="padding:12px;color:var(--text-3);font-size:13px">No articles match "${{filterQuery}}"</p>`;
  }}
  container.innerHTML = html;
}}

function loadArticle(slug, pushHistory = true) {{
  const a = WIKI_DATA.articles[slug];
  if (!a) return;
  currentArticleId = slug;

  document.getElementById("article-category").textContent = a.category;
  document.getElementById("article-readtime").textContent = a.readingTime;
  document.getElementById("article-wordcount").textContent = `${{a.wordCount}} words`;
  document.getElementById("article-title").textContent = a.title;
  document.getElementById("article-body").innerHTML = a.html;
  document.title = `${{a.title}} · SpaceCorps 2027 Wiki`;

  // Render right TOC
  const tocList = document.getElementById("wiki-toc-list");
  if (a.toc && a.toc.length > 0) {{
    document.getElementById("wiki-toc-pane").style.display = "block";
    tocList.innerHTML = a.toc.map(item => `
      <li class="wiki-toc-item level-${{item.level}}">
        <a href="#${{item.anchor}}">${{item.title}}</a>
      </li>
    `).join("");
  }} else {{
    document.getElementById("wiki-toc-pane").style.display = "none";
  }}

  // Pagination (prev / next)
  const allSlugs = [];
  WIKI_DATA.categories.forEach(c => c.article_slugs.forEach(s => allSlugs.push(s)));
  const idx = allSlugs.indexOf(slug);
  const prevSlug = idx > 0 ? allSlugs[idx - 1] : null;
  const nextSlug = idx < allSlugs.length - 1 ? allSlugs[idx + 1] : null;

  let pagHtml = "";
  if (prevSlug && WIKI_DATA.articles[prevSlug]) {{
    const p = WIKI_DATA.articles[prevSlug];
    pagHtml += `<a href="?article=${{prevSlug}}" class="wiki-page-btn" onclick="handleNavClick(event, '${{prevSlug}}')">
      <span>&larr; Previous</span>
      <span class="wiki-page-btn-title">${{p.title}}</span>
    </a>`;
  }} else {{
    pagHtml += `<div></div>`;
  }}
  if (nextSlug && WIKI_DATA.articles[nextSlug]) {{
    const n = WIKI_DATA.articles[nextSlug];
    pagHtml += `<a href="?article=${{nextSlug}}" class="wiki-page-btn" style="text-align:right" onclick="handleNavClick(event, '${{nextSlug}}')">
      <span>Next &rarr;</span>
      <span class="wiki-page-btn-title">${{n.title}}</span>
    </a>`;
  }}
  document.getElementById("article-pagination").innerHTML = pagHtml;

  // Intercept internal article links in the newly rendered body
  document.querySelectorAll("#article-body a.wiki-link").forEach(link => {{
    link.addEventListener("click", (e) => {{
      const targetSlug = link.getAttribute("data-article");
      if (targetSlug && WIKI_DATA.articles[targetSlug]) {{
        e.preventDefault();
        loadArticle(targetSlug, true);
        window.scrollTo({{ top: document.getElementById("wiki-main").offsetTop - 20, behavior: "smooth" }});
      }}
    }});
  }});

  // Update active sidebar item
  document.querySelectorAll(".wiki-nav-item").forEach(el => {{
    el.classList.toggle("active", el.getAttribute("data-slug") === slug);
  }});

  if (pushHistory) {{
    history.pushState({{ article: slug }}, `${{a.title}} · SpaceCorps Wiki`, `?article=${{slug}}`);
  }}
}}

function handleNavClick(event, slug) {{
  event.preventDefault();
  loadArticle(slug, true);
  window.scrollTo({{ top: document.getElementById("wiki-main").offsetTop - 20, behavior: "smooth" }});
}}

// Initialize routing
window.addEventListener("DOMContentLoaded", () => {{
  const params = new URLSearchParams(window.location.search);
  const requested = params.get("article") || window.location.hash.replace("#", "");
  const initialSlug = (requested && WIKI_DATA.articles[requested]) ? requested : "{default_slug}";

  renderSidebar();
  loadArticle(initialSlug, false);

  // Search input handler
  const searchInput = document.getElementById("wiki-search");
  searchInput.addEventListener("input", (e) => {{
    renderSidebar(e.target.value);
  }});

  // Keyboard shortcut '/'
  window.addEventListener("keydown", (e) => {{
    if (e.key === "/" && document.activeElement !== searchInput) {{
      e.preventDefault();
      searchInput.focus();
    }}
  }});

  window.addEventListener("popstate", (e) => {{
    const params = new URLSearchParams(window.location.search);
    const slug = params.get("article") || "{default_slug}";
    if (WIKI_DATA.articles[slug]) {{
      loadArticle(slug, false);
    }}
  }});
}});
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
    wiki_html_path = os.path.join(PLAY_ROOT, "wiki.html")
    with open(wiki_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated {wiki_html_path}")


if __name__ == "__main__":
    build_wiki()
