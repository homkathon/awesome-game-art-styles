# Stained glass · 彩色玻璃

[← All styles](../../README.md#2d-graphic--print)

<a href="https://store.steampowered.com/app/1034150/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1034150/ss_bf7d6fdf910f95c39d3fda401ba0c57840849586.600x338.jpg" width="100%" alt="Stained glass: Mosaic Chronicles"></a>

> Illustrations assembled from coloured glass panes separated by dark lead lines.<br>
> 以深色铅条分隔透光的彩色玻璃块，再拼成完整插画。

What it takes: **Code plus assets.** The rendering is code, but it needs suitable models, textures or sprites: Closed coloured pane silhouettes, a subtle glass-grain texture and thick lead outlines.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/511470/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/511470/ss_fd980552210f5e66870ed3a63ff6fa799f2dae4d.600x338.jpg" width="100%" alt="Glass Masquerade"></a><br><sub>Glass Masquerade</sub></td>
</tr>
</table>

## How to spot it

- Every coloured shape has a dark, closed outline like a lead came
- Jewel-toned panes form a larger picture from small irregular pieces
- Light and subtle glass grain make the colours feel translucent

## Techniques

- closed pane masks and thick lead contours
- translucent colour layers
- fine glass grain and backlight glow

## Reference games

- [Mosaic Chronicles](https://store.steampowered.com/app/1034150/)
- [Glass Masquerade](https://store.steampowered.com/app/511470/)

## Learn

- [Stained glass and volumetric rays](https://x.com/Cyanilux/status/1407727586986311687) · Cyanilux (X technique post)

## Similar styles

- [Flat vector minimal](../flat-vector/) · 扁平极简矢量
- [Medieval manuscript / woodcut](../manuscript/) · 中世纪手抄本 / 木刻

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. In Godot 4, draw each pane as a `Polygon2D` and trace its closed perimeter with a dark `Line2D` (4–8 px) for the lead seams.
1. Give each polygon a single saturated fill; overlay a low-opacity noise texture in a `canvas_item` shader to suggest uneven glass.
1. Put a soft warm light layer behind the artwork and enable `WorldEnvironment` glow on the brightest panes; keep the outlines opaque.
