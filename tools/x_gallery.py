"""Build a static, consent-to-load X embed gallery from bilingual resource tables.

Official X embeds show media from the original post; this repo does not rehost videos.
"""
from html import escape
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
    rows = []
    for a, b in zip(en, zh):
        idx = groups_en.index(a['group'])
        rows.append(f'''<article class="post" data-group="{idx}">
  <div class="post-top"><span class="category en">{escape(a['group'])}</span><span class="category zh">{escape(b['group'])}</span><span class="date">{a['date']}</span></div>
  <h2 class="en">{escape(a['title'])}</h2><h2 class="zh">{escape(b['title'])}</h2>
  <p class="technique en">{escape(a['technique'])}</p><p class="technique zh">{escape(b['technique'])}</p>
  <p class="attribution"><span>@{escape(a['handle'])}</span><span aria-hidden="true">·</span><a href="{escape(a['style_url'], quote=True)}"><span class="en">{escape(a['style_title'])}</span><span class="zh">{escape(b['style_title'])}</span></a></p>
  <div class="player" id="post-{a['id']}"><button class="load" type="button" data-id="{a['id']}"><span class="play-icon" aria-hidden="true">▶</span><span class="en">Load original X post</span><span class="zh">加载 X 原帖 / 视频</span></button></div>
  <a class="original" href="{escape(a['url'], quote=True)}" target="_blank" rel="noopener noreferrer"><span class="en">Open original on X ↗</span><span class="zh">在 X 查看原帖 ↗</span></a>
</article>''')
    template = (ROOT / 'tools/x-gallery-template.html').read_text(encoding='utf-8')
    output = (template.replace('<!-- __FILTERS__ -->', groups)
              .replace('<!-- __POSTS__ -->', '\n'.join(rows))
              .replace('__POST_COUNT__', str(len(rows)))
              .replace('__GROUP_COUNT__', str(len(groups_en))))
    if '<!-- __POSTS__ -->' in output or '<!-- __FILTERS__ -->' in output:
        raise ValueError('X gallery template slots unresolved')
    target = ROOT / 'x-posts' / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(output, encoding='utf-8')
    return len(rows)


if __name__ == '__main__':
    print('built: x-posts/index.html (' + str(render()) + ' embeds)')
