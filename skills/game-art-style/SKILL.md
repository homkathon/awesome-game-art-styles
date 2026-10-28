---
name: game-art-style
description: Help pick a visual style for a game and gather the references, techniques and free assets to reach it. Use when someone is deciding how their game should look ("what art style", "my game looks ugly", "games that look like X", "which assets fit a cozy / retro / print look"), comparing styles, or wants to reproduce a style (toon, PS1, 1-bit dither, pixelated 3D, watercolour …) in their engine. Draws on the Awesome Game Art Styles list in this repository.
---

# Game art style

Help the user choose a visual style for their game and leave them with a concrete plan: style, reference games, techniques, learning resources and assets with licences. Then, if they want, apply it.

## Where the data is

- `README.md`: the index. One grid per section; each cell is a style name linking to `styles/<id>/`.
- `styles/<id>/README.md`: one page per style with
  - a one-line summary and a screenshot gallery (Steam screenshots of the reference games),
  - **What it takes**: code only, code plus assets, or mostly art, and which assets to prepare,
  - **How to spot it**: what makes the look recognisable,
  - **Techniques**, **Reference games**, **Learn**, **Free assets to start with** (with licences),
  - **Similar styles**: neighbours that are easy to confuse,
  - **Agent notes**: numbered steps to reproduce the look.
- `tools/styles.py`: the same content as structured data, if that is easier to scan.
- `demos/<id>.html`: runnable three.js versions of some styles (toon, PS1, 1-bit, pixelated 3D), one file each with commented shaders. When the user's engine is three.js or WebGL, start from these; for other engines, port the shader logic.
- The "Asset libraries" table at the end of `README.md` lists licences and the date they were checked.

Read the index and the relevant style pages before recommending anything. Prefer the list over your own memory, and say when you go beyond it.

## Steps

1. **Ask only what changes the answer.** Skip anything the user already said or the project shows.
   - Theme and tone (cozy, satirical, eerie, heroic …).
   - 2D or 3D, and engine.
   - Who makes the art: nobody (assets only), a programmer, an artist.
   - Licence constraints (commercial, open source, competition, CC0 only).
   - Budget: free only, or paid packs allowed.
2. **Shortlist 2–3 styles.** For each: why it fits the theme in one line, a link to its style page, two reference games, and the main risk or cost, taken from the page's **What it takes** line (e.g. "claymation needs physical models or a lot of texture work"). When nobody on the team makes art, lead with code-only styles, or say exactly which assets a style needs and where free ones are. Mention a "Similar style" when the user's description sits between two.
   With licence constraints, prefer styles whose assets are CC0, and flag anything that is not.
3. **Give the plan for the chosen style:** techniques in order of impact, learning links, asset packs with licences.
4. **Offer to apply it.** If the user has a project open, follow the style page's **Agent notes** on one scene first, adapted to their engine. Then screenshot the scene, put it next to the gallery screenshots and compare values first, then palette, then detail; fix the biggest gap before changing more, and show the user the comparison. In a post-processing pass, check that colour is converted to the display colour space exactly once; a missing conversion makes everything dark. Ask before downloading any asset pack, and name the file, source and licence when asking.

## Rules

- Licences change. Quote the checked date and tell the user to check the pack page before shipping. Never describe a custom or unclear licence as CC0.
- Link to reference games; never download or redistribute their screenshots.
- If nothing in the list fits, say so, name the closest two, and suggest adding the style (CONTRIBUTING.md).
