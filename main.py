#!/usr/bin/env python3
"""Everyday Things, Two Lines: rain, explained to a 10-year-old.

Line 1 explains rain in a single vivid sentence built on one analogy:
the sky as a bathtub tipped over. Line 2 says in one sentence why that
analogy works: what it maps, and what it leaves out.

The program writes exactly those two lines to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, or /output). The text is fixed, so every
run produces byte-identical output.
"""

import os

LINE_1 = "Rain is the sky tipping over a bathtub it forgot was full."
LINE_2 = (
    "It maps a whole skyful of water coming down from above, but leaves out "
    "that rain falls drop by drop for hours while a tub empties in one splash, "
    "and that clouds have no rim to tip."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def validate_entry(text: str) -> None:
    """Enforce the competition's gate before writing anything.

    The gate accepts UTF-8 text of 1 to 400 characters, not only white
    space; this entry must be exactly two non-empty lines, one sentence
    each, so a bad edit fails loudly here instead of shipping an entry
    the judge never sees.
    """
    if not 1 <= len(text) <= 400:
        raise ValueError(f"entry is {len(text)} characters, gate allows 1-400")
    if text.strip() == "":
        raise ValueError("entry is only white space")
    lines = text.splitlines()
    if len(lines) != 2 or any(line.strip() == "" for line in lines):
        raise ValueError("entry must be exactly two non-empty lines")
    for line in lines:
        if line.count(".") != 1 or not line.endswith("."):
            raise ValueError(f"each line must be one sentence: {line!r}")


def main() -> int:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
