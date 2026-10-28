# Illustrated paper puzzles · 纸面插画解谜

[← All styles](../../README.md#2d-graphic--print)

<a href="https://store.steampowered.com/app/1172450/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1172450/ss_85d60c053d7f16b03d3378e4466be3bdbdcea692.600x338.jpg" width="100%" alt="Illustrated paper puzzles: Carto"></a>

> Moveable maps and folded paper panels combine flat illustration with tactile puzzle surfaces.<br>
> 可移动地图与折叠纸页，将平面插画和可操作纸面结合起来。

What it takes: **Code plus assets.** The rendering is code, but it needs suitable models, textures or sprites: Illustrated maps, paper panel textures and foldable surfaces.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1889740/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1889740/ss_1469a801a268e771e65b1c58f2930a9b33614e5d.600x338.jpg" width="100%" alt="Paper Trail"></a><br><sub>Paper Trail</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1172450/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1172450/ss_5e9fb66710e5b0b8912c43f56299830893435379.600x338.jpg" width="100%" alt="Carto"></a><br><sub>Carto</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1889740/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1889740/ss_a1a611020f74862495fa0777a6d5da84a0c061a2.600x338.jpg" width="100%" alt="Paper Trail"></a><br><sub>Paper Trail</sub></td>
</tr>
</table>

## How to spot it

- World is framed as a map or foldable sheet
- Flat symbols and simple fields of colour
- Moving paper edges is central to the experience

## Techniques

- illustrated map tiles
- page folds and pivot transforms
- paper edge shading

## Reference games

- [Carto](https://store.steampowered.com/app/1172450/)
- [Paper Trail](https://store.steampowered.com/app/1889740/)

## Similar styles

- [Papercraft](../papercraft/) · 纸艺
- [Stickerbook cutouts](../stickerbook-cutouts/) · 贴纸绘本拼贴
- [Layered paper landscapes](../layered-paper-landscapes/) · 分层纸片风景

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Draw locations as separate illustration tiles with consistent borders and scene perspective.
1. In Godot rotate Node2D map pieces or pivot flat MeshInstance3D planes for folds; add subtle contact shadows and paper grain.
