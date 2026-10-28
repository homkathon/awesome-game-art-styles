# Whimsical monochrome ink · 俏皮黑白手绘

[← All styles](../../README.md#2d-drawn--painted)

<a href="https://store.steampowered.com/app/1307580/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1307580/ss_452053e6976add5d6690c6f5dc227d3fd4bda26d.600x338.jpg" width="100%" alt="Whimsical monochrome ink: TOEM: A Photo Adventure"></a>

> Playful black ink sketches on white, sometimes layered as 2D cutouts in tiny 3D worlds.<br>
> 轻松活泼的黑白墨线，搭配有趣的小角色；有时以二维剪纸的方式构成立体小世界。

What it takes: **Mostly art.** The look lives in made material; code only supports it. You need: Original hand-inked black-and-white sprites and scenery.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1307580/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1307580/ss_3c5c560a2627d6d35f69a138ec3159517c662e44.600x338.jpg" width="100%" alt="TOEM: A Photo Adventure"></a><br><sub>TOEM: A Photo Adventure</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1307580/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1307580/ss_88ec5d56ccceb942d8baa5f56481d254db78c398.600x338.jpg" width="100%" alt="TOEM: A Photo Adventure"></a><br><sub>TOEM: A Photo Adventure</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/435400/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/435400/ss_5cda037d48f0603bfc1268b1090d8a0f0f1780b3.600x338.jpg" width="100%" alt="Hidden Folks"></a><br><sub>Hidden Folks</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/435400/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/435400/ss_611032e3a955d50f03ed9303409b5d32e3173605.600x338.jpg" width="100%" alt="Hidden Folks"></a><br><sub>Hidden Folks</sub></td>
</tr>
</table>

## How to spot it

- Varied, slightly irregular black line weight defines objects
- Expressive tiny characters amid charming monochrome scene detail
- Layered drawings, cutouts and gentle grey shadows give depth

## Techniques

- hand-inked sprites and hatching
- flat grayscale surfaces and ambient occlusion
- orthographic cutout dioramas

## Reference games

- [TOEM: A Photo Adventure](https://store.steampowered.com/app/1307580/)
- [Hidden Folks](https://store.steampowered.com/app/435400/)

## Similar styles

- [Line art / colouring book](../line-art/) · 线稿 / 涂色书
- [Storybook / picture book](../storybook/) · 绘本
- [Gouache picture book](../gouache-picture-book/) · 水粉质感绘本

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Draw props and characters as transparent black-ink sprites with subtly varied line width; avoid CAD-clean strokes.
1. For a TOEM-like diorama, combine Godot Camera3D in orthographic mode with Sprite3D cutouts, simple grey meshes and light ambient occlusion.
1. For flat hidden-object scenes, use CanvasItem sprites and a 2D zoom camera instead; add hatching sparingly and keep UI out of hero shots.
