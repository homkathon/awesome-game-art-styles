# Neon abstract · 霓虹抽象

[← All styles](../../README.md#light--silhouette)

<a href="https://store.steampowered.com/app/1122720/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1122720/ss_03804e3335afd5edddceafe722ff1c4eb3c19931.600x338.jpg" width="100%" alt="Neon abstract: Sayonara Wild Hearts"></a>

> Pure colour, light trails and geometry in motion; often rhythm-led.<br>
> 纯色、光轨和运动中的几何体；常以节奏驱动。

What it takes: **Code only.** Simple models plus shaders and post-processing get close.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1122720/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1122720/ss_78e2f5e6afa93bfcea8bbe587487ae4bc0c50e6e.600x338.jpg" width="100%" alt="Sayonara Wild Hearts"></a><br><sub>Sayonara Wild Hearts</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/356400/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/356400/ss_26cfa006225969a9fde35b60687d588eea40948b.600x338.jpg" width="100%" alt="Thumper"></a><br><sub>Thumper</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/356400/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/356400/ss_1913cc1bf6abe7c757343362cecbd27f36a27e7b.600x338.jpg" width="100%" alt="Thumper"></a><br><sub>Thumper</sub></td>
</tr>
</table>

## How to spot it

- Glowing colour on dark backgrounds
- Abstract shapes and light trails instead of realistic scenery
- Effects pulse with the music

## Techniques

- emissive materials and bloom
- chromatic aberration
- music-synced effects

## Reference games

- [Sayonara Wild Hearts](https://store.steampowered.com/app/1122720/)
- [Thumper](https://store.steampowered.com/app/356400/)

## Similar styles

- [Neon 80s pixel](../neon-80s/) · 80 年代霓虹像素
- [Flat vector minimal](../flat-vector/) · 扁平极简矢量

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Use emissive materials and strong bloom on a near-black background.
1. Limit the palette to two or three hues (magenta, cyan, gold).
1. Drive scale, colour and camera shake from the beat clock.
