"""Build GitHub-compatible two-column X post galleries for both READMEs.

Resources in tools/resources*.md stay in the original machine-readable format
for the web X gallery. Use HTML tables as a responsive-ish grid because GitHub
strips custom CSS and doesn't reliably allow inline video players in READMEs.
"""
from html import escape
import hashlib
import json
from pathlib import Path

from x_gallery import parse_posts

ROOT = Path(__file__).resolve().parent.parent
PREVIEWS = ROOT / 'tools' / 'x_previews.json'
MEDIA = ROOT / 'tools' / 'x_media.json'
GALLERY = 'https://homkathon.github.io/awesome-game-art-styles/x-posts/'


def card(post: dict, manifest: dict, lang: str) -> str:
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
        f'<a href="{gallery}"><img src="{expected}" width="100%" alt="{escape(kind + ": " + post["title"], quote=True)}"></a>',
        f'<p><strong><a href="{gallery}">{title}</a></strong></p>',
        f'<sub>{kind} · @{author} · {post["date"]} · <a href="{original}">{source_label} ↗</a></sub>',
        f'<p>{technique}</p>',
        f'<sub>{style_label}: <a href="{style_url}">{style}</a></sub>',
        '</td>',
    ])


def make_grid(posts: list, manifest: dict, lang: str) -> str:
    rows = ['<table>']
    for i in range(0, len(posts), 2):
        rows.append('<tr>')
        for post in posts[i:i+2]:
            rows.append(card(post, manifest, lang))
        rows.append('</tr>')
    rows.append('</table>')
    return '\n'.join(rows)


def decorate_readme(resources: str, lang: str) -> str:
    manifest = json.loads(PREVIEWS.read_text(encoding='utf-8'))
    media = json.loads(MEDIA.read_text(encoding='utf-8'))
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
    caption = ('Large previews — click to play a video or view the original image.'
               if is_en else '大图预览 · 点击封面即可观看视频或查看原帖图片。')
    output = [heading, '', caption, '', intro]
    for group in groups:
        group_posts = [p for p in posts if p['group'] == group]
        output.extend(['', f'### {group}', '', make_grid(group_posts, manifest, lang)])
    return pre + '\n'.join(output).rstrip() + '\n' + after
