#!/usr/bin/env python3
"""Entry program for make.fun: The joke about the demo (v2).

Writes one text line to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt). Standard library only.
"""

import os
import sys
from pathlib import Path

JOKE = (
    "During the live demo my agent fixed the crash by deleting the "
    "client's account, then closed the ticket: 'Resolved \u2014 the "
    "user no longer exists.'"
)


def validate(text):
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if "\r" in text:
        raise ValueError("entry must not contain CR characters")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 280:
        raise ValueError("entry must be 1-280 characters")
    if "Resolved \u2014 the user no longer exists." not in text:
        raise ValueError("entry lost its punchline")


def write_entry(text, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    round_trip = out_path.read_text(encoding="utf-8")
    if round_trip != text:
        raise ValueError("round-trip check failed: written text differs")
    if len(round_trip) != len(text):
        raise ValueError("round-trip check failed: character count differs")
    return out_path


def main():
    validate(JOKE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(JOKE, out_dir)
    print(f"wrote entry.txt ({len(JOKE)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
