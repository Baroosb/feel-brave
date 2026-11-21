#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI judge feel brave" bounty.

Writes one short text to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR when set, otherwise /output). The text is the
whole entry: a quiet scene meant to leave the reader steadier,
unhurried, and ready to move.
"""

import os
from pathlib import Path

TEXT = (
    "The night watchman walks his round with a small lamp. "
    "He is not afraid of the dark; he has met it every night for years, "
    "and it has never once hurried him. "
    "The lamp shows only the next step. "
    "It has always been enough. "
    "He takes it. Then the next."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
