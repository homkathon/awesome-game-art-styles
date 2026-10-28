# Stickerbook cutouts · 贴纸绘本拼贴

[← All styles](../../README.md#2d-drawn--painted)

<a href="https://store.steampowered.com/app/2322180/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2322180/ss_bb56c95322d9fbbd7ec6f6fa0354dcb34c70255b.600x338.jpg" width="100%" alt="Stickerbook cutouts: A Tiny Sticker Tale"></a>

> Simple, friendly silhouettes behave like individual stickers in a playful scrapbook world.<br>
> 简洁讨喜的轮廓像一枚枚贴纸，组成可摆弄的手账世界。

What it takes: **Mostly art.** The look lives in made material; code only supports it. You need: Sticker-shaped sprites with clean alpha silhouettes.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1172450/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1172450/ss_5e9fb66710e5b0b8912c43f56299830893435379.600x338.jpg" width="100%" alt="Carto"></a><br><sub>Carto</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/2322180/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2322180/ss_d5e9c334757d7b20d0fbcbd3346ee8a008ed0043.600x338.jpg" width="100%" alt="A Tiny Sticker Tale"></a><br><sub>A Tiny Sticker Tale</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1172450/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1172450/ss_722dc056235ac70f8cc7bacf1be895e49ed2f231.600x338.jpg" width="100%" alt="Carto"></a><br><sub>Carto</sub></td>
</tr>
</table>

## How to spot it

- Props read as individual movable stickers
- Soft outlines surround flat colours
- Layout feels like an open scrapbook

## Techniques

- masked 2D sprites
- subtle border stroke
- tile snapping

## Reference games

- [A Tiny Sticker Tale](https://store.steampowered.com/app/2322180/)
- [Carto](https://store.steampowered.com/app/1172450/)

## Similar styles

- [Storybook / picture book](../storybook/) · 绘本
- [Gouache picture book](../gouache-picture-book/) · 水粉质感绘本

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Paint each prop on a transparent sprite with an easily recognisable closed outline.
1. Apply a one-pixel CanvasItem border in Godot, plus drag-and-snap positioning for sticker-like interaction.
