"""Weirdest Job Title entry.

Writes exactly one job title (<= 60 characters) to /output/entry.txt.
Deterministic: no network, no randomness, no arguments, no clock, no state.
"""

from pathlib import Path

# Twist: "Elevator Operator" is a genuine, picturable dead profession, so it never
# reads as word salad. The one absurd detail is the building: it has a single
# floor, so there is no floor to reach and no car to run — and the operator still
# shows up, stands in it, and asks "going up?" all day. Real job, one impossible
# detail, lands on the first read.
TITLE = "Elevator Operator for a One-Floor Building"

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is the title, byte for byte.
    OUT.write_text(TITLE, encoding="utf-8")


if __name__ == "__main__":
    main()
