#!/usr/bin/env python3
"""Generate README.md (image grid) and styles/<id>/README.md (detail pages) from tools/styles.py.

Usage: python3 tools/build.py
"""
import json
import sys
from pathlib import Path

import styles as data
import x_gallery
import x_previews

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SHOTS = json.loads((HERE / "screenshots.json").read_text())
BY_ID = {s["id"]: s for s in data.STYLES}
COLS = 4
NEEDS_LABEL = {
    "code": "**Code only.** Simple models plus shaders and post-processing get close.",
    "mixed": "**Code plus assets.** The rendering is code, but it needs suitable models, textures or sprites:",
    "art": "**Mostly art.** The look lives in made material; code only supports it. You need:",
}
REPO = "https://github.com/homkathon/awesome-opus-game-art-styles"
PAGES = "https://homkathon.github.io/awesome-opus-game-art-styles"
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
        need = data.NEEDS.get(s["id"])
        if not need or need[0] not in NEEDS_LABEL:
            errors.append(f"{s['id']}: NEEDS entry must be code, mixed or art")
        elif need[0] != "code" and not (need[1] and data.NEEDS_ZH.get(s["id"])):
            errors.append(f"{s['id']}: a {need[0]} style needs a note in NEEDS and NEEDS_ZH")
        for field, zh in (("spot", data.SPOT_ZH), ("techniques", data.TECHNIQUES_ZH), ("agent", data.AGENT_ZH)):
            if len(zh.get(s["id"], [])) != len(s[field]):
                errors.append(f"{s['id']}: {field.upper()}_ZH must have one item per {field} item")
    seen_games = set()
    for item in data.ILLUSTRATED_INSPIRATION:
        gid = item["game"]
        if gid in seen_games:
            errors.append(f"duplicate inspiration game {gid}")
        seen_games.add(gid)
        if gid not in data.GAMES:
            errors.append(f"unknown inspiration game {gid}")
        if item["style"] not in BY_ID:
            errors.append(f"unknown inspiration style {item['style']}")
        ref_gid, idx = item["image"].split(":")
        if int(ref_gid) != gid or ref_gid not in SHOTS or int(idx) >= len(SHOTS[ref_gid]):
            errors.append(f"unknown inspiration screenshot {item['image']}")
    return errors


TEXT = {
    "en": dict(
        file="README.md", resources="resources.md", sections=data.SECTIONS, name=lambda s: s["title"], sub=lambda s: s["zh"],
        switch="**English** · [简体中文](README.zh-CN.md)",
        intro="> {n} game visual styles, organised by **look**, so Claude Opus 5.5 (or any coding agent) can build your game "
        "in the style you mean instead of the same generic look. Each style has in-game screenshots, how to spot it, "
        "techniques, tutorials, free assets and step-by-step agent notes.",
        start="Start here",
        links=[
            ("🌐 Website", "[homkathon.gokoding.com/styles]({site}): search and filter every style, play the demos (Chinese UI)"),
            ("🤖 Claude Code skill", "Tell Opus 5.5: *Read {site}/install.md and install the game-art-style skill.* "
             "([source](skills/game-art-style/SKILL.md), works in Codex and Cursor too)"),
            ("▶️ Shader demos", "[Toon, PS1, 1-bit and pixelated 3D]({pages}/demos/), one commented HTML file each"),
            ("🎬 X post gallery", "[{x} creator technique posts]({pages}/x-posts/), playable and downloadable with credit"),
        ],
        note="Screenshots are hot-linked from Steam and link to each game's store page; nothing is rehosted here.",
        contents="Contents",
        star="If this list helped you pick a look, a ⭐ helps other developers find it.",
    ),
    "zh": dict(
        file="README.zh-CN.md", resources="resources.zh-CN.md", sections=data.SECTIONS_ZH, name=lambda s: s["zh"], sub=lambda s: s["title"],
        switch="[English](README.md) · **简体中文**",
        intro="> {n} 种游戏视觉风格，按**观感**分类。用 Opus 5.5（或别的编程智能体）做游戏时先挑一种，"
        "做出来才不会都长一个样。每种风格都有真实游戏截图、识别要点、实现技术、教程、免费素材和给智能体的实现步骤。",
        start="从这里开始",
        links=[
            ("🌐 中文网页版", "[homkathon.gokoding.com/styles]({site})：搜索、分类筛选，翻截图、玩在线演示"),
            ("🤖 Claude Code 技能", "对 Opus 5.5 说：*读 {site}/install.md ，按步骤安装 game-art-style 技能。*"
             "（[源码](skills/game-art-style/SKILL.md)，Codex、Cursor 也能用）"),
            ("▶️ 着色器演示", "[卡通、PS1、1-bit、像素化 3D]({pages}/demos/)，每个都是一个带注释的 HTML 文件"),
            ("🎬 X 技术帖画廊", "[{x} 条创作者技术帖]({pages}/x-posts/)，可直接播放、下载，保留作者署名"),
        ],
        note="截图直接从 Steam 加载并链接到商店页，本仓库不转存任何截图。风格详情页目前为英文。",
        contents="目录",
        star="如果这份列表帮你选定了画风，点个 ⭐ 能让更多开发者看到它。",
    ),
}


def illustrated_inspiration(lang):
    """A first-class, two-column visual gallery of all curated game examples."""
    zh = lang == "zh"
    title = "插画游戏灵感 · 16 款作品" if zh else "Illustrated game inspiration · 16 games"
    sub = ("以下都是独立的视觉案例，不是 16 种人为拆分出来的美术流派。点击图片查看 Steam 原始截图和游戏，点击风格进入实现说明。"
           if zh else "Each game has its own visual card. These are individual inspirations, not artificially renamed genres. Images open Steam; style names open implementation notes.")
    out = ['<a id="illustrated-inspiration"></a>', f"## {title}", "", sub, "", "<table>"]
    cells = []
    for item in data.ILLUSTRATED_INSPIRATION:
        gid, url = shot(item["image"])
        game = data.GAMES[item["game"]]
        sty = BY_ID[item["style"]]
        style_name = sty["zh"] if zh else sty["title"]
        note = item["note_zh"] if zh else item["note_en"]
        cells.append(
            f'<td width="50%" valign="top"><a href="{store(gid)}">'
            f'<img src="{url}" width="100%" alt="{game}: {style_name}"></a>'
            f'<br><b><a href="{store(gid)}">{game}</a></b>'
            f'<br><sub><a href="styles/{sty["id"]}/">{style_name}</a></sub>'
            f'<br><sub>{note}</sub></td>'
        )
    for i in range(0, len(cells), 2):
        out += ["<tr>", *cells[i : i + 2], "</tr>"]
    out += ["</table>", ""]
    out.append("### 插画创作者参考" if zh else "### Illustrator references")
    out.append("")
    out.append("作者作品仅供研究参考，不代表可自由复用的素材。" if zh else "For visual study only; the artists' work is not a reusable asset library.")
    out.append("")
    for artist in data.ILLUSTRATORS:
        desc = artist["zh"] if zh else artist["en"]
        out.append(f'- [{artist["name"]}]({artist["url"]}) — {desc}')
    out.append("")
    return out


def home(lang):
    t = TEXT[lang]
    resources = x_previews.decorate_readme((HERE / t["resources"]).read_text(), lang)
    x_count = len(json.loads((HERE / "x_media.json").read_text()))
    extra = [line[3:] for line in resources.splitlines() if line.startswith("## ")]
    out = [
        '<p align="center"><img src="assets/banner.png" alt="One scene in four styles: toon, PS1, 1-bit, pixelated 3D"></p>',
        "",
        "# Awesome Game Art Styles for Opus [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        f"[![Styles](https://img.shields.io/badge/styles-{len(data.STYLES)}-f2b134)](#{slug(t['sections'][0])}) "
        "[![Licence: CC0](https://img.shields.io/badge/licence-CC0-lightgrey)](LICENSE) "
        f"[![check]({REPO}/actions/workflows/check.yml/badge.svg)]({REPO}/actions/workflows/check.yml)",
        "",
        t["switch"],
        "",
        t["intro"].format(n=len(data.STYLES)),
        "",
        f"### {t['start']}",
        "",
        "| | |",
        "|:--|:--|",
        *[f"| **{k}** | {v.format(site=SITE, pages=PAGES, x=x_count)} |" for k, v in t["links"]],
        "",
        t["note"],
        "",
        f"## {t['contents']}",
        "",
        *[f"- [{sec}](#{slug(sec)})" for sec in t["sections"]],
        "- [" + ("插画游戏灵感" if lang == "zh" else "Illustrated game inspiration") + "](#illustrated-inspiration)",
        *[f"- [{sec}](#{slug(sec)})" for sec in extra],
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
    out += illustrated_inspiration(lang)
    out.append(resources)
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
        f"What it takes: {NEEDS_LABEL[data.NEEDS[s['id']][0]]} {data.NEEDS[s['id']][1]}".rstrip(),
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
        "The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. "
        "When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.",
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
    gallery_count = x_gallery.render()
    print(f"built: README.md + README.zh-CN.md + {len(data.STYLES)} style pages + {gallery_count} X embeds")


if __name__ == "__main__":
    main()
