#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes one line (under 200 characters) that reads as a hilarious
autocorrect fail to /output/entry.txt.
The intended phrase was "your hand in mine"; autocorrect served
"your ham in mine" instead, right in the middle of a marriage
proposal text — one wrong word, maximum damage.
"""

import os
import sys

ENTRY = "Babe, tonight at dinner I'm getting down on one knee, taking your ham in mine, and asking you to marry me"

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 199


def validate(text: str) -> None:
    """Raise ValueError unless text is a single non-empty line under 200 chars."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry must be under 200 characters, got {len(text)}")
    if len(text) < 1:
        raise ValueError("entry must be at least 1 character")


def main() -> int:
    validate(ENTRY)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Read back and verify exactly what was written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    line = written.rstrip("\n")
    validate(line)
    if line != ENTRY:
        raise ValueError("read-back does not match ENTRY")
    print(f"Wrote {OUTPUT_PATH}: {len(line)} chars")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
