#!/usr/bin/env python3
"""Cache Steam screenshot URLs for every reference game in tools/styles.py into tools/screenshots.json.

Only needed when a game is added. Usage: python3 tools/fetch_screenshots.py
"""
import json
import time
import urllib.request
from pathlib import Path

import styles

HERE = Path(__file__).resolve().parent
OUT = HERE / "screenshots.json"


def main():
    cache = json.loads(OUT.read_text()) if OUT.exists() else {}
    for gid in sorted({g for s in styles.STYLES for g in s["games"]}):
        if str(gid) in cache:
            continue
        url = f"https://store.steampowered.com/api/appdetails?appids={gid}&filters=screenshots"
        data = json.load(urllib.request.urlopen(url, timeout=20))[str(gid)]
        shots = [s["path_thumbnail"].split("?")[0] for s in data.get("data", {}).get("screenshots", [])][:8]
        cache[str(gid)] = shots
        print(gid, len(shots))
        time.sleep(0.4)
    OUT.write_text(json.dumps(cache, indent=1, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
