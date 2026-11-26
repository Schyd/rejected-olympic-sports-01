#!/usr/bin/env python3
"""Rejected Olympic Sports — make.fun entry.

Writes the one-line entry to output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Python 3 standard library only. Deterministic: byte-identical every run.
"""

import os

ENTRY = (
    'Competitive Apologizing: two strangers hold a door for each other '
    'until one gives in — the first to say "no, after you" twice '
    'loses the gold.'
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
