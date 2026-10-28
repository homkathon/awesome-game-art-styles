# Toy diorama / tilt-shift · 玩具微缩景

[← All styles](../../README.md#3d-shading--form)

<a href="https://store.steampowered.com/app/1291340/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1291340/ss_989ff1808d9416c7b22da3e16ee54874697b1cea.600x338.jpg" width="100%" alt="Toy diorama / tilt-shift: Townscaper"></a>

> The world as a tabletop model: soft light, shallow depth of field, everything small and touchable.<br>
> 把世界做成桌面模型：柔光、浅景深，一切小巧得像能摸到。

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/2198150/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2198150/ss_1a98b0d5e8111f100b3ececda8f682333337e3cb.600x338.jpg" width="100%" alt="Tiny Glade"></a><br><sub>Tiny Glade</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/2198150/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2198150/ss_83248b45f1431127f94ab7bcfc246e5efb26848e.600x338.jpg" width="100%" alt="Tiny Glade"></a><br><sub>Tiny Glade</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1291340/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1291340/ss_07f2bedd6f510cb08bf5a0708e3a2e8ed299fbbd.600x338.jpg" width="100%" alt="Townscaper"></a><br><sub>Townscaper</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/427820/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/427820/ss_4a27e52bee4422a5539c63083aa256ef72f82e58.600x338.jpg" width="100%" alt="Hitman GO"></a><br><sub>Hitman GO</sub></td>
</tr>
</table>

## How to spot it

- Background and foreground are blurred as if shot with a macro lens
- Edges are rounded, materials look like painted wood or plastic
- The whole scene fits on a table

## Techniques

- bokeh depth of field
- ambient occlusion
- rounded bevels
- warm key light

## Reference games

- [Tiny Glade](https://store.steampowered.com/app/2198150/)
- [Townscaper](https://store.steampowered.com/app/1291340/)
- [Hitman GO](https://store.steampowered.com/app/427820/)

## Learn

- [Analytical ambient occlusion for mobile scenes](https://x.com/florisium/status/1975506073319567393) · Florisium (X technical thread)

## Free assets to start with

- [KayKit](https://kaylousberg.itch.io/furniture-bits) · CC0
- [Kenney](https://kenney.nl/assets) · CC0

Licences change; check the pack page before you ship.

## Similar styles

- [Minimal geometric 3D](../minimal-geometric/) · 极简几何 3D
- [Dark miniature](../dark-miniature/) · 黑暗微缩

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.

1. Add depth of field with a short focus distance; blur both near and far.
1. Enable SSAO and bevel every model edge; small rounded edges sell the toy scale.
1. Use a high camera angle and a narrow field of view, like a photo of a model.
