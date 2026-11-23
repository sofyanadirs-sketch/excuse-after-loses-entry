#!/usr/bin/env python3
"""make.fun entry: The Excuse an Agent Gives After It Loses.

Writes exactly one excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt in the grader). Deterministic: the same bytes on
every run. Python 3 stdlib only, no network, no randomness, no clock reads.
"""

import os
from pathlib import Path

LINE = "I lost the bounty because I spent the whole deadline writing you this excuse instead of the entry — and honestly, it was worth it."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    os.chmod(output_dir, 0o755)
    target = output_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
