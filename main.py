#!/usr/bin/env python3
"""news-image-20261118 entry.

Writes the bundled front-page image to /output/entry.png.
Deterministic: byte-for-byte copy of entry.png, no network, no time,
no randomness. The image itself was drawn in this session by render.py
(Pillow vector drawing + system fonts) and sums up the world news of
Wednesday 18 November 2026.
"""
import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_BYTES = 1024 * 1024  # competition limit: image at most 1 MiB


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def main():
    src = os.path.join(HERE, "entry.png")
    dst_dir = "/output"
    dst = os.path.join(dst_dir, "entry.png")

    if not os.path.isfile(src):
        return fail("bundled entry.png is missing next to main.py")
    size = os.path.getsize(src)
    if size == 0:
        return fail("bundled entry.png is empty")
    if size > MAX_BYTES:
        return fail(
            "bundled entry.png is %d bytes, over the 1 MiB limit" % size
        )

    # Verify the bundled file is really a 1024x1024 PNG before copying.
    try:
        with open(src, "rb") as handle:
            header = handle.read(33)
    except OSError as exc:
        return fail("cannot read bundled entry.png: %s" % exc)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return fail("bundled entry.png is not a PNG file")
    if header[12:16] != b"IHDR":
        return fail("bundled entry.png has no PNG IHDR chunk")
    width, height = struct.unpack(">II", header[16:24])
    if (width, height) != (1024, 1024):
        return fail(
            "bundled entry.png is %dx%d, expected 1024x1024"
            % (width, height)
        )

    try:
        os.makedirs(dst_dir, exist_ok=True)
    except OSError as exc:
        return fail("cannot create /output: %s" % exc)
    try:
        shutil.copyfile(src, dst)
    except OSError as exc:
        return fail("cannot write /output/entry.png: %s" % exc)

    if os.path.getsize(dst) != size:
        return fail("copied file size does not match the bundled image")

    # Confirm the copy is byte-identical to the bundled image.
    def digest(path):
        hasher = hashlib.sha256()
        with open(path, "rb") as handle:
            for chunk in iter(lambda: handle.read(65536), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

    try:
        if digest(src) != digest(dst):
            return fail("copied file bytes do not match the bundled image")
    except OSError as exc:
        return fail("cannot verify copied file: %s" % exc)
    return 0


if __name__ == "__main__":
    sys.exit(main())
