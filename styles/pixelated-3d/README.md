# Pixelated 3D · 像素化 3D

[← All styles](../../README.md#3d-retro--lo-fi)

<a href="https://store.steampowered.com/app/1055540/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1055540/ss_f2123fea859e299736a3e99d130238c784d53e75.600x338.jpg" width="100%" alt="Pixelated 3D: A Short Hike"></a>

> A 3D world rendered at low resolution so it reads as pixel art.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1055540/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1055540/ss_0e864bf975bb71f238de6861fc8fd3d6ed6e4ce8.600x338.jpg" width="100%" alt="A Short Hike"></a><br><sub>A Short Hike</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1055540/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1055540/ss_a22817e259c4220cad0c25db315f417b6d3641b8.600x338.jpg" width="100%" alt="A Short Hike"></a><br><sub>A Short Hike</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1055540/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1055540/ss_c9c8a8e6062511c5ae9259c68c66754cd09ae971.600x338.jpg" width="100%" alt="A Short Hike"></a><br><sub>A Short Hike</sub></td>
</tr>
</table>

## How to spot it

- Looks like pixel art but the camera rotates and moves in depth
- Crisp one-pixel outlines on edges
- No shimmering when the camera pans

## Techniques

- low-res render target, nearest upscale
- pixel-snapped camera
- edge highlights

## Reference games

- [A Short Hike](https://store.steampowered.com/app/1055540/)

## Learn

- [t3ssel8r](https://www.youtube.com/@t3ssel8r) · pixel-art look in 3D

## Free assets to start with

- [KayKit](https://kaylousberg.itch.io/furniture-bits) · CC0
- [Kenney](https://kenney.nl/assets) · CC0

Licences change; check the pack page before you ship.

## Similar styles

- [Pixel art](../pixel-art/) · 像素画
- [PS1 / low-fi 3D](../ps1/) · PS1 复古 3D

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.

1. Render the 3D scene to a small viewport (e.g. 1/4–1/6 resolution) and upscale with nearest filtering (three.js: `RenderPixelatedPass`).
1. Snap the orthographic camera to whole texels and offset the final image by the remainder to stop shimmer.
1. Add one-pixel highlights where depth or normals change.
