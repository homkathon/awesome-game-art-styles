# Retro FPS / boomer shooter · 复古 FPS

[← All styles](../../README.md#3d-retro--lo-fi)

<a href="https://store.steampowered.com/app/1229490/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1229490/ss_bc7a00fadbcde4a6c6dcb95d8e464ad5ffc06e3c.600x338.jpg" width="100%" alt="Retro FPS / boomer shooter: ULTRAKILL"></a>

> Mid-90s shooter looks: chunky textures, sprite-like enemies, bright pickups, fast movement.<br>
> 90 年代中期射击游戏的样子：粗颗粒贴图、像精灵图的敌人、醒目的道具、高速移动。

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/562860/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/562860/ss_406b0b080e523ff37d843151449fcd7149c7ef72.600x338.jpg" width="100%" alt="Ion Fury"></a><br><sub>Ion Fury</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/964800/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/964800/ss_2810cf77fe7dff16357004184621b0a0e98ca146.600x338.jpg" width="100%" alt="Prodeus"></a><br><sub>Prodeus</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1684930/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1684930/87851204173c816a4d5284c9110b7f34fdd71d3f/ss_87851204173c816a4d5284c9110b7f34fdd71d3f.600x338.jpg" width="100%" alt="CULTIC"></a><br><sub>CULTIC</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1229490/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1229490/ss_7a5692d56ec4115252980fed4ad5536d1e401e04.600x338.jpg" width="100%" alt="ULTRAKILL"></a><br><sub>ULTRAKILL</sub></td>
</tr>
</table>

## How to spot it

- Low-resolution, unfiltered textures on simple level geometry
- Big readable enemies and pickups
- Strong coloured lighting, little realism

## Techniques

- nearest-filtered textures
- low texel density
- billboard sprites or low-poly enemies
- limited palettes

## Reference games

- [ULTRAKILL](https://store.steampowered.com/app/1229490/)
- [Ion Fury](https://store.steampowered.com/app/562860/)
- [Prodeus](https://store.steampowered.com/app/964800/)
- [CULTIC](https://store.steampowered.com/app/1684930/)

## Learn

- [Godot Shaders](https://godotshaders.com) · community shader library
- [Render-texture-driven fracture](https://x.com/Cyanilux/status/1638623920235356172) · Cyanilux (X technique post)

## Free assets to start with

- [Kenney](https://kenney.nl/assets) · CC0

Licences change; check the pack page before you ship.

## Similar styles

- [PS1 / low-fi 3D](../ps1/) · PS1 复古 3D
- [Pixelated 3D](../pixelated-3d/) · 像素化 3D

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.

1. Use small textures (64–128 px) with nearest filtering and no mipmap blur.
1. Build levels from boxes and ramps; detail comes from texture and light colour, not geometry.
1. Draw enemies as camera-facing sprites with 8 directions, or as low-poly models with pixel textures.
