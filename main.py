#!/usr/bin/env python3
"""news-image-20261118 entry (Python 3.13, standard library only).

The repository holds the finished image (entry.png), drawn from scratch
for this bounty. This program copies it to the output directory as
entry.png. It touches no network, writes the same bytes on every run,
and uses only the standard library.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENTRY = "entry.png"


def main() -> None:
    # A plain byte copy: the output is identical on every run, and the
    # program never touches the network.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / ENTRY, out_dir / ENTRY)


if __name__ == "__main__":
    main()
