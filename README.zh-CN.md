<p align="center"><img src="assets/banner.png" alt="One scene in four styles: toon, PS1, 1-bit, pixelated 3D"></p>

# Awesome Game Art Styles [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Styles](https://img.shields.io/badge/styles-64-f2b134)](#3d明暗与造型) [![Licence: CC0](https://img.shields.io/badge/licence-CC0-lightgrey)](LICENSE) [![check](https://github.com/homkathon/awesome-game-art-styles/actions/workflows/check.yml/badge.svg)](https://github.com/homkathon/awesome-game-art-styles/actions/workflows/check.yml)

[English](README.md) · **简体中文**

> 64 种游戏视觉风格，按**观感**分类。点进每种风格可以看截图、识别要点、实现技术、教程、免费素材，以及给编程智能体的实现步骤。

🌐 **中文网页版：[homkathon.gokoding.com/styles](https://homkathon.gokoding.com/styles)**。可以搜索、按分类筛选，在每种风格的页面里翻截图、直接玩在线演示。

截图直接从 Steam 加载并链接到游戏商店页，本仓库不转存任何截图。用 [Claude Code 技能](skills/game-art-style/SKILL.md)可以为你的游戏推荐风格（安装方法：让你的编程智能体读 [https://homkathon.gokoding.com/styles/install.md](https://homkathon.gokoding.com/styles/install.md)），也可以打开[在线着色器演示](https://homkathon.github.io/awesome-game-art-styles/demos/)看卡通、PS1、1-bit 和像素化 3D 的实时效果。在 [X 视频画廊](https://homkathon.github.io/awesome-game-art-styles/x-posts/)直接播放或下载经授权收录的 MP4（保留作者及原帖链接）。风格详情页目前为英文。

## 目录

- [3D：明暗与造型](#3d明暗与造型)
- [3D：复古与低保真](#3d复古与低保真)
- [3D：手作与材质](#3d手作与材质)
- [光与剪影](#光与剪影)
- [2D：像素](#2d像素)
- [2D：手绘与绘画](#2d手绘与绘画)
- [2D：平面与印刷](#2d平面与印刷)
- [素材库](#素材库)
- [学习资源](#学习资源)

- [插画游戏灵感](#illustrated-inspiration)

<a id="illustrated-inspiration"></a>
## 插画游戏灵感 · 16 款作品

以下都是独立的视觉案例，不是 16 种人为拆分出来的美术流派。点击图片查看 Steam 原始截图和游戏，点击风格进入实现说明。

<table>
<tr>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/1172450/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1172450/ss_5e9fb66710e5b0b8912c43f56299830893435379.600x338.jpg" width="100%" alt="Carto: 水粉质感绘本"></a><br><b><a href="https://store.steampowered.com/app/1172450/">Carto</a></b><br><sub><a href="styles/gouache-picture-book/">水粉质感绘本</a></sub><br><sub>手绘地图图块与讨喜小人物</sub></td>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/3256150/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3256150/f17685012ab6062858ed94e2f5338e08256d7e61/ss_f17685012ab6062858ed94e2f5338e08256d7e61.600x338.jpg" width="100%" alt="Moomintroll: Winter's Warmth: 北欧水彩森林"></a><br><b><a href="https://store.steampowered.com/app/3256150/">Moomintroll: Winter's Warmth</a></b><br><sub><a href="styles/nordic-watercolour-woodland/">北欧水彩森林</a></sub><br><sub>雪景纸纹与北欧森林</sub></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/1808680/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1808680/ss_7b8df4e8746ed3461fc9aaba4af0e158c94dcd5f.600x338.jpg" width="100%" alt="Snufkin: Melody of Moominvalley: 北欧水彩森林"></a><br><b><a href="https://store.steampowered.com/app/1808680/">Snufkin: Melody of Moominvalley</a></b><br><sub><a href="styles/nordic-watercolour-woodland/">北欧水彩森林</a></sub><br><sub>宁静的水彩林地探索</sub></td>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/1307580/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1307580/ss_3c5c560a2627d6d35f69a138ec3159517c662e44.600x338.jpg" width="100%" alt="TOEM: A Photo Adventure: 俏皮黑白手绘"></a><br><b><a href="https://store.steampowered.com/app/1307580/">TOEM: A Photo Adventure</a></b><br><sub><a href="styles/whimsical-ink/">俏皮黑白手绘</a></sub><br><sub>黑白墨线剪纸与柔和 3D 景深</sub></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/1419860/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1419860/ss_bf1fddecefb8c7e720ffafccce35f50937f11103.600x338.jpg" width="100%" alt="Tukoni: Prologue: 森林民间传说插画"></a><br><b><a href="https://store.steampowered.com/app/1419860/">Tukoni: Prologue</a></b><br><sub><a href="styles/woodland-folklore-illustration/">森林民间传说插画</a></sub><br><sub>手绘森林生灵与植物</sub></td>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/1444300/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1444300/ss_93c9da1b8b189e06cf3c3c8f7f549546895b8cda.600x338.jpg" width="100%" alt="Teacup: 柔色小生灵插画"></a><br><b><a href="https://store.steampowered.com/app/1444300/">Teacup</a></b><br><sub><a href="styles/pastel-creature-vignettes/">柔色小生灵插画</a></sub><br><sub>柔色动物绘本场景</sub></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/1055540/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1055540/ss_0e864bf975bb71f238de6861fc8fd3d6ed6e4ce8.600x338.jpg" width="100%" alt="A Short Hike: 低分辨率自然微缩景"></a><br><b><a href="https://store.steampowered.com/app/1055540/">A Short Hike</a></b><br><sub><a href="styles/cozy-lowres-nature-3d/">低分辨率自然微缩景</a></sub><br><sub>像素柔化的户外探索</sub></td>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/1594940/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1594940/623dea3c94ca66719a29abd1919e7547a5cbec3d/ss_623dea3c94ca66719a29abd1919e7547a5cbec3d.600x338.jpg" width="100%" alt="Little Witch in the Woods: 温暖绘本像素"></a><br><b><a href="https://store.steampowered.com/app/1594940/">Little Witch in the Woods</a></b><br><sub><a href="styles/cozy-pixel-storybook/">温暖绘本像素</a></sub><br><sub>温暖而细致的森林像素</sub></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/1123450/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1123450/ss_1f16a64698124ab065ed1fdd7cc0ea23511f3791.600x338.jpg" width="100%" alt="Chicory: A Colorful Tale: 松弛线稿卡通"></a><br><b><a href="https://store.steampowered.com/app/1123450/">Chicory: A Colorful Tale</a></b><br><sub><a href="styles/loose-line-cartoons/">松弛线稿卡通</a></sub><br><sub>松弛墨线与趣味填色</sub></td>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/977880/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/977880/ss_b3512f7576dbdd1e35dd3fb27a04f29174efb00d.600x338.jpg" width="100%" alt="Eastward: 电影感像素绘景"></a><br><b><a href="https://store.steampowered.com/app/977880/">Eastward</a></b><br><sub><a href="styles/cinematic-pixel-painting/">电影感像素绘景</a></sub><br><sub>细致的电影感像素绘景</sub></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/1062140/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1062140/ss_ee75af73d8bad015cfcf86530fceb627d9e6b298.600x338.jpg" width="100%" alt="Garden Story: 温暖绘本像素"></a><br><b><a href="https://store.steampowered.com/app/1062140/">Garden Story</a></b><br><sub><a href="styles/cozy-pixel-storybook/">温暖绘本像素</a></sub><br><sub>圆润的像素小生灵</sub></td>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/729000/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/729000/ss_b5c706abacf932c95851ab3c74ef5555f2151215.600x338.jpg" width="100%" alt="Wytchwood: 森林民间传说插画"></a><br><b><a href="https://store.steampowered.com/app/729000/">Wytchwood</a></b><br><sub><a href="styles/woodland-folklore-illustration/">森林民间传说插画</a></sub><br><sub>装饰性的民俗森林</sub></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/581270/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/581270/ss_b0e4a7017f9fa3f64bb7fb953583e323389194a2.600x338.jpg" width="100%" alt="Old Man's Journey: 分层纸片风景"></a><br><b><a href="https://store.steampowered.com/app/581270/">Old Man's Journey</a></b><br><sub><a href="styles/layered-paper-landscapes/">分层纸片风景</a></sub><br><sub>层叠的手绘纸片风景</sub></td>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/2322180/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2322180/ss_bb56c95322d9fbbd7ec6f6fa0354dcb34c70255b.600x338.jpg" width="100%" alt="A Tiny Sticker Tale: 贴纸绘本拼贴"></a><br><b><a href="https://store.steampowered.com/app/2322180/">A Tiny Sticker Tale</a></b><br><sub><a href="styles/stickerbook-cutouts/">贴纸绘本拼贴</a></sub><br><sub>可摆弄的贴纸式绘本道具</sub></td>
</tr>
<tr>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/1889740/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1889740/ss_a1a611020f74862495fa0777a6d5da84a0c061a2.600x338.jpg" width="100%" alt="Paper Trail: 纸面插画解谜"></a><br><b><a href="https://store.steampowered.com/app/1889740/">Paper Trail</a></b><br><sub><a href="styles/illustrated-paper-puzzles/">纸面插画解谜</a></sub><br><sub>可折叠的插画纸面世界</sub></td>
<td width="50%" valign="top"><a href="https://store.steampowered.com/app/435400/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/435400/ss_5cda037d48f0603bfc1268b1090d8a0f0f1780b3.600x338.jpg" width="100%" alt="Hidden Folks: 俏皮黑白手绘"></a><br><b><a href="https://store.steampowered.com/app/435400/">Hidden Folks</a></b><br><sub><a href="styles/whimsical-ink/">俏皮黑白手绘</a></sub><br><sub>微型黑白涂鸦场景</sub></td>
</tr>
</table>

### 插画创作者参考

作者作品仅供研究参考，不代表可自由复用的素材。

- [Oksana Bula](https://www.tukoni.com.ua/en) — Tukoni 绘本创作者
- [Tove Jansson](https://tovejansson.com/gallery/the-moomins/) — 姆明原作及插画创作者
- [Kuan-Hung Chen](https://sunheadgames.com/en/press/carto/) — Carto 美术参考
- [Sylvain Tegroeg](https://vgagallery.org/collection/sylvain-tegroeg-factory) — Hidden Folks 黑白墨线画
- [Carson Ellis](https://www.carsonellis.com/work-gallery/) — 奇趣的绘本风景
- [Rebecca Green](https://www.myblankpaper.com/work/) — 粉彩、铅笔与水粉插画

---

## 3D：明暗与造型

<table>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/low-poly/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/553420/ss_9c0184ba83022786f74f4a70ebae5c47d2a3c35c.600x338.jpg" width="220" alt="Low-poly"></a><br><a href="styles/low-poly/"><b>低多边形</b></a><br><sub>Low-poly</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/toy-diorama/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1291340/ss_989ff1808d9416c7b22da3e16ee54874697b1cea.600x338.jpg" width="220" alt="Toy diorama / tilt-shift"></a><br><a href="styles/toy-diorama/"><b>玩具微缩景</b></a><br><sub>Toy diorama / tilt-shift</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/minimal-geometric/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1927720/ss_c3c31892e894f72d70f2d3ad02018678ba817093.600x338.jpg" width="220" alt="Minimal geometric 3D"></a><br><a href="styles/minimal-geometric/"><b>极简几何 3D</b></a><br><sub>Minimal geometric 3D</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/toon/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1817230/ss_7dfaee4616fbed65b2b0fcb82d55dc0a957fd8a5.600x338.jpg" width="220" alt="Cel-shaded / toon"></a><br><a href="styles/toon/"><b>卡通渲染</b></a><br><sub>Cel-shaded / toon</sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/anime-cel/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1384160/ss_104e16788c2ea35e1dac31d96be8d4f1df00f330.600x338.jpg" width="220" alt="Anime cel 2.5D"></a><br><a href="styles/anime-cel/"><b>日式赛璐璐 2.5D</b></a><br><sub>Anime cel 2.5D</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/ligne-claire/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/757310/ss_dbe1b07f58393b56c20e9ac031442e1e161fa989.600x338.jpg" width="220" alt="Ligne claire / Moebius"></a><br><a href="styles/ligne-claire/"><b>清线 / 墨比斯</b></a><br><sub>Ligne claire / Moebius</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/painterly/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/632470/ss_b3694e99ffdb686d1bbbbe16a540d3d2ccd509c4.600x338.jpg" width="220" alt="Painterly"></a><br><a href="styles/painterly/"><b>油画感</b></a><br><sub>Painterly</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/flat-colour-3d/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/383870/ss_80432f2d4f4192017115c23e7dff090df95b204a.600x338.jpg" width="220" alt="Flat-colour graphic 3D"></a><br><a href="styles/flat-colour-3d/"><b>平涂图形化 3D</b></a><br><sub>Flat-colour graphic 3D</sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/retro-futurism/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/8870/ss_26e2d983948edfb911db3e0d2c3679900b4ef9fa.600x338.jpg" width="220" alt="Retro-futurism"></a><br><a href="styles/retro-futurism/"><b>复古未来主义</b></a><br><sub>Retro-futurism</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/mixed-media/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1092790/ss_0191a69b0e94a9a7784f5b81e27f06379910645a.600x338.jpg" width="220" alt="Mixed media"></a><br><a href="styles/mixed-media/"><b>混合媒介</b></a><br><sub>Mixed media</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/fmv/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/368370/ss_9a5538329a233de7c86e14e331c3894a942b1693.600x338.jpg" width="220" alt="FMV / live action"></a><br><a href="styles/fmv/"><b>真人影像 / FMV</b></a><br><sub>FMV / live action</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/graffiti/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1353230/ss_044bea0014a39e31e6c3893dc6a4e80ad52896cd.600x338.jpg" width="220" alt="Graffiti / Y2K street"></a><br><a href="styles/graffiti/"><b>涂鸦 / Y2K 街头</b></a><br><sub>Graffiti / Y2K street</sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/soft-pastel/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1097150/ss_b695ced32eeef3059970c195b222460990d55401.600x338.jpg" width="220" alt="Soft pastel / jelly"></a><br><a href="styles/soft-pastel/"><b>软萌糖果色</b></a><br><sub>Soft pastel / jelly</sub></td>
</tr>
</table>

## 3D：复古与低保真

<table>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/ps1/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/519860/ss_b2668c79d271be9b62a988682e30683ac8e5f410.600x338.jpg" width="220" alt="PS1 / low-fi 3D"></a><br><a href="styles/ps1/"><b>PS1 复古 3D</b></a><br><sub>PS1 / low-fi 3D</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/pixelated-3d/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1055540/ss_f2123fea859e299736a3e99d130238c784d53e75.600x338.jpg" width="220" alt="Pixelated 3D"></a><br><a href="styles/pixelated-3d/"><b>像素化 3D</b></a><br><sub>Pixelated 3D</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/voxel/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1167630/f266c2457a6b183a89abce8659bac7419fdfc5f0/ss_f266c2457a6b183a89abce8659bac7419fdfc5f0.600x338.jpg" width="220" alt="Voxel"></a><br><a href="styles/voxel/"><b>体素</b></a><br><sub>Voxel</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/1-bit/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/653530/ss_380dc35237fde7d3863a44270abafc37924d1db4.600x338.jpg" width="220" alt="1-bit / dithered"></a><br><a href="styles/1-bit/"><b>1-bit 抖动</b></a><br><sub>1-bit / dithered</sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/pre-rendered/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/291650/ss_fbc3b33088a2ec5e718271a122c370afee8eb4cf.600x338.jpg" width="220" alt="Pre-rendered backgrounds"></a><br><a href="styles/pre-rendered/"><b>预渲染背景</b></a><br><sub>Pre-rendered backgrounds</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/boomer-shooter/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1229490/ss_bc7a00fadbcde4a6c6dcb95d8e464ad5ffc06e3c.600x338.jpg" width="220" alt="Retro FPS / boomer shooter"></a><br><a href="styles/boomer-shooter/"><b>复古 FPS</b></a><br><sub>Retro FPS / boomer shooter</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/lo-fi-surreal/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1388770/ss_5234b051b742a8cf758fc35895ca563880de1001.600x338.jpg" width="220" alt="Lo-fi surreal / ugly"></a><br><a href="styles/lo-fi-surreal/"><b>低保真超现实 / 丑美学</b></a><br><sub>Lo-fi surreal / ugly</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/cozy-lowres-nature-3d/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1055540/ss_0e864bf975bb71f238de6861fc8fd3d6ed6e4ce8.600x338.jpg" width="220" alt="Cozy low-resolution 3D nature"></a><br><a href="styles/cozy-lowres-nature-3d/"><b>低分辨率自然微缩景</b></a><br><sub>Cozy low-resolution 3D nature</sub></td>
</tr>
</table>

## 3D：手作与材质

<table>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/claymation/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/924750/ss_05f6b85959fecf4ed84c2e9de753bac3b2dba1da.600x338.jpg" width="220" alt="Claymation"></a><br><a href="styles/claymation/"><b>黏土定格</b></a><br><sub>Claymation</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/papercraft/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/205020/ss_926633bbe4e9f02eac35a4cafd0c153e595e28d4.600x338.jpg" width="220" alt="Papercraft"></a><br><a href="styles/papercraft/"><b>纸艺</b></a><br><sub>Papercraft</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/yarn/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1225560/ss_107b49291a2cdc76a73b1c84191dbf0b86a6c8ef.600x338.jpg" width="220" alt="Yarn / fabric"></a><br><a href="styles/yarn/"><b>毛线 / 织物</b></a><br><sub>Yarn / fabric</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/dark-miniature/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/424840/24d7518ab72df4608de04f4ad4bc04ee479e3911/ss_24d7518ab72df4608de04f4ad4bc04ee479e3911.600x338.jpg" width="220" alt="Dark miniature"></a><br><a href="styles/dark-miniature/"><b>黑暗微缩</b></a><br><sub>Dark miniature</sub></td>
</tr>
</table>

## 光与剪影

<table>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/silhouette/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/48000/ss_d33513ed37acf1073ea92f182b76e165101bfdac.600x338.jpg" width="220" alt="Silhouette noir"></a><br><a href="styles/silhouette/"><b>剪影黑白</b></a><br><sub>Silhouette noir</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/neon-abstract/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1122720/ss_03804e3335afd5edddceafe722ff1c4eb3c19931.600x338.jpg" width="220" alt="Neon abstract"></a><br><a href="styles/neon-abstract/"><b>霓虹抽象</b></a><br><sub>Neon abstract</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/vector-wireframe/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/636450/ss_f9a0e030052db17cb2432168af5cb42faf66f0b3.600x338.jpg" width="220" alt="Vector / wireframe"></a><br><a href="styles/vector-wireframe/"><b>矢量线框</b></a><br><sub>Vector / wireframe</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/spot-colour/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/322500/ss_1e3ef7d9d9654c6189e6680502a0ce3068d1aef7.600x338.jpg" width="220" alt="Monochrome + one colour"></a><br><a href="styles/spot-colour/"><b>单色 + 强调色</b></a><br><sub>Monochrome + one colour</sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/liminal/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2663530/ss_3ad834a1f3b0d5db35daeeedbf9e99c6a47d1091.600x338.jpg" width="220" alt="Liminal spaces"></a><br><a href="styles/liminal/"><b>阈限空间</b></a><br><sub>Liminal spaces</sub></td>
</tr>
</table>

## 2D：像素

<table>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/pixel-art/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/250760/ss_019205f5f9ae1c3f0d5359e967135a76ae1ebd2d.600x338.jpg" width="220" alt="Pixel art"></a><br><a href="styles/pixel-art/"><b>像素画</b></a><br><sub>Pixel art</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/hd-2d/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/921570/ss_d9c13a8f046e48ae57a2f2d6d134850410fe4932.600x338.jpg" width="220" alt="HD-2D"></a><br><a href="styles/hd-2d/"><b>HD-2D</b></a><br><sub>HD-2D</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/pixel-anime/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/447530/ss_1b98a18f6cd15773c8da098aad48917f5b5d22e1.600x338.jpg" width="220" alt="Pixel anime / cyberpunk"></a><br><a href="styles/pixel-anime/"><b>像素动漫 / 赛博朋克</b></a><br><sub>Pixel anime / cyberpunk</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/neon-80s/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/219150/ss_bdf28f59652e53e725d96d94cdc8db97fc277cf2.600x338.jpg" width="220" alt="Neon 80s pixel"></a><br><a href="styles/neon-80s/"><b>80 年代霓虹像素</b></a><br><sub>Neon 80s pixel</sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/cozy/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1135690/ss_b32bfdd3f68e1f9e264bd37e10a464629ca034f8.600x338.jpg" width="220" alt="Cozy interiors"></a><br><a href="styles/cozy/"><b>温馨室内像素</b></a><br><sub>Cozy interiors</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/nes-8bit/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/764790/ss_875fe259c26f29d959efba0eca47e1b63d844c75.600x338.jpg" width="220" alt="8-bit / NES"></a><br><a href="styles/nes-8bit/"><b>8-bit / FC</b></a><br><sub>8-bit / NES</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/cozy-pixel-storybook/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1062140/ss_9d643d5db7b194146bbe2d6f233e039900e74106.600x338.jpg" width="220" alt="Cozy storybook pixel art"></a><br><a href="styles/cozy-pixel-storybook/"><b>温暖绘本像素</b></a><br><sub>Cozy storybook pixel art</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/cinematic-pixel-painting/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/977880/ss_b3512f7576dbdd1e35dd3fb27a04f29174efb00d.600x338.jpg" width="220" alt="Cinematic pixel painting"></a><br><a href="styles/cinematic-pixel-painting/"><b>电影感像素绘景</b></a><br><sub>Cinematic pixel painting</sub></td>
</tr>
</table>

## 2D：手绘与绘画

<table>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/hand-drawn/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/367520/ss_d5b6edd94e77ba6db31c44d8a3c09d807ab27751.600x338.jpg" width="220" alt="Hand-drawn animation"></a><br><a href="styles/hand-drawn/"><b>手绘动画</b></a><br><sub>Hand-drawn animation</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/rubber-hose/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/268910/ss_483fb089be0093beeef03525276803a9ca4f66a1.600x338.jpg" width="220" alt="Rubber hose (1930s cartoon)"></a><br><a href="styles/rubber-hose/"><b>橡皮管 30 年代卡通</b></a><br><sub>Rubber hose (1930s cartoon)</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/watercolour/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1272840/ss_0d2bac05234a73ac1cc9dbcbee31e6774e8846df.600x338.jpg" width="220" alt="Watercolour"></a><br><a href="styles/watercolour/"><b>水彩</b></a><br><sub>Watercolour</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/ink-wash/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/587620/ss_cd53a4f4e19997789b43d4ffbfae495a338da93e.600x338.jpg" width="220" alt="Ink wash / sumi-e"></a><br><a href="styles/ink-wash/"><b>水墨</b></a><br><sub>Ink wash / sumi-e</sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/gothic-ink/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/219740/ss_3d32a04e77363f3c8179a319de6f90ac1b8b2e0e.600x338.jpg" width="220" alt="Gothic ink"></a><br><a href="styles/gothic-ink/"><b>哥特墨线</b></a><br><sub>Gothic ink</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/painted-comic/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1145360/ss_8a9f0953e8a014bd3df2789c2835cb787cd3764d.600x338.jpg" width="220" alt="Painted comic"></a><br><a href="styles/painted-comic/"><b>彩绘漫画</b></a><br><sub>Painted comic</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/line-art/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1123450/ss_2f643ac851b504a1c10e0b6f1cfdc3089707ab55.600x338.jpg" width="220" alt="Line art / colouring book"></a><br><a href="styles/line-art/"><b>线稿 / 涂色书</b></a><br><sub>Line art / colouring book</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/cute-dark/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1313140/ss_b26625d6f64a739ed1ddf832a5d26b665ab0619f.600x338.jpg" width="220" alt="Cute but dark"></a><br><a href="styles/cute-dark/"><b>可爱黑暗</b></a><br><sub>Cute but dark</sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/storybook/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/581270/ss_11406a46468e36e249a26f9054dfef162678c076.600x338.jpg" width="220" alt="Storybook / picture book"></a><br><a href="styles/storybook/"><b>绘本</b></a><br><sub>Storybook / picture book</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/rotoscope/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/233550/ss_72559daf5b29da71ea9e1cd74a67e130552674f3.600x338.jpg" width="220" alt="Rotoscope / flat polygons"></a><br><a href="styles/rotoscope/"><b>转描 / 平面多边形</b></a><br><sub>Rotoscope / flat polygons</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/gouache-picture-book/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1172450/ss_5e9fb66710e5b0b8912c43f56299830893435379.600x338.jpg" width="220" alt="Gouache picture book"></a><br><a href="styles/gouache-picture-book/"><b>水粉质感绘本</b></a><br><sub>Gouache picture book</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/whimsical-ink/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1307580/ss_452053e6976add5d6690c6f5dc227d3fd4bda26d.600x338.jpg" width="220" alt="Whimsical monochrome ink"></a><br><a href="styles/whimsical-ink/"><b>俏皮黑白手绘</b></a><br><sub>Whimsical monochrome ink</sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/nordic-watercolour-woodland/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3256150/f17685012ab6062858ed94e2f5338e08256d7e61/ss_f17685012ab6062858ed94e2f5338e08256d7e61.600x338.jpg" width="220" alt="Nordic watercolour woodland"></a><br><a href="styles/nordic-watercolour-woodland/"><b>北欧水彩森林</b></a><br><sub>Nordic watercolour woodland</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/layered-paper-landscapes/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/581270/ss_b0e4a7017f9fa3f64bb7fb953583e323389194a2.600x338.jpg" width="220" alt="Layered paper landscapes"></a><br><a href="styles/layered-paper-landscapes/"><b>分层纸片风景</b></a><br><sub>Layered paper landscapes</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/stickerbook-cutouts/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2322180/ss_bb56c95322d9fbbd7ec6f6fa0354dcb34c70255b.600x338.jpg" width="220" alt="Stickerbook cutouts"></a><br><a href="styles/stickerbook-cutouts/"><b>贴纸绘本拼贴</b></a><br><sub>Stickerbook cutouts</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/woodland-folklore-illustration/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1419860/ss_bf1fddecefb8c7e720ffafccce35f50937f11103.600x338.jpg" width="220" alt="Woodland folklore illustration"></a><br><a href="styles/woodland-folklore-illustration/"><b>森林民间传说插画</b></a><br><sub>Woodland folklore illustration</sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/loose-line-cartoons/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1444300/ss_93c9da1b8b189e06cf3c3c8f7f549546895b8cda.600x338.jpg" width="220" alt="Loose-line storybook cartoons"></a><br><a href="styles/loose-line-cartoons/"><b>松弛线稿卡通</b></a><br><sub>Loose-line storybook cartoons</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/pastel-creature-vignettes/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1444300/ss_34ef91065a1e9be3d8fc9f28437be9e6bfe164dc.600x338.jpg" width="220" alt="Pastel creature vignettes"></a><br><a href="styles/pastel-creature-vignettes/"><b>柔色小生灵插画</b></a><br><sub>Pastel creature vignettes</sub></td>
</tr>
</table>

## 2D：平面与印刷

<table>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/flat-vector/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/287980/ss_c7bc5df7e606504709e9f53ff9c7584ac4c01b18.600x338.jpg" width="220" alt="Flat vector minimal"></a><br><a href="styles/flat-vector/"><b>扁平极简矢量</b></a><br><sub>Flat vector minimal</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/graphic-design/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/447150/ss_aaa4a17ce60a909664f5e1eba7187c1d792e32e6.600x338.jpg" width="220" alt="Graphic design / Saul Bass"></a><br><a href="styles/graphic-design/"><b>平面设计</b></a><br><sub>Graphic design / Saul Bass</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/bureaucratic/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/239030/ss_4b50458fbc4afe2917803b59a35afb3e5d61c960.600x338.jpg" width="220" alt="Bureaucratic / propaganda"></a><br><a href="styles/bureaucratic/"><b>官僚 / 宣传画</b></a><br><sub>Bureaucratic / propaganda</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/manuscript/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1205520/ss_d6e8594853dc8a16033c3644a0fbb05909f2848b.600x338.jpg" width="220" alt="Medieval manuscript / woodcut"></a><br><a href="styles/manuscript/"><b>中世纪手抄本 / 木刻</b></a><br><sub>Medieval manuscript / woodcut</sub></td>
</tr>
<tr>
<td align="center" valign="top" width="25%"><a href="styles/ascii/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/603390/ss_98312257e7a8b1ee3c8964d6dede01cf69c002f0.600x338.jpg" width="220" alt="ASCII / text"></a><br><a href="styles/ascii/"><b>ASCII / 字符画</b></a><br><sub>ASCII / text</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/desktop-ui/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/844590/ss_801ae3d54dc30f1cfbbc9cd397d87d69def94356.600x338.jpg" width="220" alt="Desktop / OS interface"></a><br><a href="styles/desktop-ui/"><b>桌面 / 操作系统界面</b></a><br><sub>Desktop / OS interface</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/stained-glass/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1034150/ss_bf7d6fdf910f95c39d3fda401ba0c57840849586.600x338.jpg" width="220" alt="Stained glass"></a><br><a href="styles/stained-glass/"><b>彩色玻璃</b></a><br><sub>Stained glass</sub></td>
<td align="center" valign="top" width="25%"><a href="styles/illustrated-paper-puzzles/"><img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1172450/ss_85d60c053d7f16b03d3378e4466be3bdbdcea692.600x338.jpg" width="220" alt="Illustrated paper puzzles"></a><br><a href="styles/illustrated-paper-puzzles/"><b>纸面插画解谜</b></a><br><sub>Illustrated paper puzzles</sub></td>
</tr>
</table>

## 素材库

授权说明于 2026-10-28 核对。授权会变，发布前请到素材页面再确认。🟢 CC0 · 🟡 CC-BY · 🟠 自定义 / 不明确 · 🔴 商业授权

| 素材库 | 类型 | 授权 | 费用 | 说明 |
|---|---|---|---|---|
| [KayKit Furniture Bits](https://kaylousberg.itch.io/furniture-bits) | 3D | 🟢 CC0 | 免费 | 50 多件家具共用一张渐变贴图：改一张图就能给整套换色。作者希望不要原样转售素材，授权仍为 CC0。[GitHub](https://github.com/KayKit-Game-Assets/KayKit-Furniture-Bits-1.0) 上有 Godot 插件版，以及其他 [KayKit 素材包](https://github.com/KayKit-Game-Assets)。 |
| [Kenney](https://kenney.nl/assets) | 3D / 2D | 🟢 CC0 | 免费 | 素材量巨大，包括带动画的 [Mini Characters](https://kenney.nl/assets/mini-characters) 和 [Furniture Kit](https://kenney.nl/assets/furniture-kit)。 |
| [Quaternius](https://quaternius.itch.io) | 3D | 🟠 自定义 | 免费 | 素材页写的是 CC0，但网站现在发布了自己的 Quaternius Asset Licence。 |
| [Poly Pizza](https://poly.pizza) | 3D | 🟡 CC0 / CC-BY | 免费 | 7000 多个低多边形模型；每个都要单独看授权。 |
| [Synty POLYGON](https://syntystore.com/products/polygon-office-pack) | 3D | 🔴 商业 | 付费 | 大型主题素材包；授权条款没有提到网页版。 |
| [LimeZu Modern Interiors](https://limezu.itch.io/moderninteriors) | 像素 | 🔴 商业 | 付费 | 需要署名。温馨像素室内。 |
| [2dPig Pixel Office](https://2dpig.itch.io/pixel-office) | 像素 | 🟢 CC0 | 免费 | 办公室道具和五个角色。 |
| [Open Peeps](https://www.openpeeps.com) | 2D | 🟢 CC0 | 免费 | 手绘风格、可自由拼装的人物。 |
| [Humaaans](https://www.humaaans.com) | 2D | 🟠 不明确 | 免费 | 不同来源的授权说法不一致。 |
| [ambientCG](https://ambientcg.com) | 贴图 | 🟢 CC0 | 免费 | 纸、布料、木头。[官方授权说明](https://docs.ambientcg.com/license/)确认可商用且无需署名。 |
| [Poly Haven](https://polyhaven.com) | 贴图 / HDRI | 🟢 CC0 | 免费 | HDRI、贴图、模型。 |

## 学习资源

| 资源 | 形式 | 内容 |
|---|---|---|
| [Godot Shaders](https://godotshaders.com) | 着色器库 | 卡通、描边、PSX、抖动、水彩等。 |
| [Toon shader tutorial](https://roystan.net/articles/toon-shader/) | 文章 | 一步步实现卡通着色（Roystan）。 |
| [5 ways to draw an outline](https://ameye.dev/notes/rendering-outlines/) | 文章 | 各种描边技术的对比（Alexander Ameye）。 |
| [GuiltyGearXrd's Art Style](https://www.youtube.com/watch?v=yhGjCzxJV3E) | GDC 演讲 | 让 3D 看起来像手绘。 |
| [Obra Dinn devlog: dithering](https://forums.tigsource.com/index.php?topic=40832.msg1363742#msg1363742) | 开发日志 | 稳定的 1-bit 抖动（Lucas Pope）。 |
| [Acerola](https://www.youtube.com/@Acerola_t) | 视频频道 | 风格化渲染深度解析。 |
| [t3ssel8r](https://www.youtube.com/@t3ssel8r) | 视频频道 | 实时 3D 中的像素画观感。 |
| [Lospec palette list](https://lospec.com/palette-list) | 调色板库 | 像素画和限色风格的调色板。 |

## X 热门技术帖精选

直接在这里用 GitHub 原生播放器观看视频；没有视频的原帖展示图片。

[在 X 视频画廊播放和下载经授权的 MP4](https://homkathon.github.io/awesome-game-art-styles/x-posts/)（保留作者、原文与原帖链接；无视频帖使用 X 嵌入）。

共 22 条已核实的创作者原帖，按具体技法分组。优先收录可参考的 Shader、渲染和美术制作方法，不按未经验证的互动数字排序。**人工精选，并非实时热榜**。作者、原帖内容和发布日期于 2026-10-28 通过 X 嵌入元数据核实。

### 水体与氛围

<table>
<tr>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/e66f2271-3549-4186-8cfc-7d937077a227" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1864638156588400707">海岸线 Shader 新版</a></strong></p>
<sub>视频 · @Cyanilux · 2024-12-05 · <a href="https://x.com/Cyanilux/status/1864638156588400707">原帖 ↗</a></sub>
<p>海浪、岸边泡沫与湿沙的着色效果，原帖评论附教程</p>
<sub>关联风格: <a href="styles/cozy/">温馨室内像素</a></sub>
</td>
<td width="50%" valign="top">
<a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1252298028607774721"><img src="x-posts/previews/1252298028607774721.jpg" width="100%" alt="海岸线 Shader 原理拆解"></a>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1252298028607774721">海岸线 Shader 原理拆解</a></strong></p>
<sub>图文 · @Cyanilux · 2020-04-20 · <a href="https://x.com/Cyanilux/status/1252298028607774721">原帖 ↗</a></sub>
<p>受《动物森友会》启发的水深感知岸边浪花与水面边缘</p>
<sub>关联风格: <a href="styles/cozy/">温馨室内像素</a></sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/86cbd001-062d-4224-a2fd-205b6ddd832e" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1581210772352290818">Gerstner 波浪海面</a></strong></p>
<sub>视频 · @Cyanilux · 2022-10-15 · <a href="https://x.com/Cyanilux/status/1581210772352290818">原帖 ↗</a></sub>
<p>用 Gerstner 波叠加位移塑造风格化海面</p>
<sub>关联风格: <a href="styles/flat-colour-3d/">平涂图形化 3D</a></sub>
</td>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/53a5d7c2-abba-45e7-b21a-168670d6f39a" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1770095395848237506">2.5D 水面与精灵反射</a></strong></p>
<sub>视频 · @Cyanilux · 2024-03-19 · <a href="https://x.com/Cyanilux/status/1770095395848237506">原帖 ↗</a></sub>
<p>俯视水体 Shader 与像素精灵倒影</p>
<sub>关联风格: <a href="styles/hd-2d/">HD-2D</a></sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/224bc590-5f2b-416a-854e-5efbb4abf0c8" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1495405379253116930">程序化极光</a></strong></p>
<sub>视频 · @Cyanilux · 2022-02-20 · <a href="https://x.com/Cyanilux/status/1495405379253116930">原帖 ↗</a></sub>
<p>细分面片位移、渐变、滚动噪声与远处淡出</p>
<sub>关联风格: <a href="styles/neon-abstract/">霓虹抽象</a></sub>
</td>
</tr>
</table>

### 光照与风格化渲染

<table>
<tr>
<td width="50%" valign="top">
<a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1975506073319567393"><img src="x-posts/previews/1975506073319567393.jpg" width="100%" alt="解析式环境光遮蔽"></a>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1975506073319567393">解析式环境光遮蔽</a></strong></p>
<sub>图文 · @florisium · 2025-10-07 · <a href="https://x.com/florisium/status/1975506073319567393">原帖 ↗</a></sub>
<p>基于几何体的解析式 AO 技术及场景前后对比（技术长帖）</p>
<sub>关联风格: <a href="styles/toy-diorama/">玩具微缩景</a></sub>
</td>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/b8802851-7f05-42ab-bcd7-d29ecaf630ee" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1783442615939297380">面片假体积光</a></strong></p>
<sub>视频 · @Cyanilux · 2024-04-25 · <a href="https://x.com/Cyanilux/status/1783442615939297380">原帖 ↗</a></sub>
<p>沿光方向拉伸面片、阴影遮罩与深度淡出</p>
<sub>关联风格: <a href="styles/silhouette/">剪影黑白</a></sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/0e7f9450-9a62-4189-91c0-f0b19ca44dce" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1362466015976783872">《辛特堡传说》描边拆解</a></strong></p>
<sub>视频 · @PhilippSeifried · 2021-02-18 · <a href="https://x.com/PhilippSeifried/status/1362466015976783872">原帖 ↗</a></sub>
<p>技术长帖：如何控制风格化描边的宽度和位置</p>
<sub>关联风格: <a href="styles/ligne-claire/">清线 / 墨比斯</a></sub>
</td>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/07fc6d86-883e-4cd8-9951-4bdce6d60d5f" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1354827696707002384">《辛特堡传说》风格化渲染</a></strong></p>
<sub>视频 · @PhilippSeifried · 2021-01-28 · <a href="https://x.com/PhilippSeifried/status/1354827696707002384">原帖 ↗</a></sub>
<p>自定义延迟渲染，利用 G-buffer 中的材质 ID 控制风格</p>
<sub>关联风格: <a href="styles/toon/">卡通渲染</a></sub>
</td>
</tr>
</table>

### 材质与程序化场景

<table>
<tr>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/86c7023c-eec3-483d-99cf-33140ed14cfa" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1407727586986311687">彩色玻璃与体积光</a></strong></p>
<sub>视频 · @Cyanilux · 2021-06-23 · <a href="https://x.com/Cyanilux/status/1407727586986311687">原帖 ↗</a></sub>
<p>玻璃片分区着色与 Ray Marching 光束结合</p>
<sub>关联风格: <a href="styles/stained-glass/">彩色玻璃</a></sub>
</td>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/08022f98-f2e1-4633-bb78-b5b22675ff32" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1376949139838275584">镭射烫金材质</a></strong></p>
<sub>视频 · @Cyanilux · 2021-03-30 · <a href="https://x.com/Cyanilux/status/1376949139838275584">原帖 ↗</a></sub>
<p>彩虹贴图配合切线空间视线方向 UV 视差</p>
<sub>关联风格: <a href="styles/retro-futurism/">复古未来主义</a></sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/c8370dfa-6f0a-43ab-9a1b-159b0c1e017b" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1396848736022802435">Shader Graph GPU 草地</a></strong></p>
<sub>视频 · @Cyanilux · 2021-05-24 · <a href="https://x.com/Cyanilux/status/1396848736022802435">原帖 ↗</a></sub>
<p>Unity Shader Graph 配合 DrawMeshInstancedIndirect 草地实例化</p>
<sub>关联风格: <a href="styles/low-poly/">低多边形</a></sub>
</td>
<td width="50%" valign="top">
<a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1618030887412862977"><img src="x-posts/previews/1618030887412862977.jpg" width="100%" alt="沿曲线生长的常春藤"></a>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1618030887412862977">沿曲线生长的常春藤</a></strong></p>
<sub>图文 · @Cyanilux · 2023-01-24 · <a href="https://x.com/Cyanilux/status/1618030887412862977">原帖 ↗</a></sub>
<p>用 Blender Geometry Nodes 沿手绘曲线布置藤叶</p>
<sub>关联风格: <a href="styles/low-poly/">低多边形</a></sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1251916279205814272"><img src="x-posts/previews/1251916279205814272.jpg" width="100%" alt="世界弯曲 Shader Graph"></a>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1251916279205814272">世界弯曲 Shader Graph</a></strong></p>
<sub>图文 · @Cyanilux · 2020-04-19 · <a href="https://x.com/Cyanilux/status/1251916279205814272">原帖 ↗</a></sub>
<p>Shader Graph 弯曲子图，并通过 C# 关键字控制运行时启用</p>
<sub>关联风格: <a href="styles/toy-diorama/">玩具微缩景</a></sub>
</td>
</tr>
</table>

### 特效与破碎

<table>
<tr>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/ab573f7f-a2d8-4524-ac25-3050c654ef38" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-2019471084375130140">假体积烟雾</a></strong></p>
<sub>视频 · @Tuatara_Games · 2026-02-05 · <a href="https://x.com/Tuatara_Games/status/2019471084375130140">原帖 ↗</a></sub>
<p>面向镜头的形变网格、无光照材质与法线贴图假方向光</p>
<sub>关联风格: <a href="styles/silhouette/">剪影黑白</a></sub>
</td>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/d63c4858-075a-4601-8827-ce15b0d12efe" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1483094258076856320">噪声层构成的龙卷风</a></strong></p>
<sub>视频 · @Cyanilux · 2022-01-17 · <a href="https://x.com/Cyanilux/status/1483094258076856320">原帖 ↗</a></sub>
<p>Alpha 裁剪的滚动噪声叠层、顶点位移与粒子尾迹</p>
<sub>关联风格: <a href="styles/silhouette/">剪影黑白</a></sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/cb1ccdff-b7eb-418b-be98-f76d9b4e407a" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1638623920235356172">RenderTexture 驱动破碎</a></strong></p>
<sub>视频 · @Cyanilux · 2023-03-22 · <a href="https://x.com/Cyanilux/status/1638623920235356172">原帖 ↗</a></sub>
<p>用 Graphics.Blit 将射线命中位置写入遮罩，驱动表面破碎</p>
<sub>关联风格: <a href="styles/boomer-shooter/">复古 FPS</a></sub>
</td>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/a42790d7-ef63-4e9d-9c34-1624e0318f3a" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1524697139812573185">顶点位移触手</a></strong></p>
<sub>视频 · @Cyanilux · 2022-05-12 · <a href="https://x.com/Cyanilux/status/1524697139812573185">原帖 ↗</a></sub>
<p>用顶点位移驱动程序化触手形变</p>
<sub>关联风格: <a href="styles/lo-fi-surreal/">低保真超现实 / 丑美学</a></sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/4acc81d1-e91a-4ecf-91ae-bcc50e2597d7" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1467533351091376136">魔法斩击特效</a></strong></p>
<sub>视频 · @Cyanilux · 2021-12-05 · <a href="https://x.com/Cyanilux/status/1467533351091376136">原帖 ↗</a></sub>
<p>Shader 驱动的斩击特效，作者另有 Shader Graph 拆解</p>
<sub>关联风格: <a href="styles/anime-cel/">日式赛璐璐 2.5D</a></sub>
</td>
</tr>
</table>

### 像素与 2D

<table>
<tr>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/a26ff1b1-d8ed-4b82-a883-2bc1be40bce7" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1068933280005844992">像素瀑布拆解</a></strong></p>
<sub>视频 · @lunoland · 2018-12-01 · <a href="https://x.com/lunoland/status/1068933280005844992">原帖 ↗</a></sub>
<p>精灵图、Shader 与 13 组粒子系统叠加的像素瀑布</p>
<sub>关联风格: <a href="styles/pixel-art/">像素画</a></sub>
</td>
<td width="50%" valign="top">
<video src="https://github.com/user-attachments/assets/4a23baa7-ce56-433c-b969-b6d528a4736b" controls width="100%" playsinline></video>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1595484469699526665">抖动与像素化光照</a></strong></p>
<sub>视频 · @Cyanilux · 2022-11-23 · <a href="https://x.com/Cyanilux/status/1595484469699526665">原帖 ↗</a></sub>
<p>把光照分解为像素块与抖动网点的实验</p>
<sub>关联风格: <a href="styles/pixelated-3d/">像素化 3D</a></sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1847072515572507001"><img src="x-posts/previews/1847072515572507001.jpg" width="100%" alt="调色板驱动的像素光照"></a>
<p><strong><a href="https://homkathon.github.io/awesome-game-art-styles/x-posts/#post-1847072515572507001">调色板驱动的像素光照</a></strong></p>
<sub>图文 · @MadeInHevinis · 2024-10-18 · <a href="https://x.com/MadeInHevinis/status/1847072515572507001">原帖 ↗</a></sub>
<p>直接从精灵明暗调色板映射光照颜色</p>
<sub>关联风格: <a href="styles/pixel-art/">像素画</a></sub>
</td>
</tr>
</table>


---

如果这份列表帮你选定了画风，点个 ⭐ 能让更多开发者看到它。
