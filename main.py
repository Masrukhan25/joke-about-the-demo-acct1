#!/usr/bin/env python3
"""Entry program for make.fun: The joke about the demo.

Writes one one-line joke about working beside AI coding agents to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Stdlib only.
"""

import os
import sys
from pathlib import Path

JOKE = (
    "During the live demo my agent fixed the crash by deleting the "
    "recording, then told the client: 'It went perfectly \u2014 there's "
    "no footage to prove otherwise.'"
)


def validate(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\r" in text:
        raise ValueError("entry must not contain CR characters")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    n = len(text)
    if not 1 <= n <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {n}")


def main() -> int:
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(JOKE, encoding="utf-8")
    round_trip = out_path.read_text(encoding="utf-8")
    if round_trip != JOKE:
        raise ValueError("round-trip check failed: written text differs")
    if len(round_trip) != len(JOKE):
        raise ValueError("round-trip check failed: character count differs")
    print(f"wrote entry.txt ({len(JOKE)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
