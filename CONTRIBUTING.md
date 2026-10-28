# Contributing

Additions and corrections are welcome.

`README.md` and `styles/*/README.md` are generated. Edit `tools/styles.py` (styles) or `tools/resources.md` (asset libraries, learning resources, related lists, wanted), then run:

```bash
python3 tools/build.py
```

Commit the generated files with your change. No dependencies beyond Python 3.

## Adding a style

A style earns an entry when it is a recognisable look that more than one team could adopt, not a single game's identity.

1. Add the reference games to `GAMES` in `tools/styles.py` (Steam app id → name).
2. Run `python3 tools/fetch_screenshots.py` to cache their screenshot URLs in `tools/screenshots.json`.
3. Add a `dict(...)` to `STYLES`:
   - `hero`: the screenshot shown in the grid, as `"APPID:INDEX"` into `screenshots.json`. **Pick an in-game screenshot that shows the style most clearly**, not a title card, logo or menu.
   - `gallery`: 2–4 more screenshots, ideally from more than one game.
   - `spot`: what makes the look recognisable at a glance.
   - `techniques`, `learn`, `assets`, `similar` (ids of neighbouring styles).
   - `agent`: numbered steps to reproduce the look in an engine; concrete enough for a coding agent to follow.
4. `python3 tools/build.py` validates references and regenerates the pages.

Styles without a good reference game go under **Wanted** in `tools/resources.md`.

## Adding a resource

- Asset libraries: state the licence and cost. If the licence is not CC0 or is unclear, say so.
- Learning resources: tutorials, talks and breakdowns that teach a technique, not showcases.

## Rules

- Never commit screenshots of commercial games into this repository. Link to them (Steam-hosted URLs are fine).
- Keep descriptions short and neutral. No affiliate links.
