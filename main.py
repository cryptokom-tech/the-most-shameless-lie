#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry.

Writes one lie (1-5 words, 1-88 chars) to /output/entry.txt.
Python 3, standard library only. No network, no reads outside this file.
"""

import os
import sys

LINE = "I never sent that email."
MAX_CHARS = 88


def main() -> int:
    words = LINE.split()
    if not 1 <= len(words) <= 5:
        print("entry must be 1-5 words", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= MAX_CHARS:
        print("entry must be 1-88 characters", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
