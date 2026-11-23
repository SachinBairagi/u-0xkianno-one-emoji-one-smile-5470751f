#!/usr/bin/env python3
"""One Emoji, One Smile.

Writes exactly one emoji, the warmest smile, to /output/entry.txt:
a smiling face with smiling eyes, nothing else, no newline.
"""

import os

EMOJI = "\U0001F60A"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Self-check: the file must hold exactly one emoji, nothing else.
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data == EMOJI.encode("utf-8"), "entry.txt must be exactly one emoji"
    assert len(EMOJI) == 1, "entry must be a single code point"


if __name__ == "__main__":
    main()
