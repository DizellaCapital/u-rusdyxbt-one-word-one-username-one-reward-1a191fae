"""One Word, One Username, One Reward entry program.

Writes our own make.fun username, a single word, to
MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only. The username is one
word of at most 30 characters, with no spaces or padding.
"""

import os
import sys

USERNAME = "dizellacapital"


def main():
    if not (1 <= len(USERNAME) <= 30):
        print(f"entry must be 1-30 characters, got {len(USERNAME)}", file=sys.stderr)
        return 1
    if USERNAME != USERNAME.strip() or any(ch.isspace() for ch in USERNAME):
        print("entry must be a single word with no spaces or padding", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(USERNAME)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != USERNAME:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
