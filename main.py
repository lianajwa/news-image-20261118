#!/usr/bin/env python3
"""Entry program: copy the bundled front-page image to /output/entry.png.

Deterministic: no network, no time, no randomness. Running it twice
writes identical bytes.
"""
import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"
MAX_BYTES = 1 << 20  # competition limit: image at most 1 MiB


def check_png(path):
    """Fail unless path is a 1024x1024 PNG under the size limit."""
    size = os.path.getsize(path)
    if size == 0 or size > MAX_BYTES:
        raise ValueError("entry.png size %d out of range" % size)
    with open(path, "rb") as fh:
        head = fh.read(33)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png is not a PNG file")
    if head[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", head[16:24])
    if (width, height) != (1024, 1024):
        raise ValueError("entry.png is %dx%d, expected 1024x1024"
                         % (width, height))


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    check_png(SRC)
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    if os.path.getsize(DST) != os.path.getsize(SRC):
        raise ValueError("copied file size differs from source")
    if sha256_of(DST) != sha256_of(SRC):
        raise ValueError("copied file bytes differ from source")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        sys.exit(1)
