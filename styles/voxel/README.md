# Voxel · 体素

[← All styles](../../README.md#3d-retro--lo-fi)

<a href="https://store.steampowered.com/app/1167630/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1167630/f266c2457a6b183a89abce8659bac7419fdfc5f0/ss_f266c2457a6b183a89abce8659bac7419fdfc5f0.600x338.jpg" width="100%" alt="Voxel: Teardown"></a>

> The world built from cubes; often destructible.<br>
> 世界由方块搭成，通常可以破坏。

What it takes: **Code only.** Simple models plus shaders and post-processing get close.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1167630/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1167630/ss_b140eeaf8e489dfa4451411ae23c28a0ecb26729.600x338.jpg" width="100%" alt="Teardown"></a><br><sub>Teardown</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1167630/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1167630/560d42a1125ebee850a1740f92f31da84c4c88e5/ss_560d42a1125ebee850a1740f92f31da84c4c88e5.600x338.jpg" width="100%" alt="Teardown"></a><br><sub>Teardown</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1167630/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1167630/ss_9a48b92d7144b7f4a27c0b5bc7dac1e687698f5b.600x338.jpg" width="100%" alt="Teardown"></a><br><sub>Teardown</sub></td>
</tr>
</table>

## How to spot it

- Everything is made of visible cubes
- Objects break apart cube by cube

## Techniques

- voxel meshing
- small-cube detail on large forms

## Reference games

- [Teardown](https://store.steampowered.com/app/1167630/)

## Similar styles

- [Low-poly](../low-poly/) · 低多边形
- [Pixelated 3D](../pixelated-3d/) · 像素化 3D

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Model in a voxel editor such as MagicaVoxel and export to OBJ / glTF.
1. Use greedy meshing so large flat areas become few triangles.
1. Keep voxel size consistent across all assets.
