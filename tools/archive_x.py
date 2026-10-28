#!/usr/bin/env python3
"""Archive videos from source X posts with curator-obtained republication permission.

Optional install: pip install yt-dlp  (and ffmpeg for oversized files)
Usage: PYTHONPATH=.weekly-dlp-tool python3 tools/archive_x.py
Only original author posts listed in the X gallery are considered. Keeps post URLs.
"""
import argparse
import concurrent.futures
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import subprocess
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from x_gallery import parse_posts

ROOT = Path(__file__).resolve().parent.parent
MEDIA = ROOT / 'x-posts' / 'media'
MANIFEST = ROOT / 'tools' / 'x_media.json'
FFMPEG = shutil.which('ffmpeg') or str(Path.home() / '.local' / 'bin' / 'ffmpeg')

class ExtractText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside = False
        self.chunks = []
    def handle_starttag(self, tag, attrs):
        if tag == 'p' and not self.chunks:
            self.inside = True
        if tag == 'br' and self.inside:
            self.chunks.append('\n')
    def handle_endtag(self, tag):
        if tag == 'p':
            self.inside = False
    def handle_data(self, data):
        if self.inside:
            self.chunks.append(data)


def fetch_original(post):
    url = 'https://publish.twitter.com/oembed?' + urlencode({'url':post['url'], 'omit_script':'true'})
    try:
        req = Request(url,headers={'User-Agent':'Mozilla/5.0'})
        data=json.load(urlopen(req,timeout=12))
        parser=ExtractText()
        parser.feed(data['html'])
        original=''.join(parser.chunks).strip()
        return {'text': original, 'author_name': data.get('author_name',''), 'source': post['url']}
    except Exception as e:
        return {'text':'', 'author_name':'', 'source':post['url'], 'metadata_error':str(e)[:120]}


def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):
            h.update(chunk)
    return h.hexdigest()


def transcode_if_needed(path, max_bytes):
    if path.stat().st_size <= max_bytes:
        return path
    ff=Path(FFMPEG)
    if not ff.exists():
        raise RuntimeError('oversize file and ffmpeg is missing')
    destination = path.with_suffix('.small.mp4')
    cmd=[str(ff),'-y','-hide_banner','-loglevel','error','-i',str(path),'-vf',
         'scale=w=960:h=-2:force_original_aspect_ratio=decrease', '-c:v','libx264','-preset','fast',
         '-crf','27','-pix_fmt','yuv420p','-c:a','aac','-b:a','96k','-movflags','+faststart',str(destination)]
    r=subprocess.run(cmd,timeout=120,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    if r.returncode!=0:
        raise RuntimeError('ffmpeg: '+r.stderr[-300:])
    if destination.stat().st_size > max_bytes:
        raise RuntimeError('compressed file still oversize')
    path.unlink()
    destination.replace(path)
    return path


def archive(post,max_bytes):
    status=post['id']
    filename = status + '.mp4'
    final = MEDIA/filename
    if final.exists() and final.stat().st_size>1000:
        return {'status':'video','file':'x-posts/media/'+filename,'bytes':final.stat().st_size,'sha256':digest(final)},'cached'
    template = str(MEDIA/(status+'.%(ext)s'))
    command=[sys.executable,'-m','yt_dlp','--no-playlist','--no-progress','--no-warnings',
       '--retries','1','--fragment-retries','1','--socket-timeout','10','--format',
       'best[ext=mp4][height<=720]/best[ext=mp4]/best',
       '--merge-output-format','mp4','--remux-video','mp4']
    if Path(FFMPEG).exists():
        command.extend(['--ffmpeg-location',str(FFMPEG)])
    command.extend(['-o',template,post['url']])
    try:
        r=subprocess.run(command,cwd=str(ROOT),timeout=85,capture_output=True,text=True)
        files=list(MEDIA.glob(status+'.*'))
        if r.returncode!=0 or not final.exists():
            for p in files:
                if p.is_file():p.unlink()
            combined=(r.stdout+'\n'+r.stderr)[-450:]
            kind = 'no_video' if 'No video could be found' in combined or 'not contain a video' in combined or 'No video formats found' in combined else 'unavailable'
            return {'status':kind,'error':combined.replace('\n',' ').strip()[:300]},kind
        transcode_if_needed(final,max_bytes)
        return {'status':'video','file':'x-posts/media/'+filename,'bytes':final.stat().st_size,'sha256':digest(final)},'downloaded'
    except Exception as e:
        return {'status':'unavailable','error':str(e)[:260]},'error'


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--workers',type=int,default=2)
    ap.add_argument('--max-file-mib',type=int,default=35)
    args=ap.parse_args()
    MEDIA.mkdir(parents=True,exist_ok=True)
    _,posts=parse_posts('tools/resources.md','Popular X posts (curated)')
    def process(post):
        attribution=fetch_original(post)
        media,note=archive(post,args.max_file_mib*1024*1024)
        media.update(attribution)
        media.pop('error', None)  # diagnostic output should not become public metadata
        media['id']=post['id']
        media['handle']=post['handle']
        return media,note
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        results=list(executor.map(process,posts))
    data={media['id']:media for media,_ in results}
    MANIFEST.write_text(json.dumps(data,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
    counts={}
    for media,note in results:
        counts[media['status']]=counts.get(media['status'],0)+1
        print(f"{media['id']} {media['status']} {media.get('bytes',0)} {note} {media.get('error','')[:120]}",flush=True)
    print('TOTAL',counts, 'MB',round(sum(x.get('bytes',0) for x in data.values())/1e6,1), flush=True)

if __name__=='__main__':
    main()
