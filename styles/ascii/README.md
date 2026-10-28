# ASCII / text · ASCII / 字符画

[← All styles](../../README.md#2d-graphic--print)

<a href="https://store.steampowered.com/app/603390/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/603390/ss_98312257e7a8b1ee3c8964d6dede01cf69c002f0.600x338.jpg" width="100%" alt="ASCII / text: Stone Story RPG"></a>

> The world drawn with characters.<br>
> 用字符画出整个世界。

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/603390/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/603390/ss_f47ebda50e77ea2c3fb2211620e48a9c0e93c08d.600x338.jpg" width="100%" alt="Stone Story RPG"></a><br><sub>Stone Story RPG</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/603390/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/603390/ss_6716f20985f9b95ebda494ea53ea812fdc9222f7.600x338.jpg" width="100%" alt="Stone Story RPG"></a><br><sub>Stone Story RPG</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/333640/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/333640/ss_0d7f344e2478cf941e174078297b5d2adde21567.600x338.jpg" width="100%" alt="Caves of Qud"></a><br><sub>Caves of Qud</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/333640/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/333640/ss_fc17afe945a7d81473c1b2d728aa513ff2011fc2.600x338.jpg" width="100%" alt="Caves of Qud"></a><br><sub>Caves of Qud</sub></td>
</tr>
</table>

## How to spot it

- Every image is made of text characters on a grid
- Monospace font, often few colours

## Techniques

- monospace grid
- character-based animation

## Reference games

- [Stone Story RPG](https://store.steampowered.com/app/603390/)
- [Caves of Qud](https://store.steampowered.com/app/333640/)

## Similar styles

- [1-bit / dithered](../1-bit/) · 1-bit 抖动
- [Pixel art](../pixel-art/) · 像素画

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.

1. Render to a character grid (one glyph per cell) instead of pixels.
1. Map brightness to a ramp of glyphs, or draw scenes by hand as text.
1. Animate by swapping glyphs per frame.
