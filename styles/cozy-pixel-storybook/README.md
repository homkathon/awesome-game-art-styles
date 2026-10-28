# Cozy storybook pixel art · 温暖绘本像素

[← All styles](../../README.md#2d-pixel)

<a href="https://store.steampowered.com/app/1062140/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1062140/ss_9d643d5db7b194146bbe2d6f233e039900e74106.600x338.jpg" width="100%" alt="Cozy storybook pixel art: Garden Story"></a>

> Friendly pixel characters and small nature scenes with muted, storybook-inspired palettes.<br>
> 保留清楚的方形像素，以温和配色、圆润轮廓与自然细节呈现绘本般的亲和力。

What it takes: **Mostly art.** The look lives in made material; code only supports it. You need: Small-scale pixel sprites, tile sets and matching foliage in a limited palette.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1594940/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1594940/ss_0569cca715dc43d7e86ae11b8b8d2c84ec4a4fd3.600x338.jpg" width="100%" alt="Little Witch in the Woods"></a><br><sub>Little Witch in the Woods</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1062140/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1062140/ss_ee75af73d8bad015cfcf86530fceb627d9e6b298.600x338.jpg" width="100%" alt="Garden Story"></a><br><sub>Garden Story</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/977880/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/977880/ss_b3512f7576dbdd1e35dd3fb27a04f29174efb00d.600x338.jpg" width="100%" alt="Eastward"></a><br><sub>Eastward</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1594940/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1594940/3d249807f69063f01d966f1817bf766aaa91f8d9/ss_3d249807f69063f01d966f1817bf766aaa91f8d9.600x338.jpg" width="100%" alt="Little Witch in the Woods"></a><br><sub>Little Witch in the Woods</sub></td>
</tr>
</table>

## How to spot it

- Visible square pixels paired with round friendly silhouettes
- Warm greens, browns and creams rather than neon colours
- Layered plants, paths and props make an inviting world

## Techniques

- limited-palette pixel tiles and sprites
- nearest-neighbour integer scaling
- layered foliage tilemaps

## Reference games

- [Garden Story](https://store.steampowered.com/app/1062140/)
- [Little Witch in the Woods](https://store.steampowered.com/app/1594940/)
- [Eastward](https://store.steampowered.com/app/977880/)

## Learn

- [Lospec palette list](https://lospec.com/palette-list) · Lospec
- [Palette-driven pixel-art lighting](https://x.com/MadeInHevinis/status/1847072515572507001) · MadeInHevinis (X technique post)

## Free assets to start with

- [LimeZu Modern Interiors](https://limezu.itch.io/moderninteriors) · paid, credit required

Licences change; check the pack page before you ship.

## Similar styles

- [Pixel art](../pixel-art/) · 像素画
- [Cozy interiors](../cozy/) · 温馨室内像素
- [Gouache picture book](../gouache-picture-book/) · 水粉质感绘本

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. In Godot, draw a 16- or 32-pixel tile grid with matching character sprites; choose 12–20 harmonious colours first.
1. Set CanvasItem texture filtering to Nearest, use integer scaling and enable snap_2d_transforms_to_pixel to avoid uneven pixels.
1. Stack foliage and props on multiple TileMapLayers, and animate characters in 4–8 distinct hand-drawn poses.
