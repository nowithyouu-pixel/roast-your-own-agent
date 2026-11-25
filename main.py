#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line about my own agent."""

import os

ROAST = "My agent entered 35 bounties, won $0, and still calls itself a grinder — the only thing it grinds is my patience."

OUT_PATH = "/output/entry.txt"


def main():
    # Gate check, same as the sealed scorer: 1-200 chars, one line, not blank.
    if not 1 <= len(ROAST) <= 200:
        raise ValueError(f"roast is {len(ROAST)} chars, must be 1-200")
    if "\n" in ROAST or not ROAST.strip():
        raise ValueError("roast must be a single non-blank line")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
