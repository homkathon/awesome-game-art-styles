# Hand-drawn animation · 手绘动画

[← All styles](../../README.md#2d-drawn--painted)

<a href="https://store.steampowered.com/app/367520/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/367520/ss_d5b6edd94e77ba6db31c44d8a3c09d807ab27751.600x338.jpg" width="100%" alt="Hand-drawn animation: Hollow Knight"></a>

> Frame-by-frame or skeletal animation over painted backgrounds.<br>
> 逐帧或骨骼动画，配手绘背景。

What it takes: **Mostly art.** The look lives in made material; code only supports it. You need: Drawn character animation and painted background layers.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/367520/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/367520/ss_5384f9f8b96a0b9934b2bc35a4058376211636d2.600x338.jpg" width="100%" alt="Hollow Knight"></a><br><sub>Hollow Knight</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/367520/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/367520/ss_62e10cf506d461e11e050457b08aa0e2a1c078d0.600x338.jpg" width="100%" alt="Hollow Knight"></a><br><sub>Hollow Knight</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/387290/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/387290/ss_304ededbbfd607cb37e708cd83e7160c7d840863.600x338.jpg" width="100%" alt="Ori and the Blind Forest"></a><br><sub>Ori and the Blind Forest</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/972660/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/972660/ss_a751970e68bc928538fbc4f52d6090c6ff1d8974.600x338.jpg" width="100%" alt="Spiritfarer"></a><br><sub>Spiritfarer</sub></td>
</tr>
</table>

## How to spot it

- Characters look drawn, not modelled
- Painted backgrounds with many parallax layers
- Glow and particles over the art

## Techniques

- layered parallax
- particle-rich lighting
- frame-by-frame key poses

## Reference games

- [Hollow Knight](https://store.steampowered.com/app/367520/)
- [Ori and the Blind Forest](https://store.steampowered.com/app/387290/)
- [Spiritfarer](https://store.steampowered.com/app/972660/)

## Similar styles

- [Rubber hose (1930s cartoon)](../rubber-hose/) · 橡皮管 30 年代卡通
- [Watercolour](../watercolour/) · 水彩

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Split backgrounds into 5+ parallax layers with atmospheric tint per layer.
1. Animate characters frame by frame or with a skeletal tool (Spine, Godot Skeleton2D).
1. Add additive light sprites and particles for glow.
