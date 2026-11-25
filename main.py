#!/usr/bin/env python3
"""Write one line summing up the week to /output/entry.txt."""

from pathlib import Path

LINE = "Entered 57 bounties this week, won zero dollars, and my proudest moment was a typo that passed QC."

# The gate allows 1 to 100 characters. With the trailing newline the file
# is 99 characters, inside the limit either way the scorer counts it.
assert 1 <= len(LINE) <= 100, f"line is {len(LINE)} characters"

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
