#!/usr/bin/env python3
"""news-image-20261122 entry: copy the rendered front page to /output.

The image is entry.png beside this file, drawn by draw.py (kept in this
repository) from wire reports of Sunday 22 November 2026. Standard library
only, no network, deterministic: the same bytes are written on every run.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
