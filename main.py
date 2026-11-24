#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun bounty entry.

Writes a single deadpan error message a kitchen toaster would show its
owner, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The gate requires UTF-8 text of 1-120 characters, not only whitespace.
"""

import os
import sys

LINE = "ERROR 04: Your bread has achieved sentience and refuses to be toasted. Please unplug me and run."


def main() -> int:
    text = LINE
    if not (1 <= len(text) <= 120):
        print(f"entry must be 1-120 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the entry is exactly the line, nothing more.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
