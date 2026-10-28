# Contributing

Additions and corrections are welcome. Open a pull request that edits `README.md`.

## Adding a style

A style earns its own entry when it is a recognisable look that more than one team could adopt, not a single game's identity.

Each style is one row in its section's table, and its name is added to that section's line in **Contents**:

```html
<tr>
<td width="380"><a href="https://store.steampowered.com/app/APPID/"><img src="SCREENSHOT_URL" width="360" alt="Style: Game"></a></td>
<td><h3>Style name</h3>中文名<br><br>What it looks like, in one sentence.<br><br>🎮 <a href="https://store.steampowered.com/app/APPID/">Game</a>, <a href="…">Another game</a></td>
<td width="300">• technique<br>• technique<br><br><b>Start with:</b> <a href="…">tutorial or asset pack</a></td>
</tr>
```

- **The image is an in-game screenshot, not key art or a logo.** Pick the one that shows the style most clearly. Get the URL from `https://store.steampowered.com/api/appdetails?appids=APPID&filters=screenshots` (`path_thumbnail`, drop the `?t=` query).
- For a game that is not on Steam, link its official page and use a screenshot from its official press kit.
- Link one to three reference games.

Styles without a reference game go under **Wanted**.

## Adding a resource

- Asset libraries: state the licence and cost. If the licence is not CC0 or is unclear, say so.
- Learning resources: tutorials, talks and breakdowns that teach a technique, not showcases.

## Rules

- Never commit screenshots of commercial games into this repository. Link to them.
- Keep descriptions short and neutral. No affiliate links.
