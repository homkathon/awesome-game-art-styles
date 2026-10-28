# Vector / wireframe · 矢量线框

[← All styles](../../README.md#light--silhouette)

<a href="https://store.steampowered.com/app/636450/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/636450/ss_f9a0e030052db17cb2432168af5cb42faf66f0b3.600x338.jpg" width="100%" alt="Vector / wireframe: Rez Infinite"></a>

> Glowing lines on black, like an arcade vector monitor.<br>
> 黑底上发光的线条，像街机矢量显示器。

What it takes: **Code only.** Simple models plus shaders and post-processing get close.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/636450/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/636450/ss_54795193a491c9d5a0e49d9ee8776259ad44891d.600x338.jpg" width="100%" alt="Rez Infinite"></a><br><sub>Rez Infinite</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/636450/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/636450/ss_7b8c1b5c7324bcf45475e8e1409a03f8e967dd24.600x338.jpg" width="100%" alt="Rez Infinite"></a><br><sub>Rez Infinite</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/688140/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/688140/ss_997eae8fb0230a3148f742b29184c7a4b3db9923.600x338.jpg" width="100%" alt="Tempest 4000"></a><br><sub>Tempest 4000</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/688140/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/688140/ss_78cc46399ac534cab032b4b5e6580d202249e9d3.600x338.jpg" width="100%" alt="Tempest 4000"></a><br><sub>Tempest 4000</sub></td>
</tr>
</table>

## How to spot it

- Objects drawn as bright outlines, not filled surfaces
- Black background, additive glow
- Geometry pulses and flashes to music or action

## Techniques

- line rendering (edges only)
- additive blending and bloom
- audio-reactive animation

## Reference games

- [Rez Infinite](https://store.steampowered.com/app/636450/)
- [Tempest 4000](https://store.steampowered.com/app/688140/)

## Learn

- [Acerola](https://www.youtube.com/@Acerola_t) · stylised rendering deep dives

## Similar styles

- [Neon abstract](../neon-abstract/) · 霓虹抽象
- [Neon 80s pixel](../neon-80s/) · 80 年代霓虹像素

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Draw meshes with their edges only (three.js: `EdgesGeometry` + `LineSegments`, or `LineSegments2` + `LineMaterial` when lines must be thicker than 1 px, since WebGL ignores line width; Godot: `render_mode wireframe` in a spatial shader).
1. Use additive blending on a black background and add bloom.
1. Drive line brightness and thickness from the music or hit events.
