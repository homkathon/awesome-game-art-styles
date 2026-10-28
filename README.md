# Awesome Game Art Styles [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of game visual styles, organised by **look** rather than by asset type. Each style shows an in-game screenshot of a game that defines it, plus the techniques behind it, where to learn it, and free assets to start with.

Screenshots link to each game's Steam page and load from Steam; nothing is rehosted here. There is also a [Claude Code skill](skills/game-art-style/SKILL.md) that uses this list to help you pick a style.

## Contents

- [3D: shading & form](#3d-shading--form) · Low-poly · Toy diorama / tilt-shift · Minimal geometric 3D · Cel-shaded / toon · Anime cel 2.5D · Ligne claire / Moebius · Painterly · Flat-colour graphic 3D · Retro-futurism · Mixed media
- [3D: retro & lo-fi](#3d-retro--lo-fi) · PS1 / low-fi 3D · Pixelated 3D · Voxel · 1-bit / dithered
- [3D: handmade & material](#3d-handmade--material) · Claymation · Papercraft · Yarn / fabric · Dark miniature
- [Light & silhouette](#light--silhouette) · Silhouette noir · Neon abstract
- [2D: pixel](#2d-pixel) · Pixel art · HD-2D · Pixel anime / cyberpunk · Neon 80s pixel · Cozy interiors
- [2D: drawn & painted](#2d-drawn--painted) · Hand-drawn animation · Rubber hose (1930s cartoon) · Watercolour · Ink wash / sumi-e · Gothic ink · Painted comic · Line art / colouring book · Cute but dark
- [2D: graphic & print](#2d-graphic--print) · Flat vector minimal · Graphic design / Saul Bass · Bureaucratic / propaganda · Medieval manuscript / woodcut · ASCII / text
- [Asset libraries](#asset-libraries)
- [Learning resources](#learning-resources)
- [Related lists](#related-lists)
- [Wanted](#wanted)

## 3D: shading & form

<table>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/553420/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/553420/ss_9c0184ba83022786f74f4a70ebae5c47d2a3c35c.600x338.jpg" width="360" alt="Low-poly: TUNIC"></a></td>
<td><h3>Low-poly</h3>低多边形<br><br>Few, visible facets; colour carried by flat gradients or vertex colours rather than textures.<br><br>🎮 <a href="https://store.steampowered.com/app/553420/">TUNIC</a>, <a href="https://store.steampowered.com/app/1562430/">DREDGE</a></td>
<td width="300">• flat or gradient-atlas colours<br>• faceted normals<br>• strong fog for depth<br><br><b>Start with:</b> <a href="https://kaylousberg.itch.io/furniture-bits">KayKit</a>, <a href="https://kenney.nl/assets">Kenney</a>, <a href="https://quaternius.itch.io">Quaternius</a>, <a href="https://poly.pizza">Poly Pizza</a></td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/1291340/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1291340/ss_989ff1808d9416c7b22da3e16ee54874697b1cea.600x338.jpg" width="360" alt="Toy diorama / tilt-shift: Townscaper"></a></td>
<td><h3>Toy diorama / tilt-shift</h3>玩具微缩景<br><br>The world as a tabletop model: soft light, shallow depth of field, everything small and touchable.<br><br>🎮 <a href="https://store.steampowered.com/app/2198150/">Tiny Glade</a>, <a href="https://store.steampowered.com/app/1291340/">Townscaper</a>, <a href="https://store.steampowered.com/app/427820/">Hitman GO</a></td>
<td width="300">• bokeh depth of field<br>• ambient occlusion<br>• rounded bevels<br>• warm key light<br><br><b>Start with:</b> <a href="https://kaylousberg.itch.io/furniture-bits">KayKit</a>, <a href="https://kenney.nl/assets">Kenney</a></td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/1927720/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1927720/ss_c3c31892e894f72d70f2d3ad02018678ba817093.600x338.jpg" width="360" alt="Minimal geometric 3D: Monument Valley"></a></td>
<td><h3>Minimal geometric 3D</h3>极简几何 3D<br><br>Pastel solids, orthographic or isometric cameras, architecture as puzzle.<br><br>🎮 <a href="https://store.steampowered.com/app/1927720/">Monument Valley</a></td>
<td width="300">• orthographic camera<br>• flat shading<br>• pastel gradient sky</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/1817230/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1817230/ss_7dfaee4616fbed65b2b0fcb82d55dc0a957fd8a5.600x338.jpg" width="360" alt="Cel-shaded / toon: Hi-Fi RUSH"></a></td>
<td><h3>Cel-shaded / toon</h3>卡通渲染<br><br>Two or three hard light bands, ink outlines, saturated colour.<br><br>🎮 <a href="https://store.steampowered.com/app/1817230/">Hi-Fi RUSH</a>, <a href="https://store.steampowered.com/app/49520/">Borderlands 2</a></td>
<td width="300">• stepped lighting ramp<br>• inverted-hull or post-process outlines<br>• rim light<br><br><b>Start with:</b> <a href="https://roystan.net/articles/toon-shader/">Toon shader tutorial</a> (Roystan), <a href="https://ameye.dev/notes/rendering-outlines/">5 ways to draw an outline</a> (Alexander Ameye), <a href="https://kaylousberg.itch.io/furniture-bits">KayKit</a>, <a href="https://kenney.nl/assets">Kenney</a></td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/1384160/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1384160/ss_104e16788c2ea35e1dac31d96be8d4f1df00f330.600x338.jpg" width="360" alt="Anime cel 2.5D: GUILTY GEAR -STRIVE-"></a></td>
<td><h3>Anime cel 2.5D</h3>日式赛璐璐 2.5D<br><br>3D characters that read as hand-drawn animation: authored normals, held frames, no interpolation.<br><br>🎮 <a href="https://store.steampowered.com/app/1384160/">GUILTY GEAR -STRIVE-</a></td>
<td width="300">• hand-edited normals for clean shadows<br>• limited animation (stepped keys)<br>• per-shot light direction<br><br><b>Start with:</b> <a href="https://www.youtube.com/watch?v=yhGjCzxJV3E">GuiltyGearXrd's Art Style: The X Factor Between 2D and 3D</a> (GDC)</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/757310/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/757310/ss_dbe1b07f58393b56c20e9ac031442e1e161fa989.600x338.jpg" width="360" alt="Ligne claire / Moebius: Sable"></a></td>
<td><h3>Ligne claire / Moebius</h3>清线 / 墨比斯<br><br>Uniform black outlines and flat colour fields, like a European comic album.<br><br>🎮 <a href="https://store.steampowered.com/app/757310/">Sable</a>, <a href="https://store.steampowered.com/app/1931770/">Chants of Sennaar</a></td>
<td width="300">• post-process outlines on everything<br>• unlit flat colour<br>• colour shifts by time of day<br><br><b>Start with:</b> <a href="https://ameye.dev/notes/rendering-outlines/">5 ways to draw an outline</a> (Alexander Ameye)</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/632470/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/632470/ss_b3694e99ffdb686d1bbbbe16a540d3d2ccd509c4.600x338.jpg" width="360" alt="Painterly: Disco Elysium"></a></td>
<td><h3>Painterly</h3>油画感<br><br>Visible brush strokes, painted textures and skies; light as a painter would place it.<br><br>🎮 <a href="https://store.steampowered.com/app/632470/">Disco Elysium</a>, <a href="https://store.steampowered.com/app/1172620/">Sea of Thieves</a></td>
<td width="300">• hand-painted textures<br>• brush-stroke post filters<br>• painted backdrops</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/383870/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/383870/ss_80432f2d4f4192017115c23e7dff090df95b204a.600x338.jpg" width="360" alt="Flat-colour graphic 3D: Firewatch"></a></td>
<td><h3>Flat-colour graphic 3D</h3>平涂图形化 3D<br><br>Large flat colour shapes, graphic silhouettes, colour-coded atmosphere.<br><br>🎮 <a href="https://store.steampowered.com/app/383870/">Firewatch</a>, <a href="https://store.steampowered.com/app/231200/">Kentucky Route Zero</a></td>
<td width="300">• gradient fog by distance<br>• flat unlit materials<br>• strong colour scripts</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/8870/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/8870/ss_26e2d983948edfb911db3e0d2c3679900b4ef9fa.600x338.jpg" width="360" alt="Retro-futurism: BioShock Infinite"></a></td>
<td><h3>Retro-futurism</h3>复古未来主义<br><br>The future as an earlier decade imagined it: atomic-age optimism, art deco.<br><br>🎮 <a href="https://store.steampowered.com/app/377160/">Fallout 4</a>, <a href="https://store.steampowered.com/app/8870/">BioShock Infinite</a></td>
<td width="300">• period props and typography<br>• propaganda posters as set dressing</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/1092790/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1092790/ss_0191a69b0e94a9a7784f5b81e27f06379910645a.600x338.jpg" width="360" alt="Mixed media: Inscryption"></a></td>
<td><h3>Mixed media</h3>混合媒介<br><br>Different visual languages stacked in one game: 3D, pixel art, live-action, paper.<br><br>🎮 <a href="https://store.steampowered.com/app/1092790/">Inscryption</a></td>
<td width="300">• deliberate style breaks between layers<br>• diegetic UI</td>
</tr>
</table>

## 3D: retro & lo-fi

<table>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/519860/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/519860/ss_b2668c79d271be9b62a988682e30683ac8e5f410.600x338.jpg" width="360" alt="PS1 / low-fi 3D: DUSK"></a></td>
<td><h3>PS1 / low-fi 3D</h3>PS1 复古 3D<br><br>Wobbly vertices, warped textures, tiny resolution, dithered colour.<br><br>🎮 <a href="https://store.steampowered.com/app/1262350/">SIGNALIS</a>, <a href="https://store.steampowered.com/app/519860/">DUSK</a></td>
<td width="300">• vertex snapping<br>• affine texture mapping<br>• low-res render target<br>• colour dithering<br><br><b>Start with:</b> <a href="https://godotshaders.com">Godot Shaders</a>, <a href="https://kenney.nl/assets">Kenney</a></td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/1055540/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1055540/ss_f2123fea859e299736a3e99d130238c784d53e75.600x338.jpg" width="360" alt="Pixelated 3D: A Short Hike"></a></td>
<td><h3>Pixelated 3D</h3>像素化 3D<br><br>A 3D world rendered at low resolution so it reads as pixel art.<br><br>🎮 <a href="https://store.steampowered.com/app/1055540/">A Short Hike</a></td>
<td width="300">• low-res render target, nearest upscale<br>• pixel-snapped camera<br>• edge highlights<br><br><b>Start with:</b> <a href="https://www.youtube.com/@t3ssel8r">t3ssel8r</a> (pixel-art look in 3D), <a href="https://kaylousberg.itch.io/furniture-bits">KayKit</a>, <a href="https://kenney.nl/assets">Kenney</a></td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/1167630/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1167630/f266c2457a6b183a89abce8659bac7419fdfc5f0/ss_f266c2457a6b183a89abce8659bac7419fdfc5f0.600x338.jpg" width="360" alt="Voxel: Teardown"></a></td>
<td><h3>Voxel</h3>体素<br><br>The world built from cubes; often destructible.<br><br>🎮 <a href="https://store.steampowered.com/app/1167630/">Teardown</a></td>
<td width="300">• voxel meshing<br>• small-cube detail on large forms</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/653530/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/653530/ss_380dc35237fde7d3863a44270abafc37924d1db4.600x338.jpg" width="360" alt="1-bit / dithered: Return of the Obra Dinn"></a></td>
<td><h3>1-bit / dithered</h3>1-bit 抖动<br><br>Two colours and a dither pattern stand in for every tone.<br><br>🎮 <a href="https://store.steampowered.com/app/653530/">Return of the Obra Dinn</a>, <a href="https://store.steampowered.com/app/913740/">WORLD OF HORROR</a></td>
<td width="300">• ordered / blue-noise dithering<br>• stable dither in screen space<br><br><b>Start with:</b> <a href="https://forums.tigsource.com/index.php?topic=40832.msg1363742#msg1363742">Obra Dinn devlog: dithering</a> (Lucas Pope), <a href="https://www.youtube.com/@Acerola_t">Acerola</a> (stylised rendering deep dives)</td>
</tr>
</table>

## 3D: handmade & material

<table>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/924750/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/924750/ss_05f6b85959fecf4ed84c2e9de753bac3b2dba1da.600x338.jpg" width="360" alt="Claymation: Harold Halibut"></a></td>
<td><h3>Claymation</h3>黏土定格<br><br>Clay or puppet characters, fingerprints and all; real or faked stop motion.<br><br>🎮 <a href="https://store.steampowered.com/app/924750/">Harold Halibut</a>, <a href="https://store.steampowered.com/app/397740/">Hylics</a></td>
<td width="300">• photogrammetry of physical models<br>• stepped animation<br>• fingerprint normal maps</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/205020/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/205020/ss_926633bbe4e9f02eac35a4cafd0c153e595e28d4.600x338.jpg" width="360" alt="Papercraft: Lumino City"></a></td>
<td><h3>Papercraft</h3>纸艺<br><br>A world folded and cut from paper.<br><br>🎮 <a href="https://store.steampowered.com/app/205020/">Lumino City</a></td>
<td width="300">• real paper models photographed<br>• paper fibre textures<br>• fold and edge shading<br><br><b>Start with:</b> <a href="https://ambientcg.com">ambientCG</a></td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/1225560/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1225560/ss_107b49291a2cdc76a73b1c84191dbf0b86a6c8ef.600x338.jpg" width="360" alt="Yarn / fabric: Unravel"></a></td>
<td><h3>Yarn / fabric</h3>毛线 / 织物<br><br>Characters and props made of wool, felt or cloth.<br><br>🎮 <a href="https://store.steampowered.com/app/1225560/">Unravel</a></td>
<td width="300">• fibre textures<br>• soft subsurface scattering</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/424840/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/424840/24d7518ab72df4608de04f4ad4bc04ee479e3911/ss_24d7518ab72df4608de04f4ad4bc04ee479e3911.600x338.jpg" width="360" alt="Dark miniature: Little Nightmares"></a></td>
<td><h3>Dark miniature</h3>黑暗微缩<br><br>Toy-like scale used for dread: oversized furniture, dim pools of light.<br><br>🎮 <a href="https://store.steampowered.com/app/424840/">Little Nightmares</a></td>
<td width="300">• exaggerated scale<br>• volumetric light shafts<br>• heavy vignettes</td>
</tr>
</table>

## Light & silhouette

<table>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/48000/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/48000/ss_d33513ed37acf1073ea92f182b76e165101bfdac.600x338.jpg" width="360" alt="Silhouette noir: LIMBO"></a></td>
<td><h3>Silhouette noir</h3>剪影黑白<br><br>Black shapes against fog and light; no faces, no colour.<br><br>🎮 <a href="https://store.steampowered.com/app/48000/">LIMBO</a>, <a href="https://store.steampowered.com/app/304430/">INSIDE</a></td>
<td width="300">• back-lighting<br>• depth fog<br>• desaturated palette</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/1122720/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1122720/ss_03804e3335afd5edddceafe722ff1c4eb3c19931.600x338.jpg" width="360" alt="Neon abstract: Sayonara Wild Hearts"></a></td>
<td><h3>Neon abstract</h3>霓虹抽象<br><br>Pure colour, light trails and geometry in motion; often rhythm-led.<br><br>🎮 <a href="https://store.steampowered.com/app/356400/">Thumper</a>, <a href="https://store.steampowered.com/app/1122720/">Sayonara Wild Hearts</a></td>
<td width="300">• emissive materials and bloom<br>• chromatic aberration<br>• music-synced effects</td>
</tr>
</table>

## 2D: pixel

<table>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/250760/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/250760/ss_019205f5f9ae1c3f0d5359e967135a76ae1ebd2d.600x338.jpg" width="360" alt="Pixel art: Shovel Knight"></a></td>
<td><h3>Pixel art</h3>像素画<br><br>Hand-placed pixels with limited palettes.<br><br>🎮 <a href="https://store.steampowered.com/app/504230/">Celeste</a>, <a href="https://store.steampowered.com/app/250760/">Shovel Knight</a>, <a href="https://store.steampowered.com/app/413150/">Stardew Valley</a></td>
<td width="300">• limited palette<br>• sub-pixel animation<br>• integer scaling<br><br><b>Start with:</b> <a href="https://lospec.com/palette-list">Lospec palette list</a>, <a href="https://limezu.itch.io/moderninteriors">LimeZu</a>, <a href="https://kenney.nl/assets">Kenney</a></td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/921570/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/921570/ss_d9c13a8f046e48ae57a2f2d6d134850410fe4932.600x338.jpg" width="360" alt="HD-2D: Octopath Traveler"></a></td>
<td><h3>HD-2D</h3>HD-2D<br><br>Pixel sprites in a lit 3D world with depth of field and particles.<br><br>🎮 <a href="https://store.steampowered.com/app/921570/">Octopath Traveler</a>, <a href="https://store.steampowered.com/app/977880/">Eastward</a></td>
<td width="300">• sprites as billboards<br>• tilt-shift depth of field<br>• dynamic lights on pixel art</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/447530/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/447530/ss_1b98a18f6cd15773c8da098aad48917f5b5d22e1.600x338.jpg" width="360" alt="Pixel anime / cyberpunk: VA-11 Hall-A"></a></td>
<td><h3>Pixel anime / cyberpunk</h3>像素动漫 / 赛博朋克<br><br>Pixel art drawing on 80s and 90s anime and PC-98 games.<br><br>🎮 <a href="https://store.steampowered.com/app/447530/">VA-11 Hall-A</a></td>
<td width="300">• portrait-heavy layouts<br>• limited palette with neon accents<br><br><b>Start with:</b> <a href="https://lospec.com/palette-list">Lospec palette list</a></td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/219150/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/219150/ss_bdf28f59652e53e725d96d94cdc8db97fc277cf2.600x338.jpg" width="360" alt="Neon 80s pixel: Hotline Miami"></a></td>
<td><h3>Neon 80s pixel</h3>80 年代霓虹像素<br><br>Saturated magenta and cyan, VHS grain, screen shake.<br><br>🎮 <a href="https://store.steampowered.com/app/219150/">Hotline Miami</a></td>
<td width="300">• palette cycling<br>• screen shake<br>• chromatic aberration</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/1135690/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1135690/ss_b32bfdd3f68e1f9e264bd37e10a464629ca034f8.600x338.jpg" width="360" alt="Cozy interiors: Unpacking"></a></td>
<td><h3>Cozy interiors</h3>温馨室内像素<br><br>Small, warm, readable rooms full of objects.<br><br>🎮 <a href="https://store.steampowered.com/app/1135690/">Unpacking</a></td>
<td width="300">• isometric or 3/4 rooms<br>• warm palette<br><br><b>Start with:</b> <a href="https://limezu.itch.io/moderninteriors">LimeZu</a></td>
</tr>
</table>

## 2D: drawn & painted

<table>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/367520/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/367520/ss_d5b6edd94e77ba6db31c44d8a3c09d807ab27751.600x338.jpg" width="360" alt="Hand-drawn animation: Hollow Knight"></a></td>
<td><h3>Hand-drawn animation</h3>手绘动画<br><br>Frame-by-frame or skeletal animation over painted backgrounds.<br><br>🎮 <a href="https://store.steampowered.com/app/367520/">Hollow Knight</a>, <a href="https://store.steampowered.com/app/387290/">Ori and the Blind Forest</a>, <a href="https://store.steampowered.com/app/972660/">Spiritfarer</a></td>
<td width="300">• layered parallax<br>• particle-rich lighting<br>• frame-by-frame key poses</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/268910/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/268910/ss_483fb089be0093beeef03525276803a9ca4f66a1.600x338.jpg" width="360" alt="Rubber hose (1930s cartoon): Cuphead"></a></td>
<td><h3>Rubber hose (1930s cartoon)</h3>橡皮管 30 年代卡通<br><br>Bendy limbs, pie-cut eyes, film grain and jitter.<br><br>🎮 <a href="https://store.steampowered.com/app/268910/">Cuphead</a>, <a href="https://store.steampowered.com/app/622650/">Bendy and the Ink Machine</a></td>
<td width="300">• hand-inked frames<br>• film grain and gate weave<br>• period colour grading</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/1272840/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1272840/ss_0d2bac05234a73ac1cc9dbcbee31e6774e8846df.600x338.jpg" width="360" alt="Watercolour: Dordogne"></a></td>
<td><h3>Watercolour</h3>水彩<br><br>Pigment washes, soft edges, paper texture.<br><br>🎮 <a href="https://store.steampowered.com/app/683320/">GRIS</a>, <a href="https://store.steampowered.com/app/1272840/">Dordogne</a></td>
<td width="300">• edge darkening<br>• pigment granulation<br>• paper texture overlay<br><br><b>Start with:</b> <a href="https://ambientcg.com">ambientCG</a></td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/587620/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/587620/ss_cd53a4f4e19997789b43d4ffbfae495a338da93e.600x338.jpg" width="360" alt="Ink wash / sumi-e: Ōkami HD"></a></td>
<td><h3>Ink wash / sumi-e</h3>水墨<br><br>Brush ink on paper, calligraphic strokes, seals.<br><br>🎮 <a href="https://store.steampowered.com/app/587620/">Ōkami HD</a></td>
<td width="300">• brush-stroke outlines<br>• paper texture<br>• ink bleed<br><br><b>Start with:</b> <a href="https://ambientcg.com">ambientCG</a></td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/219740/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/219740/ss_3d32a04e77363f3c8179a319de6f90ac1b8b2e0e.600x338.jpg" width="360" alt="Gothic ink: Don't Starve"></a></td>
<td><h3>Gothic ink</h3>哥特墨线<br><br>Heavy black linework, crosshatching, desaturated colour.<br><br>🎮 <a href="https://store.steampowered.com/app/262060/">Darkest Dungeon</a>, <a href="https://store.steampowered.com/app/219740/">Don't Starve</a></td>
<td width="300">• thick ink outlines<br>• crosshatch shading<br>• muted palette</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/1145360/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1145360/ss_8a9f0953e8a014bd3df2789c2835cb787cd3764d.600x338.jpg" width="360" alt="Painted comic: Hades"></a></td>
<td><h3>Painted comic</h3>彩绘漫画<br><br>Comic-book inks with painted colour and bold shapes.<br><br>🎮 <a href="https://store.steampowered.com/app/1145360/">Hades</a></td>
<td width="300">• inked outlines<br>• painted fills<br>• graphic key art</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/1123450/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1123450/ss_2f643ac851b504a1c10e0b6f1cfdc3089707ab55.600x338.jpg" width="360" alt="Line art / colouring book: Chicory: A Colorful Tale"></a></td>
<td><h3>Line art / colouring book</h3>线稿 / 涂色书<br><br>Black lines on white; colour as something the player adds.<br><br>🎮 <a href="https://store.steampowered.com/app/1123450/">Chicory: A Colorful Tale</a>, <a href="https://store.steampowered.com/app/530320/">Wandersong</a></td>
<td width="300">• clean vector-like linework<br>• player-driven fills</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/1313140/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1313140/ss_b26625d6f64a739ed1ddf832a5d26b665ab0619f.600x338.jpg" width="360" alt="Cute but dark: Cult of the Lamb"></a></td>
<td><h3>Cute but dark</h3>可爱黑暗<br><br>A soft, round, cute surface wrapped around grim themes.<br><br>🎮 <a href="https://store.steampowered.com/app/1313140/">Cult of the Lamb</a>, <a href="https://store.steampowered.com/app/481510/">Night in the Woods</a></td>
<td width="300">• round shapes, big eyes<br>• pastel palette against dark subject matter<br><br><b>Start with:</b> <a href="https://www.openpeeps.com">Open Peeps</a></td>
</tr>
</table>

## 2D: graphic & print

<table>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/287980/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/287980/ss_c7bc5df7e606504709e9f53ff9c7584ac4c01b18.600x338.jpg" width="360" alt="Flat vector minimal: Mini Metro"></a></td>
<td><h3>Flat vector minimal</h3>扁平极简矢量<br><br>Lines, dots and solid shapes; information design as art.<br><br>🎮 <a href="https://store.steampowered.com/app/287980/">Mini Metro</a>, <a href="https://store.steampowered.com/app/220780/">Thomas Was Alone</a></td>
<td width="300">• solid colour shapes<br>• no outlines or textures<br>• colour as data</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/447150/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/447150/ss_aaa4a17ce60a909664f5e1eba7187c1d792e32e6.600x338.jpg" width="360" alt="Graphic design / Saul Bass: APE OUT"></a></td>
<td><h3>Graphic design / Saul Bass</h3>平面设计<br><br>Bold cut-paper shapes, few colours, film-title typography.<br><br>🎮 <a href="https://store.steampowered.com/app/447150/">APE OUT</a>, <a href="https://store.steampowered.com/app/2008920/">Lorelei and the Laser Eyes</a></td>
<td width="300">• two or three colours<br>• silhouettes<br>• typography as image</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/239030/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/239030/ss_4b50458fbc4afe2917803b59a35afb3e5d61c960.600x338.jpg" width="360" alt="Bureaucratic / propaganda: Papers, Please"></a></td>
<td><h3>Bureaucratic / propaganda</h3>官僚 / 宣传画<br><br>Forms, stamps and posters; the interface is the institution.<br><br>🎮 <a href="https://store.steampowered.com/app/239030/">Papers, Please</a>, <a href="https://store.steampowered.com/app/761620/">Beholder 2</a></td>
<td width="300">• document UI<br>• stamps and seals<br>• constructivist posters<br>• drab palette</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/1205520/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1205520/ss_d6e8594853dc8a16033c3644a0fbb05909f2848b.600x338.jpg" width="360" alt="Medieval manuscript / woodcut: Pentiment"></a></td>
<td><h3>Medieval manuscript / woodcut</h3>中世纪手抄本 / 木刻<br><br>Illuminated pages, woodcut prints, marginalia.<br><br>🎮 <a href="https://store.steampowered.com/app/1205520/">Pentiment</a>, <a href="https://store.steampowered.com/app/957960/">Inkulinati</a></td>
<td width="300">• parchment textures<br>• woodcut line shading<br>• typeface changes per character</td>
</tr>
<tr>
<td width="380"><a href="https://store.steampowered.com/app/603390/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/603390/ss_98312257e7a8b1ee3c8964d6dede01cf69c002f0.600x338.jpg" width="360" alt="ASCII / text: Stone Story RPG"></a></td>
<td><h3>ASCII / text</h3>ASCII / 字符画<br><br>The world drawn with characters.<br><br>🎮 <a href="https://store.steampowered.com/app/333640/">Caves of Qud</a>, <a href="https://store.steampowered.com/app/603390/">Stone Story RPG</a></td>
<td width="300">• monospace grid<br>• character-based animation</td>
</tr>
</table>

## Asset libraries

Free or cheap packs that work across several styles. Licences were checked on 2026-10-28; check again before you ship.

| Library | Type | Licence | Cost | Notes |
|:--|:--|:--|:--|:--|
| [KayKit Furniture Bits](https://kaylousberg.itch.io/furniture-bits) | 3D | 🟢 CC0 | Free | 50+ pieces on one gradient atlas: recolour the whole set by editing one image. [GitHub](https://github.com/KayKit-Game-Assets/KayKit-Furniture-Bits-1.0) has it as a Godot addon, with the other [KayKit packs](https://github.com/KayKit-Game-Assets). |
| [Kenney](https://kenney.nl/assets) | 3D / 2D | 🟢 CC0 | Free | Huge library, including animated [Mini Characters](https://kenney.nl/assets/mini-characters) and the [Furniture Kit](https://kenney.nl/assets/furniture-kit). |
| [Quaternius](https://quaternius.itch.io) | 3D | 🟠 Custom | Free | Pack pages say CC0, but the site now publishes its own Quaternius Asset Licence. |
| [Poly Pizza](https://poly.pizza) | 3D | 🟡 CC0 / CC-BY | Free | 7000+ lowpoly models; check each one. |
| [Synty POLYGON](https://syntystore.com/products/polygon-office-pack) | 3D | 🔴 Commercial | Paid | Large themed packs; the licence does not address web builds. |
| [LimeZu Modern Interiors](https://limezu.itch.io/moderninteriors) | Pixel | 🔴 Commercial | Paid | Credit required. Cosy pixel interiors. |
| [2dPig Pixel Office](https://2dpig.itch.io/pixel-office) | Pixel | 🟢 CC0 | Free | Office props and five characters. |
| [Open Peeps](https://www.openpeeps.com) | 2D | 🟢 CC0 | Free | Hand-drawn mix-and-match people. |
| [Humaaans](https://www.humaaans.com) | 2D | 🟠 Unclear | Free | Licence wording varies between sources. |
| [ambientCG](https://ambientcg.com) | Texture | 🟢 CC0 | Free | Paper, fabric, wood. |
| [Poly Haven](https://polyhaven.com) | Texture / HDRI | 🟢 CC0 | Free | HDRIs, textures, models. |

## Learning resources

| Resource | Format | Covers |
|:--|:--|:--|
| [Godot Shaders](https://godotshaders.com) | Shader library | Toon, outlines, PSX, dithering, watercolour and more. |
| [Toon shader tutorial](https://roystan.net/articles/toon-shader/) | Article | Step-by-step cel shading (Roystan). |
| [5 ways to draw an outline](https://ameye.dev/notes/rendering-outlines/) | Article | Comparison of outline techniques (Alexander Ameye). |
| [GuiltyGearXrd's Art Style](https://www.youtube.com/watch?v=yhGjCzxJV3E) | GDC talk | Making 3D look hand-drawn. |
| [Obra Dinn devlog: dithering](https://forums.tigsource.com/index.php?topic=40832.msg1363742#msg1363742) | Devlog | Stable 1-bit dithering (Lucas Pope). |
| [Acerola](https://www.youtube.com/@Acerola_t) | Video channel | Stylised rendering deep dives. |
| [t3ssel8r](https://www.youtube.com/@t3ssel8r) | Video channel | Pixel-art look in real-time 3D. |
| [Lospec palette list](https://lospec.com/palette-list) | Palette library | Palettes for pixel art and limited-colour styles. |

## Related lists

- [awesome-cc0](https://github.com/madjin/awesome-cc0) - Public-domain assets.
- [awesome-gamedev](https://github.com/Calinou/awesome-gamedev) - Free software and free culture for making games.
- [Awesome-Gamedev](https://github.com/FronkonGames/Awesome-Gamedev) - Broad game development resource list.
- [Awesome-Illustrations-4Projects](https://github.com/Anmol-Baranwal/Awesome-Illustrations-4Projects) - Illustration libraries.
- [awesome-pixel-art](https://github.com/Siilwyn/awesome-pixel-art) - Pixel art tutorials and tools.
- [awesome-godot](https://github.com/Calinou/awesome-godot) - Godot plugins, templates and demos.

## Wanted

Styles without a good reference game in the list yet. Pull requests welcome.

| Style | What to look for |
|:--|:--|
| Risograph / two-ink print | Halftone dots, two spot inks, mis-registration |
| Corporate Memphis | Flat blob people, noodle limbs, tech-brand pastels |
| Blueprint / technical drawing | Line drawings on a grid, dimensions, annotations |
| Ukiyo-e woodblock | Woodblock outlines, flat bokashi gradients |
| Manga screentone | Screentone patterns, speed lines, panel layouts |
| Stained glass | Lead lines, translucent colour cells |
| Gouache picture book | Opaque painted shapes, visible brush texture |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

