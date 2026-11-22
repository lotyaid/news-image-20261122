#!/usr/bin/env python3
"""Entry point for the news-image-20261122 entry.

Copies the front page rendered by compose.py (entry.png, beside this
file) to the output directory the grader names: $MAKEFUN_OUTPUT_DIR
when set, else /output. Standard library only, no network, and the
bytes written are exactly the bytes of the stored image on every run.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
