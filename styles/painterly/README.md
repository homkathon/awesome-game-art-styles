# Painterly · 油画感

[← All styles](../../README.md#3d-shading--form)

<a href="https://store.steampowered.com/app/632470/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/632470/ss_b3694e99ffdb686d1bbbbe16a540d3d2ccd509c4.600x338.jpg" width="100%" alt="Painterly: Disco Elysium"></a>

> Visible brush strokes, painted textures and skies; light as a painter would place it.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1172620/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1172620/ss_ec623c77d75dfa098c622b547b1ab21ad4cae0a8.600x338.jpg" width="100%" alt="Sea of Thieves"></a><br><sub>Sea of Thieves</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1172620/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1172620/ss_6ea04bdc415c336a195555aec4b97a73a9910fc1.600x338.jpg" width="100%" alt="Sea of Thieves"></a><br><sub>Sea of Thieves</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1172620/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1172620/ss_2144ac860fd64d82cb9cc49680f5087c7bb8fe2f.600x338.jpg" width="100%" alt="Sea of Thieves"></a><br><sub>Sea of Thieves</sub></td>
</tr>
</table>

## How to spot it

- Textures and skies show brush marks
- Light is stylised, often warmer and more dramatic than real
- Edges are soft and broken, not crisp

## Techniques

- hand-painted textures
- brush-stroke post filters
- painted backdrops

## Reference games

- [Disco Elysium](https://store.steampowered.com/app/632470/)
- [Sea of Thieves](https://store.steampowered.com/app/1172620/)

## Similar styles

- [Watercolour](../watercolour/) · 水彩
- [Painted comic](../painted-comic/) · 彩绘漫画

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.

1. Paint lighting into albedo textures; keep real-time lighting simple.
1. Use a Kuwahara or brush-stroke post filter to break up edges.
1. Paint skies and distant backdrops as 2D cards.
