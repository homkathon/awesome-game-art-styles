# PS1 / low-fi 3D · PS1 复古 3D

[← All styles](../../README.md#3d-retro--lo-fi)

<a href="https://store.steampowered.com/app/519860/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/519860/ss_b2668c79d271be9b62a988682e30683ac8e5f410.600x338.jpg" width="100%" alt="PS1 / low-fi 3D: DUSK"></a>

> Wobbly vertices, warped textures, tiny resolution, dithered colour.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/519860/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/519860/ss_1ed571301ad0b5f952fc4e793d7357084405c467.600x338.jpg" width="100%" alt="DUSK"></a><br><sub>DUSK</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/519860/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/519860/ss_e2f865387e9e82dbb80be51a58ab7473d825be6f.600x338.jpg" width="100%" alt="DUSK"></a><br><sub>DUSK</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1262350/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1262350/ss_a2603694154878b8260c1dd498a06168cad012a4.600x338.jpg" width="100%" alt="SIGNALIS"></a><br><sub>SIGNALIS</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1262350/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1262350/ss_bb676746c44db01c2bd7ca78616032984f958106.600x338.jpg" width="100%" alt="SIGNALIS"></a><br><sub>SIGNALIS</sub></td>
</tr>
</table>

## How to spot it

- Vertices jitter as the camera moves
- Textures swim and warp across large polygons
- Low resolution and visible colour banding or dither

## Techniques

- vertex snapping
- affine texture mapping
- low-res render target
- colour dithering

## Reference games

- [DUSK](https://store.steampowered.com/app/519860/)
- [SIGNALIS](https://store.steampowered.com/app/1262350/)

## Learn

- [Godot Shaders](https://godotshaders.com) · community shader library

## Free assets to start with

- [Kenney](https://kenney.nl/assets) · CC0

Licences change; check the pack page before you ship.

## Similar styles

- [Pixelated 3D](../pixelated-3d/) · 像素化 3D
- [1-bit / dithered](../1-bit/) · 1-bit 抖动

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.

1. Snap clip-space vertex positions to a coarse grid in the vertex shader.
1. Imitate affine mapping by multiplying UVs by w in the vertex shader and dividing in the fragment shader.
1. Render to a 320×240-ish target with nearest filtering, then dither to 15-bit colour.
