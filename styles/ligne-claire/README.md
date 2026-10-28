# Ligne claire / Moebius · 清线 / 墨比斯

[← All styles](../../README.md#3d-shading--form)

<a href="https://store.steampowered.com/app/757310/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/757310/ss_dbe1b07f58393b56c20e9ac031442e1e161fa989.600x338.jpg" width="100%" alt="Ligne claire / Moebius: Sable"></a>

> Uniform black outlines and flat colour fields, like a European comic album.

## Gallery

<table>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/757310/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/757310/ss_f7cf5d40340dfcfc534daff63be314fdbb9e6817.600x338.jpg" width="100%" alt="Sable"></a><br><sub>Sable</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/757310/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/757310/ss_cad83dc56ce2d4e690df7d31eac8346db25baa9d.600x338.jpg" width="100%" alt="Sable"></a><br><sub>Sable</sub></td>
</tr>
<tr>
<td width="50%"><a href="https://store.steampowered.com/app/1931770/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1931770/ss_0c7b55a542bab74ccb3bbab18346c0f68296ebf4.600x338.jpg" width="100%" alt="Chants of Sennaar"></a><br><sub>Chants of Sennaar</sub></td>
<td width="50%"><a href="https://store.steampowered.com/app/1931770/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1931770/ss_adcaa7de0b90bc02a927ec7119f889a0834e8484.600x338.jpg" width="100%" alt="Chants of Sennaar"></a><br><sub>Chants of Sennaar</sub></td>
</tr>
</table>

## How to spot it

- Every object has the same thin black outline
- Large flat colour areas with almost no shading
- Colour palette shifts strongly with time of day

## Techniques

- post-process outlines on everything
- unlit flat colour
- colour shifts by time of day

## Reference games

- [Sable](https://store.steampowered.com/app/757310/)
- [Chants of Sennaar](https://store.steampowered.com/app/1931770/)

## Learn

- [5 ways to draw an outline](https://ameye.dev/notes/rendering-outlines/) · Alexander Ameye

## Similar styles

- [Cel-shaded / toon](../toon/) · 卡通渲染
- [Flat-colour graphic 3D](../flat-colour-3d/) · 平涂图形化 3D

## Agent notes

Steps a coding agent (or you) can follow to reproduce the look. The [game-art-style skill](../../skills/game-art-style/SKILL.md) reads this section.

1. Use unlit materials with one flat colour each; add at most one shadow band.
1. Run an edge-detection pass on depth and normals and draw constant-width black lines.
1. Drive the whole palette from a time-of-day colour grade instead of real lighting.
