# Cel-shaded / toon · 卡通渲染

[← All styles](../../README.md#3d-shading--form)

<a href="https://store.steampowered.com/app/1817230/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1817230/ss_7dfaee4616fbed65b2b0fcb82d55dc0a957fd8a5.600x338.jpg" width="100%" alt="Cel-shaded / toon: Hi-Fi RUSH"></a>

> Two or three hard light bands, ink outlines, saturated colour.<br>
> 两三层硬边明暗、墨线描边、高饱和色彩。

▶ **[Live demo](https://homkathon.github.io/awesome-game-art-styles/demos/toon.html)** · runs in the browser, [source](../../demos/toon.html) is one HTML file with commented shaders

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1817230/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1817230/ss_382e9d5abb00498eee6a86b0366a2db7826268b7.600x338.jpg" width="100%" alt="Hi-Fi RUSH"></a><br><sub>Hi-Fi RUSH</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1817230/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1817230/ss_8a13650ffe930da77593dae80f0118588c46a5ca.600x338.jpg" width="100%" alt="Hi-Fi RUSH"></a><br><sub>Hi-Fi RUSH</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/49520/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/49520/ss_6734eaa79dcd0fe53971fbd50d20b5d0d45f4809.600x338.jpg" width="100%" alt="Borderlands 2"></a><br><sub>Borderlands 2</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/49520/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/49520/ss_c20610ab476bfe99172df77fe84f579d91e45a2b.600x338.jpg" width="100%" alt="Borderlands 2"></a><br><sub>Borderlands 2</sub></td>
</tr>
</table>

## How to spot it

- Shadows have a hard edge instead of a gradient
- Dark outlines around characters and props
- Bright, saturated colours

## Techniques

- stepped lighting ramp
- inverted-hull or post-process outlines
- rim light

## Reference games

- [Hi-Fi RUSH](https://store.steampowered.com/app/1817230/)
- [Borderlands 2](https://store.steampowered.com/app/49520/)

## Learn

- [Toon shader tutorial](https://roystan.net/articles/toon-shader/) · Roystan
- [5 ways to draw an outline](https://ameye.dev/notes/rendering-outlines/) · Alexander Ameye
- [Dungeons of Hinterberg: stylized rendering](https://x.com/PhilippSeifried/status/1354827696707002384) · PhilippSeifried (X technique post)

## Free assets to start with

- [KayKit](https://kaylousberg.itch.io/furniture-bits) · CC0
- [Kenney](https://kenney.nl/assets) · CC0

Licences change; check the pack page before you ship.

## Similar styles

- [Ligne claire / Moebius](../ligne-claire/) · 清线 / 墨比斯
- [Anime cel 2.5D](../anime-cel/) · 日式赛璐璐 2.5D

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.

1. Quantise N·L into 2–3 bands (Godot: custom `light()` function; three.js: `MeshToonMaterial` with a 3-texel gradient map and nearest filtering).
1. Draw outlines either with an inverted hull (duplicate mesh, front-face culled, pushed out along normals) or a post-process edge pass on normals and depth.
1. Turn off tone mapping or use a neutral curve so the bands stay crisp.
