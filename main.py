"""Deliver the Tuesday 24 November 2026 front page to the grader.

The picture itself lives in design.html and was rendered by hand to
entry.png (1024 by 1024, one PNG, under 1 MiB) before this program
ever runs. This program draws nothing, reads no network and keeps no
state: it checks the committed bytes look like an image of the right
size, then copies them into the grader's output folder. Two runs
therefore always produce the same file.
"""

import os
import sys
from pathlib import Path

IMAGE = "entry.png"
LIMIT = 1024 * 1024
MAGIC = (b"\x89PNG\r\n\x1a\n", b"\xff\xd8\xff")


def load_image() -> bytes:
    folder = Path(__file__).resolve().parent
    try:
        return (folder / IMAGE).read_bytes()
    except OSError as exc:
        print(f"entry image missing or unreadable: {exc}", file=sys.stderr)
        raise SystemExit(1)


def check_image(data: bytes) -> None:
    if not data.startswith(MAGIC):
        print("entry image is neither PNG nor JPEG", file=sys.stderr)
        raise SystemExit(1)
    if len(data) > LIMIT:
        print(f"entry image is {len(data)} bytes, over the 1 MiB cap", file=sys.stderr)
        raise SystemExit(1)


def main() -> None:
    data = load_image()
    check_image(data)
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    target = out / IMAGE
    target.write_bytes(data)
    if target.stat().st_size != len(data):
        print("short write of entry image", file=sys.stderr)
        raise SystemExit(1)
    print(f"wrote {target} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
