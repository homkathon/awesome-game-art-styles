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
PAGES = "https://homkathon.github.io/awesome-game-art-styles"
SITE = "https://homkathon.gokoding.com/styles"


def store(gid):
    return f"https://store.steampowered.com/app/{gid}/"


def shot(ref):
    gid, idx = ref.split(":")
    return gid, SHOTS[gid][int(idx)]


def slug(text):
    return "".join(c for c in text.lower().replace(" ", "-") if c.isalnum() or c == "-")


def validate():
    errors = []
    if len(data.SECTIONS_ZH) != len(data.SECTIONS):
        errors.append("SECTIONS_ZH must have one entry per section")
    for s in data.STYLES:
        if s["id"] not in data.SUMMARY_ZH:
            errors.append(f"{s['id']}: missing SUMMARY_ZH entry")
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


TEXT = {
    "en": dict(
        file="README.md", resources="resources.md", sections=data.SECTIONS, name=lambda s: s["title"], sub=lambda s: s["zh"],
        switch="**English** · [简体中文](README.zh-CN.md)",
        intro="> {n} game visual styles, organised by **look**. Click a style for screenshots, how to recognise it, "
        "techniques, tutorials, free assets and notes for coding agents.",
        site="🌐 **Browse it as a website: [homkathon.gokoding.com/styles]({site})** (Chinese interface). Search and filter all styles, flip through "
        "screenshots and play the live demos on each style's page.",
        body="Screenshots are loaded from Steam and link to each game's store page; nothing is rehosted here. "
        "Use the [Claude Code skill](skills/game-art-style/SKILL.md) to get a style recommendation for your own game "
        "(to install it, ask your coding agent to read [{site}/install.md]({site}/install.md)), "
        "or try the [live shader demos]({pages}/demos/) for toon, PS1, 1-bit and pixelated 3D.",
        contents="Contents",
        extra=["- [Asset libraries](#asset-libraries)", "- [Learning resources](#learning-resources)",
               "- [Related lists](#related-lists)", "- [Wanted](#wanted)"],
        star="If this list helped you pick a look, a ⭐ helps other developers find it.",
    ),
    "zh": dict(
        file="README.zh-CN.md", resources="resources.zh-CN.md", sections=data.SECTIONS_ZH, name=lambda s: s["zh"], sub=lambda s: s["title"],
        switch="[English](README.md) · **简体中文**",
        intro="> {n} 种游戏视觉风格，按**观感**分类。点进每种风格可以看截图、识别要点、实现技术、教程、免费素材，以及给编程智能体的实现步骤。",
        site="🌐 **中文网页版：[homkathon.gokoding.com/styles]({site})**。可以搜索、按分类筛选，在每种风格的页面里翻截图、直接玩在线演示。",
        body="截图直接从 Steam 加载并链接到游戏商店页，本仓库不转存任何截图。"
        "用 [Claude Code 技能](skills/game-art-style/SKILL.md)可以为你的游戏推荐风格（安装方法：让你的编程智能体读 [{site}/install.md]({site}/install.md)），"
        "也可以打开[在线着色器演示]({pages}/demos/)看卡通、PS1、1-bit 和像素化 3D 的实时效果。风格详情页目前为英文。",
        contents="目录",
        extra=["- [素材库](#素材库)", "- [学习资源](#学习资源)"],
        star="如果这份列表帮你选定了画风，点个 ⭐ 能让更多开发者看到它。",
    ),
}


def home(lang):
    t = TEXT[lang]
    out = [
        '<p align="center"><img src="assets/banner.png" alt="One scene in four styles: toon, PS1, 1-bit, pixelated 3D"></p>',
        "",
        "# Awesome Game Art Styles [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        f"[![Styles](https://img.shields.io/badge/styles-{len(data.STYLES)}-f2b134)](#{slug(t['sections'][0])}) "
        "[![Licence: CC0](https://img.shields.io/badge/licence-CC0-lightgrey)](LICENSE) "
        "[![check](https://github.com/homkathon/awesome-game-art-styles/actions/workflows/check.yml/badge.svg)]"
        "(https://github.com/homkathon/awesome-game-art-styles/actions/workflows/check.yml)",
        "",
        t["switch"],
        "",
        t["intro"].format(n=len(data.STYLES)),
        "",
        t["site"].format(site=SITE),
        "",
        t["body"].format(pages=PAGES, site=SITE),
        "",
        f"## {t['contents']}",
        "",
        *[f"- [{sec}](#{slug(sec)})" for sec in t["sections"]],
        *t["extra"],
        "",
    ]
    for si, sec in enumerate(t["sections"]):
        group = [s for s in data.STYLES if s["section"] == si]
        out += [f"## {sec}", "", "<table>"]
        for i in range(0, len(group), COLS):
            out.append("<tr>")
            for s in group[i : i + COLS]:
                _, url = shot(s["hero"])
                link = f"styles/{s['id']}/"
                out.append(
                    f'<td align="center" valign="top" width="25%"><a href="{link}"><img src="{url}" width="220" alt="{s["title"]}"></a>'
                    f'<br><a href="{link}"><b>{t["name"](s)}</b></a><br><sub>{t["sub"](s)}</sub></td>'
                )
            out.append("</tr>")
        out += ["</table>", ""]
    out.append((HERE / t["resources"]).read_text())
    out += ["", "---", "", t["star"], ""]
    return "\n".join(out)


def demo(s):
    """Link to the runnable demo, if demos/<id>.html exists."""
    if not (ROOT / "demos" / f"{s['id']}.html").exists():
        return []
    return [f"▶ **[Live demo]({PAGES}/demos/{s['id']}.html)** · runs in the browser, "
            f"[source](../../demos/{s['id']}.html) is one HTML file with commented shaders", ""]


def page(s):
    gid, hero = shot(s["hero"])
    out = [
        f"# {s['title']} · {s['zh']}",
        "",
        f"[← All styles](../../README.md#{slug(data.SECTIONS[s['section']])})",
        "",
        f'<a href="{store(gid)}"><img src="{hero}" width="100%" alt="{s["title"]}: {data.GAMES[int(gid)]}"></a>',
        "",
        f"> {s['summary']}<br>",
        f"> {data.SUMMARY_ZH[s['id']]}",
        "",
        *demo(s),
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
    for lang in TEXT:
        (ROOT / TEXT[lang]["file"]).write_text(home(lang))
    for s in data.STYLES:
        d = ROOT / "styles" / s["id"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "README.md").write_text(page(s))
    print(f"built: README.md + README.zh-CN.md + {len(data.STYLES)} style pages")


if __name__ == "__main__":
    main()
