# Gouache picture book · 水粉质感绘本

[← All styles](../../README.md#2d-drawn--painted)

<a href="https://store.steampowered.com/app/1172450/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1172450/ss_5e9fb66710e5b0b8912c43f56299830893435379.600x338.jpg" width="100%" alt="Gouache picture book: Carto"></a>

> Opaque painted shapes and gently irregular characters give a storybook world a handmade feel.<br>
> 不透明的水粉色块与微妙的干刷边缘，让简洁圆润的角色带上手作绘本气质。

What it takes: **Mostly art.** The look lives in made material; code only supports it. You need: Painted sprites and backgrounds with authentic brush and paper texture.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/3256150/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3256150/21265497594e8e2ec1435ab38fed1d59812e3fcf/ss_21265497594e8e2ec1435ab38fed1d59812e3fcf.600x338.jpg" width="100%" alt="Moomintroll: Winter's Warmth"></a><br><sub>Moomintroll: Winter's Warmth</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1808680/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1808680/ss_de3102a99281141312f2ab5888a581565e4877cf.600x338.jpg" width="100%" alt="Snufkin: Melody of Moominvalley"></a><br><sub>Snufkin: Melody of Moominvalley</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1419860/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1419860/ss_73259b282b42ab2c527e32e65c9520f9607ba015.600x338.jpg" width="100%" alt="Tukoni: Prologue"></a><br><sub>Tukoni: Prologue</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1444300/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1444300/ss_a756568f88979b4956e003907d72614a8ac5872d.600x338.jpg" width="100%" alt="Teacup"></a><br><sub>Teacup</sub></td>
</tr>
</table>

## How to spot it

- Matte colour blocks show brush grain instead of glossy gradients
- Rounded, slightly uneven silhouettes and very small faces
- A restrained natural palette keeps busy foliage readable

## Techniques

- gouache paint and dry-brush edges
- subtle paper grain
- layered 2D parallax

## Reference games

- [Carto](https://store.steampowered.com/app/1172450/)
- [Moomintroll: Winter's Warmth](https://store.steampowered.com/app/3256150/)
- [Snufkin: Melody of Moominvalley](https://store.steampowered.com/app/1808680/)
- [Tukoni: Prologue](https://store.steampowered.com/app/1419860/)
- [Teacup](https://store.steampowered.com/app/1444300/)

## Similar styles

- [Storybook / picture book](../storybook/) · 绘本
- [Watercolour](../watercolour/) · 水彩
- [Whimsical monochrome ink](../whimsical-ink/) · 俏皮黑白手绘

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Prepare painted sprites and background layers with opaque, gently broken brush edges; avoid smooth vector outlines.
1. In Godot, put painted layers in Parallax2D and apply a low-opacity paper-grain texture with a CanvasItem shader; a filter alone cannot replace painted art.
1. Use a small palette of muted greens, creams and accent colours; check grayscale contrast so tiny characters remain legible.
