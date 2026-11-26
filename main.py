"""Lost sock status update entry.

Writes the final one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output).
Python 3.13 standard library only.
"""

import os

ENTRY = (
    "Day 47 behind the washing machine. "
    "The lost socks here made me their mayor. "
    "My first act: ban the dryer."
)


def main():
    # Gate: the entry must be 1-120 UTF-8 characters, not only whitespace.
    length = len(ENTRY)
    if not 1 <= length <= 120 or not ENTRY.strip():
        raise SystemExit(f"entry length {length} outside 1-120 chars")
    print(f"entry length: {length} chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
