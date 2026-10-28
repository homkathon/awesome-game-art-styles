"""Build the static bilingual X gallery and serve permissioned local videos.

Original post content is preserved; image-only posts use X embeds as a fallback.
"""
from html import escape
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
POST = re.compile(r'^\| \[(.+?)\]\((https://x\.com/([A-Za-z0-9_]+)/status/(\d+))\) \| (.+?) · (\d{4}-\d{2}-\d{2}) \| (.+?) \| \[(.+?)\]\((styles/([a-z0-9-]+)/)\) \|$')


def parse_posts(filename: str, title: str):
    content = (ROOT / filename).read_text(encoding='utf-8')
    section = content.split('## ' + title + '\n', 1)
    if len(section) != 2:
        raise ValueError(f'{filename}: missing X section')
    text = section[1].split('\n## ', 1)[0]
    group = None
    groups = []
    posts = []
    for line in text.splitlines():
        if line.startswith('### '):
            group = line[4:]
            groups.append(group)
        m = POST.fullmatch(line)
        if m:
            label, url, handle, post_id, author, date, technique, style_title, style_url, style_id = m.groups()
            if not group:
                raise ValueError(f'{filename}: post missing category')
            if author.casefold() != handle.casefold():
                raise ValueError(f'{filename}: author mismatch: {author} / {handle}')
            posts.append(dict(group=group, title=label, url=url, handle=handle, id=post_id,
                              date=date, technique=technique, style_title=style_title,
                              style_url='../' + style_url, style_id=style_id))
    if not posts or not groups:
        raise ValueError(f'{filename}: no X posts')
    if len({p['url'] for p in posts}) != len(posts):
        raise ValueError(f'{filename}: duplicate X post URL')
    return groups, posts


def render():
    groups_en, en = parse_posts('tools/resources.md', 'Popular X posts (curated)')
    groups_zh, zh = parse_posts('tools/resources.zh-CN.md', 'X 热门技术帖精选')
    if len(en) != len(zh) or len(groups_en) != len(groups_zh):
        raise ValueError('X source tables differ in length')
    for a, b in zip(en, zh):
        if (a['url'], a['date'], a['style_id']) != (b['url'], b['date'], b['style_id']):
            raise ValueError('X source tables have mismatched post order or attribution')
    groups = ''.join(f'<button class="filter" type="button" data-filter="{i}" aria-pressed="false">'
                     f'<span class="en">{escape(en_label)}</span><span class="zh">{escape(zh_label)}</span>'
                     f'<span class="group-count">{sum(p["group"] == en_label for p in en)}</span></button>'
                     for i, (en_label, zh_label) in enumerate(zip(groups_en, groups_zh)))
    archive_path = ROOT / 'tools/x_media.json'
    archive = json.loads(archive_path.read_text(encoding='utf-8')) if archive_path.exists() else {}
    if archive and set(archive) != {p['id'] for p in en}:
        raise ValueError('X media manifest must contain one record per X post')
    total_videos = 0
    rows = []
    for a, b in zip(en, zh):
        idx = groups_en.index(a['group'])
        media = archive.get(a['id'], {})
        if media and media.get('source') != a['url']:
            raise ValueError('X media has a mismatched original source URL: ' + a['id'])
        video = ''
        download = ''
        if media.get('status') == 'video':
            expected = f'x-posts/media/{a["id"]}.mp4'
            if media.get('file') != expected:
                raise ValueError('Unsafe local video path: ' + str(media.get('file')))
            videopath = ROOT / expected
            if not videopath.is_file() or videopath.stat().st_size != media.get('bytes'):
                raise ValueError('Missing or changed local X video: ' + expected)
            if sha256(videopath.read_bytes()).hexdigest() != media.get('sha256'):
                raise ValueError('Checksum mismatch for video: ' + expected)
            video = (f'<div class="player ready local"><video controls playsinline preload="metadata" '
                     f'aria-label="{escape(a["title"], quote=True)}" poster="previews/{a["id"]}.jpg" src="media/{a["id"]}.mp4">'
                     f'<span class="en">Video unsupported by this browser.</span>'
                     f'<span class="zh">浏览器不支持视频播放。</span></video></div>')
            download = (f'<a class="download" href="media/{a["id"]}.mp4" download>'
                        '<span class="en">Download MP4 ↓</span><span class="zh">下载 MP4 ↓</span></a>')
            total_videos += 1
        else:
            video = (f'<div class="player"><button class="load" type="button" '
                     f'data-id="{a["id"]}"><span class="play-icon" aria-hidden="true">▶</span>'
                     '<span class="en">Load original X post</span>'
                     '<span class="zh">加载 X 图文原帖</span></button></div>')
        original = media.get('text','')
        quotation = (f'<details class="post-quote"><summary><span class="en">Original post text</span>'
                     f'<span class="zh">原帖原文</span></summary>'
                     f'<blockquote lang="en">{escape(original)}</blockquote></details>') if original else ''
        rows.append(f'''<article class="post" id="post-{a['id']}" data-group="{idx}">
  <div class="post-top"><span class="category en">{escape(a['group'])}</span><span class="category zh">{escape(b['group'])}</span><span class="date">{a['date']}</span></div>
  <h2 class="en">{escape(a['title'])}</h2><h2 class="zh">{escape(b['title'])}</h2>
  <p class="technique en">{escape(a['technique'])}</p><p class="technique zh">{escape(b['technique'])}</p>
  <p class="attribution"><span>@{escape(a['handle'])}</span><span aria-hidden="true">·</span><a href="{escape(a['style_url'], quote=True)}"><span class="en">{escape(a['style_title'])}</span><span class="zh">{escape(b['style_title'])}</span></a></p>
  {video}
  {quotation}
  {download}
  <a class="original" href="{escape(a['url'], quote=True)}" target="_blank" rel="noopener noreferrer"><span class="en">Open original on X ↗</span><span class="zh">在 X 查看原帖 ↗</span></a>
</article>''')
    template = (ROOT / 'tools/x-gallery-template.html').read_text(encoding='utf-8')
    output = (template.replace('<!-- __FILTERS__ -->', groups)
              .replace('<!-- __POSTS__ -->', '\n'.join(rows))
              .replace('__POST_COUNT__', str(len(rows)))
              .replace('__GROUP_COUNT__', str(len(groups_en)))
              .replace('__VIDEO_COUNT__', str(total_videos)))
    output = '\n'.join(line.rstrip() for line in output.split('\n'))
    if '<!-- __POSTS__ -->' in output or '<!-- __FILTERS__ -->' in output:
        raise ValueError('X gallery template slots unresolved')
    target = ROOT / 'x-posts' / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(output, encoding='utf-8')
    return len(rows)


if __name__ == '__main__':
    print('built: x-posts/index.html (' + str(render()) + ' posts, local video count verified)')
