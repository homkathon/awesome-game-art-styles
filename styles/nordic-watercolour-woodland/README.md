# Nordic watercolour woodland · 北欧水彩森林

[← All styles](../../README.md#2d-drawn--painted)

<a href="https://store.steampowered.com/app/3256150/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3256150/f17685012ab6062858ed94e2f5338e08256d7e61/ss_f17685012ab6062858ed94e2f5338e08256d7e61.600x338.jpg" width="100%" alt="Nordic watercolour woodland: Moomintroll: Winter's Warmth"></a>

> Soft painted forests and quiet characters turn exploration into a Nordic storybook.<br>
> 柔和水彩森林、宁静小人物和自然色调，让探索像北欧绘本。

What it takes: **Mostly art.** The look lives in made material; code only supports it. You need: Original layered watercolour backgrounds and nature sprites.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1808680/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1808680/ss_7b8df4e8746ed3461fc9aaba4af0e158c94dcd5f.600x338.jpg" width="100%" alt="Snufkin: Melody of Moominvalley"></a><br><sub>Snufkin: Melody of Moominvalley</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/3256150/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3256150/9a38008832971572e52f5082bb27d2ca98216cd8/ss_9a38008832971572e52f5082bb27d2ca98216cd8.600x338.jpg" width="100%" alt="Moomintroll: Winter's Warmth"></a><br><sub>Moomintroll: Winter's Warmth</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1419860/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1419860/ss_bf1fddecefb8c7e720ffafccce35f50937f11103.600x338.jpg" width="100%" alt="Tukoni: Prologue"></a><br><sub>Tukoni: Prologue</sub></td>
</tr>
</table>

## How to spot it

- Soft transparent painted foliage
- Small characters stay readable among layered trees
- Muted seasonal colours lead the scene

## Techniques

- painted foliage layers
- 2D parallax
- seasonal palette

## Reference games

- [Moomintroll: Winter's Warmth](https://store.steampowered.com/app/3256150/)
- [Snufkin: Melody of Moominvalley](https://store.steampowered.com/app/1808680/)
- [Tukoni: Prologue](https://store.steampowered.com/app/1419860/)

## Similar styles

- [Gouache picture book](../gouache-picture-book/) · 水粉质感绘本
- [Watercolour](../watercolour/) · 水彩

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section. When it runs, put a screenshot of your scene next to the gallery above and compare values first, then palette, then detail.

1. Paint foliage in separated transparent layers, retaining soft brush edges.
1. In Godot use Parallax2D for layered forest backgrounds and gently tint distant planes.
