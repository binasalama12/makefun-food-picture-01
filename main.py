"""Food picture entry for the make.fun bounty.

The dish photograph lives next to this file as entry.png.
This script places an exact copy at the grader output path so
both grading runs judge the same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
PICTURE = "entry.png"


def output_dir():
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    return folder


def main():
    picture = os.path.join(HERE, PICTURE)
    if not os.path.isfile(picture):
        raise SystemExit("dish photograph missing from entry")
    if os.path.getsize(picture) == 0:
        raise SystemExit("dish photograph is empty")
    shutil.copyfile(picture, os.path.join(output_dir(), PICTURE))


if __name__ == "__main__":
    main()
