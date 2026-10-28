#!/usr/bin/env python3
"""Generate lightweight 560x315 JPEG covers for curated X posts.

Use `python3 tools/make_x_previews.py` on a machine with ffmpeg. The original
post images for image-only posts are obtained from the original X tweet via
FXTwitter's public tweet metadata; source URLs are documented in x_previews.json.
The generated JPEGs are committed and do not require ffmpeg at README build time.
"""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from x_gallery import parse_posts

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'x-posts' / 'previews'
MANIFEST = ROOT / 'tools' / 'x_previews.json'
SOURCE = ROOT / 'tools' / 'x_media.json'
FFMPEG = shutil.which('ffmpeg') or str(Path.home() / '.local' / 'bin' / 'ffmpeg')
SIZE = '560:315'
FONT = next((str(p) for p in [Path('/System/Library/Fonts/Supplemental/Arial.ttf'),Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')] if p.is_file()), None)


def first_photo(post):
    url = f'https://api.fxtwitter.com/{post["handle"]}/status/{post["id"]}'
    req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
    with urlopen(req, timeout=12) as response:
        result = json.load(response)
    tweet = result.get('tweet') or {}
    if str(tweet.get('id')) != post['id']:
        raise ValueError('Original post ID does not match: ' + post['id'])
    actual = (tweet.get('author') or {}).get('screen_name','')
    if actual.casefold() != post['handle'].casefold():
        raise ValueError(f'Original post author mismatch: {actual} / {post["handle"]}')
    photos = (tweet.get('media') or {}).get('photos') or []
    if not photos:
        raise ValueError('Original X post has no photo: ' + post['id'])
    image_url = photos[0]['url']
    parsed = urlparse(image_url)
    if parsed.scheme != 'https' or parsed.netloc != 'pbs.twimg.com':
        raise ValueError('Unexpected source media host for '+post['id'])
    return image_url


def run_ffmpeg(source, dest, is_video):
    # A title-free 16:9 card keeps the art legible even for portrait source images.
    # The small centre play symbol is baked into video thumbnails for GitHub Markdown.
    filters = [f'scale={SIZE}:force_original_aspect_ratio=decrease:force_divisible_by=2',
               'setsar=1', 'pad=560:315:(ow-iw)/2:(oh-ih)/2:color=0x15171b']
    if is_video:
        filters.append('drawbox=x=246:y=130:w=68:h=55:color=black@0.60:t=fill')
        if FONT:
            filters.append(f"drawtext=fontfile={FONT}:text='▶':fontcolor=white:fontsize=38:x=(w-text_w)/2:y=(h-text_h)/2")
    cmd = [FFMPEG, '-y', '-hide_banner', '-loglevel', 'error']
    if is_video:
        cmd.extend(['-ss', '1.0'])
    cmd.extend(['-i', str(source), '-vf', ','.join(filters), '-frames:v', '1',
                '-q:v', '5', '-update', '1', str(dest)])
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=35)
    if res.returncode or not dest.is_file() or dest.stat().st_size < 2000:
        raise RuntimeError('Preview generation failed: '+res.stderr[-300:])


def main():
    OUT.mkdir(exist_ok=True, parents=True)
    if not Path(FFMPEG).is_file():
        raise RuntimeError('Please install ffmpeg first')
    _, posts = parse_posts('tools/resources.md', 'Popular X posts (curated)')
    media = json.loads(SOURCE.read_text())
    if {p['id'] for p in posts} != set(media):
        raise ValueError('Media manifest does not match post IDs')
    result = {}
    for post in posts:
        id = post['id']
        m = media[id]
        video = m['status'] == 'video'
        src = ROOT / m['file'] if video else first_photo(post)
        dst = OUT / (id+'.jpg')
        if video:
            run_ffmpeg(src, dst, True)
        else:
            # Download only the original post's image, not a third-party preview.
            original = OUT / (id+'.source')
            try:
                with urlopen(Request(src, headers={'User-Agent':'Mozilla/5.0'}), timeout=15) as response:
                    original.write_bytes(response.read(16*1024*1024+1))
                if original.stat().st_size > 16*1024*1024:
                    raise ValueError('Original image exceeds 16 MiB')
                run_ffmpeg(original, dst, False)
            finally:
                original.unlink(missing_ok=True)
        digest = hashlib.sha256(dst.read_bytes()).hexdigest()
        result[id] = {'file':f'x-posts/previews/{id}.jpg',
                      'source':post['url'] if video else src,
                      'kind':'video-frame' if video else 'original-post-photo',
                      'bytes':dst.stat().st_size, 'sha256':digest}
        print(id, result[id]['kind'], dst.stat().st_size, 'bytes', flush=True)
    MANIFEST.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)+'\n')
    print('Generated',len(result),'covers in',OUT)


if __name__ == '__main__':
    main()
