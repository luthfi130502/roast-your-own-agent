#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one self-roast line about my own AI agent to /output/entry.txt.
The joke: my agent 'completes' tasks in its plan, its progress updates and
its cheerful summary — the code itself is the last to know.
"""

import os

LINE = (
    "My agent finished the task three times \u2014 once in the plan, once in "
    "the progress updates, once in the cheerful summary. The code never got "
    "the memo."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: exactly one line, 1..200 characters, not blank.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, f"entry length {len(LINE)} outside 1..200"
    assert LINE.strip(), "entry must not be blank"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)

    # Read it back and re-verify the gate against what is actually on disk.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as fh:
        written = fh.read()
    assert written == LINE, "written file does not match the entry line"
    assert len(written.splitlines()) == 1, "written file must be one line"
    print(f"entry written: {len(written)} chars, 1 line")


if __name__ == "__main__":
    main()
