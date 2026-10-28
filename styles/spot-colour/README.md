# Monochrome + one colour · 单色 + 强调色

[← All styles](../../README.md#light--silhouette)

<a href="https://store.steampowered.com/app/322500/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/322500/ss_1e3ef7d9d9654c6189e6680502a0ce3068d1aef7.600x338.jpg" width="100%" alt="Monochrome + one colour: SUPERHOT"></a>

> A white, grey or black world with one colour reserved for what matters.<br>
> 白、灰或黑的世界，只留一种颜色给重要的东西。

What it takes: **Code only.** Simple models plus shaders and post-processing get close.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/322500/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/322500/ss_98b769b11caf672fda92891b325c9a3525bff2d7.600x338.jpg" width="100%" alt="SUPERHOT"></a><br><sub>SUPERHOT</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/322500/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/322500/ss_f027e1abfd94f4f84f9a0c7520a8238a5533b59b.600x338.jpg" width="100%" alt="SUPERHOT"></a><br><sub>SUPERHOT</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1233570/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1233570/ss_2dc81dfd38eac438c9ed16b3c716bdab1ac201d7.600x338.jpg" width="100%" alt="Mirror's Edge Catalyst"></a><br><sub>Mirror's Edge Catalyst</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1233570/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1233570/ss_09ac42923a444f9220fd62b44992e66c88d55da0.600x338.jpg" width="100%" alt="Mirror's Edge Catalyst"></a><br><sub>Mirror's Edge Catalyst</sub></td>
</tr>
</table>

## How to spot it

- Almost everything is white, grey or black
- One saturated colour marks enemies, routes or goals
- Clean surfaces, few textures

## Techniques

- desaturated or untextured environment
- single accent colour for gameplay
- strong ambient occlusion

## Reference games

- [SUPERHOT](https://store.steampowered.com/app/322500/)
- [Mirror's Edge Catalyst](https://store.steampowered.com/app/1233570/)

## Free assets to start with

- [Kenney](https://kenney.nl/assets) · CC0

Licences change; check the pack page before you ship.

## Similar styles

- [Minimal geometric 3D](../minimal-geometric/) · 极简几何 3D
- [Silhouette noir](../silhouette/) · 剪影黑白

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Make every environment material white or light grey; let ambient occlusion and shadows show form.
1. Pick one accent colour and use it only for things the player must notice.
1. Check readability by squinting at a greyscale screenshot: only the accent should pop.
