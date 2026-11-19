#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261118 (v4).

Writes one image summarising 18 November 2026 world news to
/output/entry.png. The image is rendered by render.py in this repo;
this file validates the PNG (signature, 1024x1024, <=1 MiB) and
copies it to the output path.
"""
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = "/output/entry.png"


def main():
    if not os.path.exists(SRC):
        print("entry.png missing; run render.py first", file=sys.stderr)
        return 1
    with open(SRC, "rb") as f:
        data = f.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    w, h = struct.unpack(">II", data[16:24])
    if (w, h) != (1024, 1024):
        print(f"entry.png is {w}x{h}, expected 1024x1024", file=sys.stderr)
        return 1
    if len(data) > 1024 * 1024:
        print(f"entry.png is {len(data)} bytes, over 1 MiB", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print(f"wrote {OUT} ({len(data)} bytes, 1024x1024)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
