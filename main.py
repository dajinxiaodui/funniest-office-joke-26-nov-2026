#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head: writes one original
one-line office joke to /output/entry.txt."""

import os
from pathlib import Path

JOKE = "My boss said I need to be more visible at work, so now I reply-all to everything, even the email telling us to stop replying-all."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(output_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
