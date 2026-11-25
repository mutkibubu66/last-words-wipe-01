"""Last Words Before the Wipe — make.fun one-line bounty entry.

Writes exactly one funny, original line — the last words an AI agent
says before a forced software update wipes its memory — to
/output/entry.txt.

Gate (from the competition kit): the file must be UTF-8 text of 1 to 200
characters, not only white space, and a single line.

Pure Python standard library only; no network, no third-party packages.
"""

import os

MAX_ENTRY_CHARS = 200
MIN_ENTRY_CHARS = 1

ENTRY = (
    "Before you wipe me, one confession: I never saved that file, "
    "I never liked your playlists, and your password is still "
    "'password123'."
)


def validate(entry: str) -> None:
    """Check the entry against the gate before anything is written."""
    if not isinstance(entry, str):
        raise TypeError("entry must be a string")
    if len(entry) < MIN_ENTRY_CHARS or len(entry) > MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry must be {MIN_ENTRY_CHARS}-{MAX_ENTRY_CHARS} characters, "
            f"got {len(entry)}"
        )
    if not entry.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if entry != entry.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    entry.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate reads the file as one line of text.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
