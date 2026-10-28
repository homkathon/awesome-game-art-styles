# Cozy low-resolution 3D nature · 低分辨率自然微缩景

[← All styles](../../README.md#3d-retro--lo-fi)

<a href="https://store.steampowered.com/app/1055540/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1055540/ss_0e864bf975bb71f238de6861fc8fd3d6ed6e4ce8.600x338.jpg" width="100%" alt="Cozy low-resolution 3D nature: A Short Hike"></a>

> Low-detail outdoor 3D forms become friendly miniature worlds through soft pixel-scale filtering.<br>
> 低细节的 3D 户外场景透过柔和像素尺度，变成亲切的微缩世界。

What it takes: **Code plus assets.** The rendering is code, but it needs suitable models, textures or sprites: Rounded simple 3D vegetation models and a consistent soft palette.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1586800/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1586800/ss_d3ee72455db9006d13b564f3811f21c03bc99cc2.600x338.jpg" width="100%" alt="Lil Gator Game"></a><br><sub>Lil Gator Game</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1740300/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1740300/ss_6869370198d9472c43b1822e0a21451288980657.600x338.jpg" width="100%" alt="Smushi Come Home"></a><br><sub>Smushi Come Home</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1055540/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1055540/ss_a22817e259c4220cad0c25db315f417b6d3641b8.600x338.jpg" width="100%" alt="A Short Hike"></a><br><sub>A Short Hike</sub></td>
</tr>
</table>

## How to spot it

- Soft low-poly nature meshes
- A pixel-soft image without harsh retro distortion
- Friendly small characters in pastel outdoor spaces

## Techniques

- simple low-poly nature props
- low-resolution render target
- soft fog

## Reference games

- [A Short Hike](https://store.steampowered.com/app/1055540/)
- [Lil Gator Game](https://store.steampowered.com/app/1586800/)
- [Smushi Come Home](https://store.steampowered.com/app/1740300/)

## Similar styles

- [Pixelated 3D](../pixelated-3d/) · 像素化 3D
- [Low-poly](../low-poly/) · 低多边形
- [Toy diorama / tilt-shift](../toy-diorama/) · 玩具微缩景

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Block out rounded low-poly trees, ground and rocks with large readable silhouettes.
1. Render via a smaller Godot SubViewport, upscale carefully and snap camera movement to reduce pixel shimmer.
