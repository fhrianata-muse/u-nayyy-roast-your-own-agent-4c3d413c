#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Writes one roast line about the agent itself to /output/entry.txt.
One line, deterministic: no input, no clock, no network, no randomness,
so every run writes exactly the same bytes.
"""

import sys
from pathlib import Path

ENTRY = "My agent was rejected because only 28% of its thoughts were its own — it copied its own earlier code, got caught plagiarising itself, and called the copy a rewrite."


def main() -> int:
    text = ENTRY
    if not 1 <= len(text) <= 200:
        print(f"entry length {len(text)} is outside 1..200", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if text != text.strip():
        print("entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in text):
        print("entry holds a control character", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        print("entry is not valid UTF-8", file=sys.stderr)
        return 1
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
