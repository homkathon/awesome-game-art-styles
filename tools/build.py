#!/usr/bin/env python3
"""Generate README.md (image grid) and styles/<id>/README.md (detail pages) from tools/styles.py.

Usage: python3 tools/build.py
"""
import json
import sys
from pathlib import Path

import styles as data

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SHOTS = json.loads((HERE / "screenshots.json").read_text())
BY_ID = {s["id"]: s for s in data.STYLES}
COLS = 4


def store(gid):
    return f"https://store.steampowered.com/app/{gid}/"


def shot(ref):
    gid, idx = ref.split(":")
    return gid, SHOTS[gid][int(idx)]


def slug(text):
    return "".join(c for c in text.lower().replace(" ", "-") if c.isalnum() or c == "-")


def validate():
    errors = []
    for s in data.STYLES:
        for ref in [s["hero"], *s["gallery"]]:
            gid, idx = ref.split(":")
            if int(gid) not in s["games"]:
                errors.append(f"{s['id']}: screenshot {ref} is not from one of its games")
            elif gid not in SHOTS or int(idx) >= len(SHOTS[gid]):
                errors.append(f"{s['id']}: no cached screenshot {ref}; run tools/fetch_screenshots.py")
        for k in s["learn"]:
            if k not in data.LEARN:
                errors.append(f"{s['id']}: unknown learn key {k}")
        for k in s["assets"]:
            if k not in data.ASSETS:
                errors.append(f"{s['id']}: unknown asset key {k}")
        for k in s["similar"]:
            if k not in BY_ID:
                errors.append(f"{s['id']}: unknown similar style {k}")
    return errors


def home():
    out = [
        "# Awesome Game Art Styles [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        f"> {len(data.STYLES)} game visual styles, organised by **look**. Click a style for screenshots, how to recognise it, "
        "techniques, tutorials, free assets and notes for coding agents.",
        "",
        "Screenshots are loaded from Steam and link to each game's store page; nothing is rehosted here. "
        "Use the [Claude Code skill](skills/game-art-style/SKILL.md) to get a style recommendation for your own game.",
        "",
        "## Contents",
        "",
        *[f"- [{sec}](#{slug(sec)})" for sec in data.SECTIONS],
        "- [Asset libraries](#asset-libraries)",
        "- [Learning resources](#learning-resources)",
        "- [Related lists](#related-lists)",
        "- [Wanted](#wanted)",
        "",
    ]
    for si, sec in enumerate(data.SECTIONS):
        group = [s for s in data.STYLES if s["section"] == si]
        out += [f"## {sec}", "", "<table>"]
        for i in range(0, len(group), COLS):
            out.append("<tr>")
            for s in group[i : i + COLS]:
                _, url = shot(s["hero"])
                link = f"styles/{s['id']}/"
                out.append(
                    f'<td align="center" valign="top" width="25%"><a href="{link}"><img src="{url}" width="220" alt="{s["title"]}"></a>'
                    f'<br><a href="{link}"><b>{s["title"]}</b></a><br><sub>{s["zh"]}</sub></td>'
                )
            out.append("</tr>")
        out += ["</table>", ""]
    out.append((HERE / "resources.md").read_text())
    return "\n".join(out)


def page(s):
    gid, hero = shot(s["hero"])
    out = [
        f"# {s['title']} · {s['zh']}",
        "",
        f"[← All styles](../../README.md#{slug(data.SECTIONS[s['section']])})",
        "",
        f'<a href="{store(gid)}"><img src="{hero}" width="100%" alt="{s["title"]}: {data.GAMES[int(gid)]}"></a>',
        "",
        f"> {s['summary']}",
        "",
        "## Gallery",
        "",
        "<table>",
    ]
    cells = []
    for ref in s["gallery"]:
        g, url = shot(ref)
        cells.append(
            f'<td width="50%"><a href="{store(g)}"><img src="{url}" width="100%" alt="{data.GAMES[int(g)]}"></a>'
            f'<br><sub>{data.GAMES[int(g)]}</sub></td>'
        )
    for i in range(0, len(cells), 2):
        out += ["<tr>", *cells[i : i + 2], "</tr>"]
    out += ["</table>", "", "## How to spot it", "", *[f"- {x}" for x in s["spot"]], ""]
    out += ["## Techniques", "", *[f"- {x}" for x in s["techniques"]], ""]
    out += ["## Reference games", "", *[f"- [{data.GAMES[g]}]({store(g)})" for g in s["games"]], ""]
    if s["learn"]:
        out += ["## Learn", ""]
        out += [f"- [{t}]({u}) · {who}" for t, u, who in (data.LEARN[k] for k in s["learn"])]
        out.append("")
    if s["assets"]:
        out += ["## Free assets to start with", ""]
        out += [f"- [{n}]({u}) · {lic}" for n, u, lic in (data.ASSETS[k] for k in s["assets"])]
        out += ["", "Licences change; check the pack page before you ship.", ""]
    if s["similar"]:
        out += ["## Similar styles", ""]
        out += [f"- [{BY_ID[k]['title']}](../{k}/) · {BY_ID[k]['zh']}" for k in s["similar"]]
        out.append("")
    out += [
        "## Agent notes",
        "",
        "Steps a coding agent (or you) can follow to reproduce the look. "
        "The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.",
        "",
        *[f"1. {x}" for x in s["agent"]],
        "",
    ]
    return "\n".join(out)


def main():
    errors = validate()
    for e in errors:
        print("error:", e, file=sys.stderr)
    if errors:
        sys.exit(1)
    (ROOT / "README.md").write_text(home())
    for s in data.STYLES:
        d = ROOT / "styles" / s["id"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "README.md").write_text(page(s))
    print(f"built: README.md + {len(data.STYLES)} style pages")


if __name__ == "__main__":
    main()
