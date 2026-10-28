# Anime cel 2.5D · 日式赛璐璐 2.5D

[← All styles](../../README.md#3d-shading--form)

<a href="https://store.steampowered.com/app/1384160/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1384160/ss_104e16788c2ea35e1dac31d96be8d4f1df00f330.600x338.jpg" width="100%" alt="Anime cel 2.5D: GUILTY GEAR -STRIVE-"></a>

> 3D characters that read as hand-drawn animation: authored normals, held frames, no interpolation.<br>
> 3D 角色看起来像手绘动画：手调法线、定格帧、不做插值。

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1384160/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1384160/ss_0f29aebacb81b972782382dbf4c0079f0d37b330.600x338.jpg" width="100%" alt="GUILTY GEAR -STRIVE-"></a><br><sub>GUILTY GEAR -STRIVE-</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1384160/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1384160/ss_2561a4ae822856797b5fb231502b820a962336e0.600x338.jpg" width="100%" alt="GUILTY GEAR -STRIVE-"></a><br><sub>GUILTY GEAR -STRIVE-</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1384160/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1384160/ss_c290682ecdf413e368d9a66cd4a7a9430860ca1d.600x338.jpg" width="100%" alt="GUILTY GEAR -STRIVE-"></a><br><sub>GUILTY GEAR -STRIVE-</sub></td>
</tr>
</table>

## How to spot it

- Looks like a 2D anime frame until the camera moves
- Animation snaps between poses instead of easing
- Face shadows are clean shapes, not physically correct

## Techniques

- hand-edited normals for clean shadows
- limited animation (stepped keys)
- per-shot light direction

## Reference games

- [GUILTY GEAR -STRIVE-](https://store.steampowered.com/app/1384160/)

## Learn

- [GuiltyGearXrd's Art Style: The X Factor Between 2D and 3D](https://www.youtube.com/watch?v=yhGjCzxJV3E) · GDC
- [Magic sword slash VFX](https://x.com/Cyanilux/status/1467533351091376136) · Cyanilux (X technique post)

## Similar styles

- [Cel-shaded / toon](../toon/) · 卡通渲染
- [Hand-drawn animation](../hand-drawn/) · 手绘动画

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.

1. Start from a toon shader with a single hard shadow band.
1. Edit vertex normals on faces (or use a normal-transfer from a sphere) so shadows form clean shapes.
1. Bake animation at 12 fps or less with constant interpolation; keep the camera smooth.
