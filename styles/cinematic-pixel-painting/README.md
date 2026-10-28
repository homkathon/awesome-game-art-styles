# Cinematic pixel painting · 电影感像素绘景

[← All styles](../../README.md#2d-pixel)

<a href="https://store.steampowered.com/app/977880/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/977880/ss_b3512f7576dbdd1e35dd3fb27a04f29174efb00d.600x338.jpg" width="100%" alt="Cinematic pixel painting: Eastward"></a>

> Detailed pixel scenery and atmospheric light make environments feel like painted film frames.<br>
> 细密像素绘景加上氛围光照，让环境像动画电影的镜头。

What it takes: **Mostly art.** The look lives in made material; code only supports it. You need: Original detailed pixel environments and matching sprite sheets.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1594940/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1594940/623dea3c94ca66719a29abd1919e7547a5cbec3d/ss_623dea3c94ca66719a29abd1919e7547a5cbec3d.600x338.jpg" width="100%" alt="Little Witch in the Woods"></a><br><sub>Little Witch in the Woods</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/977880/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/977880/ss_2c7516dbcfba035a359a2eb7257356809a3f5eaa.600x338.jpg" width="100%" alt="Eastward"></a><br><sub>Eastward</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1055540/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1055540/ss_a22817e259c4220cad0c25db315f417b6d3641b8.600x338.jpg" width="100%" alt="A Short Hike"></a><br><sub>A Short Hike</sub></td>
</tr>
</table>

## How to spot it

- Environment pixels are dense and carefully shaded
- Layered atmospheric light conveys depth
- Shots have strong widescreen composition

## Techniques

- hand-pixelled environments
- palette-based light
- parallax camera

## Reference games

- [Eastward](https://store.steampowered.com/app/977880/)
- [Little Witch in the Woods](https://store.steampowered.com/app/1594940/)
- [A Short Hike](https://store.steampowered.com/app/1055540/)

## Similar styles

- [Pixel anime / cyberpunk](../pixel-anime/) · 像素动漫 / 赛博朋克
- [Cozy storybook pixel art](../cozy-pixel-storybook/) · 温暖绘本像素
- [HD-2D](../hd-2d/) · HD-2D

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Create background and foreground tiles at a fixed pixel scale and author distinct local colour palettes.
1. Use Nearest-filtered Godot sprites, low-resolution light overlays and slow camera parallax to preserve pixel clarity.
