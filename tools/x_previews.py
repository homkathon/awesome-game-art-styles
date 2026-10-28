"""Build GitHub native MP4-player and image grids for both READMEs.

Original source tables remain machine-readable for the web gallery. Video player
assets must be hosted on github.com/user-attachments rather than repository raw.
"""
from html import escape
import hashlib
import json
import re
from pathlib import Path

from x_gallery import parse_posts

ROOT = Path(__file__).resolve().parent.parent
PREVIEWS = ROOT / 'tools' / 'x_previews.json'
MEDIA = ROOT / 'tools' / 'x_media.json'
VIDEO_ASSETS = ROOT / 'tools' / 'x_video_assets.json'
GALLERY = 'https://homkathon.github.io/awesome-game-art-styles/x-posts/'


def card(post: dict, manifest: dict, video_assets: dict, lang: str) -> str:
    post_id = post['id']
    item = manifest[post_id]
    expected = f'x-posts/previews/{post_id}.jpg'
    if item.get('file') != expected:
        raise ValueError('Invalid image path for X post ' + post_id)
    file = ROOT / expected
    if not file.is_file() or file.stat().st_size != item['bytes']:
        raise ValueError('Missing or modified preview file for ' + post_id)
    if hashlib.sha256(file.read_bytes()).hexdigest() != item['sha256']:
        raise ValueError('Corrupted preview for ' + post_id)
    if item['kind'] not in ('video-frame', 'original-post-photo'):
        raise ValueError('Unknown preview type: ' + post_id)

    gallery = GALLERY + '#post-' + post_id
    if item['kind'] == 'video-frame':
        asset = video_assets.get(post_id)
        if not asset or not re.fullmatch(r'https://github\.com/user-attachments/assets/[0-9a-f-]{36}', asset):
            raise ValueError('Missing or invalid native video attachment for X post ' + post_id)
        # The GitHub Markdown renderer rewrites this hosted asset to a native
        # HTML5 player with controls and a signed media URL. Repository raw MP4s
        # do not receive this transformation.
        cover = f'<video src="{asset}" controls width="100%" playsinline></video>'
    else:
        cover = (f'<a href="{gallery}"><img src="{expected}" width="100%" '
                 f'alt="{escape(post["title"], quote=True)}"></a>')
    title = escape(post['title'])
    author = escape(post['handle'])
    technique = escape(post['technique'])
    style = escape(post['style_title'])
    style_url = escape(post['style_url'].removeprefix('../'), quote=True)
    original = escape(post['url'], quote=True)
    kind = ('Video' if item['kind'] == 'video-frame' else 'Image') if lang == 'en' else ('视频' if item['kind'] == 'video-frame' else '图文')
    source_label = 'Original post' if lang == 'en' else '原帖'
    style_label = 'Style' if lang == 'en' else '关联风格'
    return '\n'.join([
        '<td width="50%" valign="top">',
        cover,
        f'<p><strong><a href="{gallery}">{title}</a></strong></p>',
        f'<sub>{kind} · @{author} · {post["date"]} · <a href="{original}">{source_label} ↗</a></sub>',
        f'<p>{technique}</p>',
        f'<sub>{style_label}: <a href="{style_url}">{style}</a></sub>',
        '</td>',
    ])


def make_grid(posts: list, manifest: dict, video_assets: dict, lang: str) -> str:
    rows = ['<table>']
    for i in range(0, len(posts), 2):
        rows.append('<tr>')
        for post in posts[i:i+2]:
            rows.append(card(post, manifest, video_assets, lang))
        rows.append('</tr>')
    rows.append('</table>')
    return '\n'.join(rows)


def decorate_readme(resources: str, lang: str) -> str:
    manifest = json.loads(PREVIEWS.read_text(encoding='utf-8'))
    media = json.loads(MEDIA.read_text(encoding='utf-8'))
    video_assets = json.loads(VIDEO_ASSETS.read_text(encoding='utf-8'))
    if set(video_assets) != {p for p, m in media.items() if m['status'] == 'video'}:
        raise ValueError('Video attachment manifest must match the 17 video posts')
    if set(manifest) != set(media):
        raise ValueError('X preview manifest must match media source posts')

    is_en = lang == 'en'
    heading = '## Popular X posts (curated)' if is_en else '## X 热门技术帖精选'
    resource_name = 'tools/resources.md' if is_en else 'tools/resources.zh-CN.md'
    groups, posts = parse_posts(resource_name, 'Popular X posts (curated)' if is_en else 'X 热门技术帖精选')
    if resources.count(heading) != 1:
        raise ValueError('README X post section not found exactly once')
    if set(manifest) != {p['id'] for p in posts}:
        raise ValueError('X preview list does not match curated post tables')

    pre, rest = resources.split(heading, 1)
    end = rest.find('\n## ')
    body, after = (rest[:end], rest[end:]) if end >= 0 else (rest, '')
    # Intro stays sourced from original resources and is never duplicated.
    intro = body.split('\n### ', 1)[0].strip()
    caption = ('Play original MP4s directly using GitHub video controls; image-only posts show original photos.'
               if is_en else '直接在这里用 GitHub 原生播放器观看视频；没有视频的原帖展示图片。')
    output = [heading, '', caption, '', intro]
    for group in groups:
        group_posts = [p for p in posts if p['group'] == group]
        output.extend(['', f'### {group}', '', make_grid(group_posts, manifest, video_assets, lang)])
    return pre + '\n'.join(output).rstrip() + '\n' + after
