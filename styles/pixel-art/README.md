# Pixel art · 像素画

[← All styles](../../README.md#2d-pixel)

<a href="https://store.steampowered.com/app/250760/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/250760/ss_019205f5f9ae1c3f0d5359e967135a76ae1ebd2d.600x338.jpg" width="100%" alt="Pixel art: Shovel Knight"></a>

> Hand-placed pixels with limited palettes.<br>
> 手工摆放的像素，有限的调色板。

What it takes: **Mostly art.** The look lives in made material; code only supports it. You need: Sprites and tiles drawn in a fixed palette, or a CC0 pixel-art pack.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/504230/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/504230/ss_1ad297c2044cdcf450ee83e56350cafb590da755.600x338.jpg" width="100%" alt="Celeste"></a><br><sub>Celeste</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/504230/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/504230/ss_4b0f0222341b64a37114033aca9994551f27c161.600x338.jpg" width="100%" alt="Celeste"></a><br><sub>Celeste</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/250760/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/250760/ss_d4a97787fdb4f0c6bdc0826fcbb7319f74fffc6c.600x338.jpg" width="100%" alt="Shovel Knight"></a><br><sub>Shovel Knight</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/413150/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/413150/ss_b887651a93b0525739049eb4194f633de2df75be.600x338.jpg" width="100%" alt="Stardew Valley"></a><br><sub>Stardew Valley</sub></td>
</tr>
</table>

## How to spot it

- Visible square pixels at integer scale
- A small, deliberate colour palette
- Animation in a few frames

## Techniques

- limited palette
- sub-pixel animation
- integer scaling

## Reference games

- [Shovel Knight](https://store.steampowered.com/app/250760/)
- [Celeste](https://store.steampowered.com/app/504230/)
- [Stardew Valley](https://store.steampowered.com/app/413150/)

## Learn

- [Lospec palette list](https://lospec.com/palette-list) · Lospec

## Free assets to start with

- [LimeZu Modern Interiors](https://limezu.itch.io/moderninteriors) · paid, credit required
- [Kenney](https://kenney.nl/assets) · CC0

Licences change; check the pack page before you ship.

## Similar styles

- [HD-2D](../hd-2d/) · HD-2D
- [Cozy interiors](../cozy/) · 温馨室内像素

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Pick a base resolution (e.g. 320×180 or 480×270) and scale only by integers.
1. Choose a palette from Lospec and stick to it.
1. Disable texture filtering and snap sprites to whole pixels (Godot: `snap_2d_transforms_to_pixel`).
