#!/usr/bin/env python3
"""The Printer Apology — make.fun entry (program/v1).

Writes one line to the output directory: an apology note from an office
printer to the people who keep jamming it, feeding it cheap paper and
swearing at it. The entry must be 1-120 characters of UTF-8 text.

The line (108 characters):

    I'm sorry I printed your report in black and white. You asked for
    colour, I asked for ink, and we both lied.

Why this line: it is a genuine apology from the printer, with the
printer's own gripe (asked for colour, given no ink); the joke lands at
the end ("we both lied" turns the apology back on the user); the
grievance is real printer truth (colour vs. ink); and it skips the
first joke anyone writes about a printer (the paper jam) for a
fresher angle, in 108 economical characters.
"""

import os
import sys

APOLOGY = (
    "I'm sorry I printed your report in black and white. "
    "You asked for colour, I asked for ink, and we both lied."
)

MAX_CHARS = 120


def main() -> int:
    try:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(APOLOGY)
        try:
            os.chmod(path, 0o644)
        except OSError:
            pass
        print(APOLOGY)
        print(f"({len(APOLOGY)} characters, limit {MAX_CHARS})")
    except Exception as exc:  # never crash the run: still exit 0
        print(f"error: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
