# Low-poly · 低多边形

[← All styles](../../README.md#3d-shading--form)

<a href="https://store.steampowered.com/app/553420/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/553420/ss_9c0184ba83022786f74f4a70ebae5c47d2a3c35c.600x338.jpg" width="100%" alt="Low-poly: TUNIC"></a>

> Few, visible facets; colour carried by flat gradients or vertex colours rather than textures.<br>
> 面数少、棱面可见；颜色靠平涂渐变或顶点色，而不是贴图。

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/553420/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/553420/ss_04ac7db623d3e88751134eb87f5c465c392fa108.600x338.jpg" width="100%" alt="TUNIC"></a><br><sub>TUNIC</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/553420/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/553420/ss_cce46eba03270e47fab2f955ec148c43f71fdb49.600x338.jpg" width="100%" alt="TUNIC"></a><br><sub>TUNIC</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1562430/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1562430/ss_70f88014423ed93eaa111c0d0daca2c500f76908.600x338.jpg" width="100%" alt="DREDGE"></a><br><sub>DREDGE</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1562430/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1562430/ss_9529104cde1af2ffbb715cab42bbb3012fb9b7d8.600x338.jpg" width="100%" alt="DREDGE"></a><br><sub>DREDGE</sub></td>
</tr>
</table>

## How to spot it

- You can count the polygons on a rock or a tree
- No surface texture: each face is one colour or a smooth gradient
- Depth comes from fog and colour, not detail

## Techniques

- flat or gradient-atlas colours
- faceted (flat-shaded) normals
- strong distance fog

## Reference games

- [TUNIC](https://store.steampowered.com/app/553420/)
- [DREDGE](https://store.steampowered.com/app/1562430/)

## Free assets to start with

- [KayKit](https://kaylousberg.itch.io/furniture-bits) · CC0
- [Kenney](https://kenney.nl/assets) · CC0
- [Quaternius](https://quaternius.itch.io) · custom licence
- [Poly Pizza](https://poly.pizza) · CC0 / CC-BY

Licences change; check the pack page before you ship.

## Similar styles

- [Toy diorama / tilt-shift](../toy-diorama/) · 玩具微缩景
- [Voxel](../voxel/) · 体素

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.

1. Use flat shading (Godot: `flat_shading` on the material or split vertices; three.js: `flatShading: true`).
1. Colour models from a small gradient atlas instead of unique textures, so the palette can be changed in one image.
1. Add exponential fog tinted to the sky colour; it does most of the depth work.
