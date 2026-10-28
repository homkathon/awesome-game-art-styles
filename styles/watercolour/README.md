# Watercolour · 水彩

[← All styles](../../README.md#2d-drawn--painted)

<a href="https://store.steampowered.com/app/1272840/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1272840/ss_0d2bac05234a73ac1cc9dbcbee31e6774e8846df.600x338.jpg" width="100%" alt="Watercolour: Dordogne"></a>

> Pigment washes, soft edges, paper texture.<br>
> 颜料晕染、柔和边缘、纸张纹理。

What it takes: **Mostly art.** The look lives in made material; code only supports it. You need: Textures and backdrops painted in transparent washes.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1272840/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1272840/ss_d1dbc0d779db775671116d7ee7e8e4a930275f5b.600x338.jpg" width="100%" alt="Dordogne"></a><br><sub>Dordogne</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1272840/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1272840/ss_309cb4ce395696af6ec48224b66a1d0df8e8fa1a.600x338.jpg" width="100%" alt="Dordogne"></a><br><sub>Dordogne</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/683320/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/683320/ss_a155ad5423e11e3e764a1a270dcf4f30323f0a35.600x338.jpg" width="100%" alt="GRIS"></a><br><sub>GRIS</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/683320/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/683320/ss_62883bfa8a341db3f9c5c03768f5c14f938fe8fc.600x338.jpg" width="100%" alt="GRIS"></a><br><sub>GRIS</sub></td>
</tr>
</table>

## How to spot it

- Colour pools and darkens at the edges of shapes
- White paper shows through
- Soft, bleeding transitions

## Techniques

- edge darkening
- pigment granulation
- paper texture overlay

## Reference games

- [Dordogne](https://store.steampowered.com/app/1272840/)
- [GRIS](https://store.steampowered.com/app/683320/)

## Free assets to start with

- [ambientCG](https://ambientcg.com) · CC0

Licences change; check the pack page before you ship.

## Similar styles

- [Ink wash / sumi-e](../ink-wash/) · 水墨
- [Painterly](../painterly/) · 油画感

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Start from painted art: paint textures and backdrops in transparent washes (or generate them with an image model) and keep 3D lighting soft and low-contrast. A post filter on an ordinary 3D render reads as a filtered render, not watercolour.
1. Keep values light: leave the paper white in highlights and build colour in a few transparent layers.
1. Darken colour near edges (from a blurred mask or depth edges).
1. Multiply a paper texture over everything and let it show in light areas.
1. Add granulation noise and slight colour bleed across edges.
