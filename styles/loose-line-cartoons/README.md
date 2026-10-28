# Loose-line storybook cartoons · 松弛线稿卡通

[← All styles](../../README.md#2d-drawn--painted)

<a href="https://store.steampowered.com/app/1444300/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1444300/ss_93c9da1b8b189e06cf3c3c8f7f549546895b8cda.600x338.jpg" width="100%" alt="Loose-line storybook cartoons: Teacup"></a>

> Uneven friendly pen lines and large, flat colour areas avoid polished vector perfection.<br>
> 不规整的亲切墨线搭配平涂色块，避免过分精致的矢量感。

What it takes: **Mostly art.** The look lives in made material; code only supports it. You need: Original hand-inked poses with separate flat-colour layers.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1123450/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1123450/ss_1f16a64698124ab065ed1fdd7cc0ea23511f3791.600x338.jpg" width="100%" alt="Chicory: A Colorful Tale"></a><br><sub>Chicory: A Colorful Tale</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1444300/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1444300/ss_e263d1a6b57d3b8d72253ca90a8c01635e9bb810.600x338.jpg" width="100%" alt="Teacup"></a><br><sub>Teacup</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/530320/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/530320/ss_1ccb5bdd2cfc8ffce9af0b9c1ea7d4f5a63bdfb6.600x338.jpg" width="100%" alt="Wandersong"></a><br><sub>Wandersong</sub></td>
</tr>
</table>

## How to spot it

- Subtle changes in outline weight
- Simple faces and exaggerated tiny proportions
- Uncluttered coloured backgrounds

## Techniques

- variable-width ink strokes
- flat fills beneath line art
- limited 2D poses

## Reference games

- [Teacup](https://store.steampowered.com/app/1444300/)
- [Chicory: A Colorful Tale](https://store.steampowered.com/app/1123450/)
- [Wandersong](https://store.steampowered.com/app/530320/)

## Similar styles

- [Line art / colouring book](../line-art/) · 线稿 / 涂色书
- [Whimsical monochrome ink](../whimsical-ink/) · 俏皮黑白手绘

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Paint outline and colour as separate layers, keeping gentle pen wobble and rounded strokes.
1. Use unlit CanvasItem sprites in Godot and animate a few drawn key poses rather than smooth vector rigs.
