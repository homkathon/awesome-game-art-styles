# 8-bit / NES · 8-bit / FC

[← All styles](../../README.md#2d-pixel)

<a href="https://store.steampowered.com/app/764790/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/764790/ss_875fe259c26f29d959efba0eca47e1b63d844c75.600x338.jpg" width="100%" alt="8-bit / NES: The Messenger"></a>

> Pixel art that follows (or pretends to follow) the NES's colour and sprite limits.<br>
> 遵守（或假装遵守）FC 颜色和精灵限制的像素画。

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/861250/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/861250/ss_a8ac9cc9a6ca8278c2af07e21ce6268bbf924a9d.600x338.jpg" width="100%" alt="Cyber Shadow"></a><br><sub>Cyber Shadow</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/861250/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/861250/ss_7fca607d9da151cf67d90f5b0bc4371829b1997e.600x338.jpg" width="100%" alt="Cyber Shadow"></a><br><sub>Cyber Shadow</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/764790/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/764790/ss_480583aad07967ee7792e15528d1493280e904b2.600x338.jpg" width="100%" alt="The Messenger"></a><br><sub>The Messenger</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/764790/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/764790/ss_105fd3de6a4dbf2cb848f2c265212ae3eb7434e5.600x338.jpg" width="100%" alt="The Messenger"></a><br><sub>The Messenger</sub></td>
</tr>
</table>

## How to spot it

- Small, flat-coloured sprites with three colours each plus transparency
- Tiles on a fixed grid, black or solid backgrounds
- No smooth gradients, no rotation

## Techniques

- NES palette (54 colours)
- 3 colours per sprite
- 8×8 or 16×16 tiles

## Reference games

- [Shovel Knight](https://store.steampowered.com/app/250760/)
- [Cyber Shadow](https://store.steampowered.com/app/861250/)
- [The Messenger](https://store.steampowered.com/app/764790/)

## Learn

- [NESdev wiki: PPU palettes](https://www.nesdev.org/wiki/PPU_palettes) · the real NES colour and sprite limits
- [Lospec palette list](https://lospec.com/palette-list) · Lospec

## Free assets to start with

- [Kenney](https://kenney.nl/assets) · CC0

Licences change; check the pack page before you ship.

## Similar styles

- [Pixel art](../pixel-art/) · 像素画
- [1-bit / dithered](../1-bit/) · 1-bit 抖动

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.

1. Restrict the palette to the NES's colours and each sprite to three colours plus transparency.
1. Build levels from 8×8 or 16×16 tiles on a strict grid; render at 256×240 and scale by whole numbers.
1. Decide which limits you break (more colours, wider screen) and break only those.
