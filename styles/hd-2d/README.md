# HD-2D · HD-2D

[← All styles](../../README.md#2d-pixel)

<a href="https://store.steampowered.com/app/921570/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/921570/ss_d9c13a8f046e48ae57a2f2d6d134850410fe4932.600x338.jpg" width="100%" alt="HD-2D: Octopath Traveler"></a>

> Pixel sprites in a lit 3D world with depth of field and particles.<br>
> 像素精灵放进有光照的 3D 世界，加景深和粒子。

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/921570/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/921570/ss_ce917ab0bc7a665ee24cc05fa42d7c3901196265.600x338.jpg" width="100%" alt="Octopath Traveler"></a><br><sub>Octopath Traveler</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/921570/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/921570/ss_3484779b5058b6bfac043604c2c831c522435c45.600x338.jpg" width="100%" alt="Octopath Traveler"></a><br><sub>Octopath Traveler</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/977880/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/977880/ss_5d50545b49db3a8502666b4195d2fabd0e31a29d.600x338.jpg" width="100%" alt="Eastward"></a><br><sub>Eastward</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/977880/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/977880/ss_2c7516dbcfba035a359a2eb7257356809a3f5eaa.600x338.jpg" width="100%" alt="Eastward"></a><br><sub>Eastward</sub></td>
</tr>
</table>

## How to spot it

- Pixel-art characters standing in a 3D diorama
- Strong depth-of-field blur top and bottom
- Modern lighting, bloom and particles

## Techniques

- sprites as billboards
- tilt-shift depth of field
- dynamic lights on pixel art

## Reference games

- [Octopath Traveler](https://store.steampowered.com/app/921570/)
- [Eastward](https://store.steampowered.com/app/977880/)

## Learn

- [2.5D water with sprite reflections](https://x.com/Cyanilux/status/1770095395848237506) · Cyanilux (X technique post)

## Similar styles

- [Pixel art](../pixel-art/) · 像素画
- [Toy diorama / tilt-shift](../toy-diorama/) · 玩具微缩景

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.

1. Place pixel sprites as billboards (or Sprite3D) in a 3D scene built from pixel-textured meshes.
1. Add tilt-shift depth of field and bloom.
1. Give sprites normal maps so dynamic lights shade them.
