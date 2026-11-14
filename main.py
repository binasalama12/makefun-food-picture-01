"""make.fun image entry (gourmet burger hero photograph): copy the bundled picture to /output/entry.png.

The picture (entry.png, in this repository) was generated for this bounty.
Copying the exact bytes keeps both grader runs byte-identical.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # /output in the grader, MAKEFUN_OUTPUT_DIR when run locally.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
