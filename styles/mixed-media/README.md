# Mixed media · 混合媒介

[← All styles](../../README.md#3d-shading--form)

<a href="https://store.steampowered.com/app/1092790/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1092790/ss_0191a69b0e94a9a7784f5b81e27f06379910645a.600x338.jpg" width="100%" alt="Mixed media: Inscryption"></a>

> Different visual languages stacked in one game: 3D, pixel art, live-action, paper.<br>
> 一个游戏里叠用多种视觉语言：3D、像素、真人实拍、纸。

What it takes: **Code plus assets.** The rendering is code, but it needs suitable models, textures or sprites: Separate art for each layer (world, UI, cutscenes).

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1092790/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1092790/ss_3b714682e9e0a214df1630a234e9f6764528eece.600x338.jpg" width="100%" alt="Inscryption"></a><br><sub>Inscryption</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1092790/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1092790/ss_7bfe728822807d232398df1cb1a5d64addd3d8fb.600x338.jpg" width="100%" alt="Inscryption"></a><br><sub>Inscryption</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1092790/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1092790/ss_79a146c36a3f0b728a8e0085327cec8c7fba82d6.600x338.jpg" width="100%" alt="Inscryption"></a><br><sub>Inscryption</sub></td>
</tr>
</table>

## How to spot it

- The style changes between layers or acts on purpose
- UI is part of the world (cards, papers, screens)

## Techniques

- deliberate style breaks between layers
- diegetic UI

## Reference games

- [Inscryption](https://store.steampowered.com/app/1092790/)

## Similar styles

- [PS1 / low-fi 3D](../ps1/) · PS1 复古 3D
- [Papercraft](../papercraft/) · 纸艺

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Decide which style each layer gets (world, UI, cutscenes) and keep each layer internally consistent.
1. Make UI physical: cards, papers, monitors inside the scene.
1. Use a shared colour grade to tie the layers together.
