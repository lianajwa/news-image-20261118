#!/usr/bin/env python3
"""news-image-20261118 entry.

Writes the bundled front-page image to /output/entry.png.
Deterministic: byte-for-byte copy of entry.png, no network, no time,
no randomness. The image itself was drawn in this session by render.py
(Pillow vector drawing + system fonts) and sums up the world news of
Wednesday 18 November 2026.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    dst_dir = "/output"
    dst = os.path.join(dst_dir, "entry.png")
    os.makedirs(dst_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
