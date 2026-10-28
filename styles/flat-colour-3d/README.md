# Flat-colour graphic 3D · 平涂图形化 3D

[← All styles](../../README.md#3d-shading--form)

<a href="https://store.steampowered.com/app/383870/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/383870/ss_80432f2d4f4192017115c23e7dff090df95b204a.600x338.jpg" width="100%" alt="Flat-colour graphic 3D: Firewatch"></a>

> Large flat colour shapes, graphic silhouettes, colour-coded atmosphere.<br>
> 大块平涂色、图形化的剪影，用颜色区分氛围。

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/383870/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/383870/ss_c7e16bc8d5a6d40ab1f7c339395d26d8f6eb57ff.600x338.jpg" width="100%" alt="Firewatch"></a><br><sub>Firewatch</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/383870/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/383870/ss_eb64648f294463df89e55f9363cdf159aebcf11e.600x338.jpg" width="100%" alt="Firewatch"></a><br><sub>Firewatch</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/231200/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/231200/ss_86f61b9478c321fd10ab4b8a75c92111138da563.600x338.jpg" width="100%" alt="Kentucky Route Zero"></a><br><sub>Kentucky Route Zero</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/231200/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/231200/ss_55f0b4aab1ddce50a64a702edc845d0679fce824.600x338.jpg" width="100%" alt="Kentucky Route Zero"></a><br><sub>Kentucky Route Zero</sub></td>
</tr>
</table>

## How to spot it

- Distant shapes fade into flat bands of one colour
- Each scene has a strong dominant colour
- Few textures; shape and colour do the work

## Techniques

- gradient fog by distance
- flat unlit materials
- strong colour scripts

## Reference games

- [Firewatch](https://store.steampowered.com/app/383870/)
- [Kentucky Route Zero](https://store.steampowered.com/app/231200/)

## Learn

- [Gerstner-wave ocean](https://x.com/Cyanilux/status/1581210772352290818) · Cyanilux (X technique post)

## Similar styles

- [Ligne claire / Moebius](../ligne-claire/) · 清线 / 墨比斯
- [Low-poly](../low-poly/) · 低多边形

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.

1. Use a fog colour gradient (near → far) as the main lighting tool.
1. Keep materials untextured or with very subtle noise.
1. Write a colour script: one key colour per scene, everything else near it.
