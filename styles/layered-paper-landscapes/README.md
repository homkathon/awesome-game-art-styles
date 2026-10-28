# Layered paper landscapes · 分层纸片风景

[← All styles](../../README.md#2d-drawn--painted)

<a href="https://store.steampowered.com/app/581270/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/581270/ss_b0e4a7017f9fa3f64bb7fb953583e323389194a2.600x338.jpg" width="100%" alt="Layered paper landscapes: Old Man's Journey"></a>

> Painted hills, trees and buildings overlap like pieces of a handmade paper theatre.<br>
> 山丘、树木和建筑像纸片剧场一样层叠拼出绘画世界。

What it takes: **Mostly art.** The look lives in made material; code only supports it. You need: Painted cut-paper landscapes and matching depth-separated props.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1889740/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1889740/ss_82470980eb5d5fde9ffa0febee5892083b61f22a.600x338.jpg" width="100%" alt="Paper Trail"></a><br><sub>Paper Trail</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/581270/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/581270/ss_11406a46468e36e249a26f9054dfef162678c076.600x338.jpg" width="100%" alt="Old Man's Journey"></a><br><sub>Old Man's Journey</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1889740/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1889740/ss_a1a611020f74862495fa0777a6d5da84a0c061a2.600x338.jpg" width="100%" alt="Paper Trail"></a><br><sub>Paper Trail</sub></td>
</tr>
</table>

## How to spot it

- Terrain is made of overlapping painted silhouettes
- Soft seams and shadows separate paper planes
- Scene reads as a staged illustration

## Techniques

- layered cut-paper sprites
- soft contact shadows
- orthographic parallax

## Reference games

- [Old Man's Journey](https://store.steampowered.com/app/581270/)
- [Paper Trail](https://store.steampowered.com/app/1889740/)

## Similar styles

- [Papercraft](../papercraft/) · 纸艺
- [Storybook / picture book](../storybook/) · 绘本

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Separate terrain illustrations into several depth planes rather than a continuous realistic mesh.
1. Use Godot Parallax2D with small layer offsets and subtle shadows; keep paper grain restrained.
