#!/usr/bin/env python3
"""The Most Shameless Lie — make.fun entry.

Writes one lie (1-5 words, 1-88 chars) to /output/entry.txt, then
reads it back to verify the file matches the entry.
Python 3, standard library only. No network.
"""

import os
import sys

LINE = "I never sent that email."
MAX_CHARS = 88


def validate(line: str) -> str | None:
    """Return an error message if line breaks the brief, else None.

    The brief asks for exactly one non-empty line: a lie of 1-5 words
    and 1-88 characters, with no line breaks inside it.
    """
    if not line.strip():
        return "entry must not be empty"
    if "\n" in line or "\r" in line:
        return "entry must be a single line"
    words = line.split()
    if not 1 <= len(words) <= 5:
        return "entry must be 1-5 words"
    if not 1 <= len(line) <= MAX_CHARS:
        return "entry must be 1-88 characters"
    return None


def main() -> int:
    error = validate(LINE)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    expected = LINE + "\n"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(expected)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != expected:
        print("read-back mismatch: entry.txt does not match the entry", file=sys.stderr)
        return 1
    error = validate(written.rstrip("\n"))
    if error is not None:
        print(f"read-back failed validation: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
