# Pre-rendered backgrounds · 预渲染背景

[← All styles](../../README.md#3d-retro--lo-fi)

<a href="https://store.steampowered.com/app/291650/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/291650/ss_fbc3b33088a2ec5e718271a122c370afee8eb4cf.600x338.jpg" width="100%" alt="Pre-rendered backgrounds: Pillars of Eternity"></a>

> Richly detailed painted-or-rendered backdrops with real-time characters walking through them.<br>
> 精细的预渲染或手绘背景，实时角色在其中走动。

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/304240/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/304240/ss_d75906451d3a57bb8fc65fdea7ce09fbf1d3b726.600x338.jpg" width="100%" alt="Resident Evil"></a><br><sub>Resident Evil</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1367590/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1367590/ss_87d9cb58df5d9e8a474cc5e3256ea71dfa22b085.600x338.jpg" width="100%" alt="Tormented Souls"></a><br><sub>Tormented Souls</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/228280/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/228280/ss_24f9924a78b5d0b08877e5e24804056ec7d5a12c.600x338.jpg" width="100%" alt="Baldur's Gate: Enhanced Edition"></a><br><sub>Baldur's Gate: Enhanced Edition</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/291650/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/291650/ss_d80d3bce1480ab165508877479353449ad30536a.600x338.jpg" width="100%" alt="Pillars of Eternity"></a><br><sub>Pillars of Eternity</sub></td>
</tr>
</table>

## How to spot it

- Fixed camera angles or a fixed isometric view
- Backgrounds far more detailed than the characters
- Characters occluded by invisible depth masks

## Techniques

- offline render or paint-over backgrounds
- depth or collision masks for occlusion
- fixed cameras

## Reference games

- [Pillars of Eternity](https://store.steampowered.com/app/291650/)
- [Resident Evil](https://store.steampowered.com/app/304240/)
- [Tormented Souls](https://store.steampowered.com/app/1367590/)
- [Baldur's Gate: Enhanced Edition](https://store.steampowered.com/app/228280/)

## Free assets to start with

- [Poly Pizza](https://poly.pizza) · CC0 / CC-BY

Licences change; check the pack page before you ship.

## Similar styles

- [Painterly](../painterly/) · 油画感
- [PS1 / low-fi 3D](../ps1/) · PS1 复古 3D

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.

1. Render (or paint over) each background from a fixed camera, and save a matching depth image.
1. Draw real-time characters with the same camera, testing their depth against the saved depth image so they pass behind objects.
1. Match lighting: bake the background light direction and use it for characters.
