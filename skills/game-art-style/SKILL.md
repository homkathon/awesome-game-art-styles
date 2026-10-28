---
name: game-art-style
description: Help pick a visual style for a game and gather the references, techniques and free assets to reach it. Use when someone is deciding how their game should look ("what art style", "my game looks ugly", "games that look like X", "which assets fit a cozy / retro / print look"), comparing styles, or looking for tutorials and CC0 packs for a given look. Draws on the curated list in this repository's README.md.
---

# Game art style

Help the user choose a visual style for their game and leave them with a concrete plan: style, reference games, techniques, learning resources and assets with licences.

## Where the data is

`README.md` at the repository root. Each `###` heading under a `##` section is one style, with:

- a one-line summary (Chinese name first),
- **Games**: reference games with Steam links (the images above the list are their Steam header images),
- **Techniques**: what produces the look,
- **Learn**: tutorials and talks, when there are any,
- **Assets**: free or cheap packs that fit.

The "Asset libraries" section lists licences and the date they were checked. "Wanted" lists styles that have no reference game yet.

Read the README before recommending anything. Prefer entries in the list over your own memory, and say when you go beyond it.

## Steps

1. **Ask only what changes the answer.** Skip anything the user already said or the project shows.
   - Theme and tone (cozy, satirical, eerie, heroic …).
   - 2D or 3D, and engine.
   - Who makes the art: nobody (assets only), a programmer, an artist.
   - Licence constraints (commercial, open source, competition, CC0 only).
   - Budget: free only, or paid packs allowed.
2. **Shortlist 2–3 styles.** For each: why it fits the theme in one line, two reference games from the list (with links), and the main risk or cost (e.g. "claymation needs physical models or a lot of texture work").
   With licence constraints, prefer styles whose assets are CC0, and flag anything that is not.
3. **Give the plan for the chosen style:** techniques in order of impact, learning links, asset packs with licences.
4. **Offer to apply it.** If the user has a project open, prototype the key technique (a shader, a palette, a post-process pass) on one scene. Ask before downloading any asset pack, and name the file, source and licence when asking.

## Rules

- Licences change. Quote the date from the README and tell the user to check the pack page before shipping. Never describe a custom or unclear licence as CC0.
- Link to reference games; never download or redistribute their screenshots.
- If nothing in the list fits, say so, name the closest two, and suggest adding the style to the list (CONTRIBUTING.md).
