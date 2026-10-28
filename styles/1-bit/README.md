# 1-bit / dithered · 1-bit 抖动

[← All styles](../../README.md#3d-retro--lo-fi)

<a href="https://store.steampowered.com/app/653530/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/653530/ss_380dc35237fde7d3863a44270abafc37924d1db4.600x338.jpg" width="100%" alt="1-bit / dithered: Return of the Obra Dinn"></a>

> Two colours and a dither pattern stand in for every tone.<br>
> 只有两种颜色，所有明暗都靠抖动图案表现。

▶ **[Live demo](https://s1ntoneli.github.io/awesome-game-art-styles/demos/1-bit.html)** · runs in the browser, [source](../../demos/1-bit.html) is one HTML file with commented shaders

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/653530/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/653530/ss_4f555f01fa82723c28fcce8f0909570caaee8e8f.600x338.jpg" width="100%" alt="Return of the Obra Dinn"></a><br><sub>Return of the Obra Dinn</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/913740/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/913740/ss_26f4f9ee59f216ec84d3c9c901743c175ba3a9c3.600x338.jpg" width="100%" alt="WORLD OF HORROR"></a><br><sub>WORLD OF HORROR</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/913740/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/913740/ss_182efb540ac2dfc7775e46809635fe174786535f.600x338.jpg" width="100%" alt="WORLD OF HORROR"></a><br><sub>WORLD OF HORROR</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/913740/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/913740/ss_81fafaf88eb23865b3488d6275ada2d3cc9e70c7.600x338.jpg" width="100%" alt="WORLD OF HORROR"></a><br><sub>WORLD OF HORROR</sub></td>
</tr>
</table>

## How to spot it

- Only two colours on screen
- Grey tones are made of dot patterns
- Patterns stay still when the camera moves

## Techniques

- ordered / blue-noise dithering
- stable dither in screen space

## Reference games

- [Return of the Obra Dinn](https://store.steampowered.com/app/653530/)
- [WORLD OF HORROR](https://store.steampowered.com/app/913740/)

## Learn

- [Obra Dinn devlog: dithering](https://forums.tigsource.com/index.php?topic=40832.msg1363742#msg1363742) · Lucas Pope
- [Acerola](https://www.youtube.com/@Acerola_t) · stylised rendering deep dives

## Similar styles

- [Silhouette noir](../silhouette/) · 剪影黑白
- [ASCII / text](../ascii/) · ASCII / 字符画

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.

1. Render in greyscale, then threshold against a Bayer or blue-noise matrix in a post pass.
1. Anchor the dither pattern to the world or camera rotation so it doesn't crawl when the view moves.
1. Draw edges first; dithered images need strong outlines to stay readable.
