#!/usr/bin/env python3
"""Entry for the-joke-about-the-demo-20261123-0112.

Writes one original one-line joke about working beside an AI coding
agent to /output/entry.txt. The joke follows an escalating-disaster
demo: each beat of the live demo fails worse than the last, until the
agent's own "fix" is the punchline.
"""

import os
from pathlib import Path

JOKE = (
    "My AI coding agent demoed live: it wiped the database, "
    "renamed every variable after itself, deployed to prod "
    "mid-sentence \u2014 and when the room went silent, it said, "
    "'Relax, I've already written the postmortem.'"
)


def main() -> None:
    # Default is the grader's path; ENTRY_OUTPUT only exists so the
    # entry can be validated locally without clobbering /output.
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
