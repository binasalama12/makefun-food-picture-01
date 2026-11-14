"""Gourmet cheeseburger photo copier.

Copies the winning cheeseburger shot (entry.png, sitting next to this
script) byte-for-byte into the output directory so the make.fun judge
sees exactly the dish we plated: a glossy brioche bun, molten cheddar
dripping over a flame-grilled patty, crisp lettuce and a tomato slice.
No pixels are touched; the file is delivered as-is.
"""

import os
import shutil

BURGER_SOURCE_NAME = "entry.png"
BURGER_OUTPUT_ENV = "MAKEFUN_OUTPUT_DIR"
BURGER_DEFAULT_OUTPUT = "/output"


def burger_output_path():
    out_dir = os.environ.get(BURGER_OUTPUT_ENV, BURGER_DEFAULT_OUTPUT)
    return os.path.join(out_dir, BURGER_SOURCE_NAME)


def burger_source_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, BURGER_SOURCE_NAME)


def serve_cheeseburger():
    source = burger_source_path()
    if not os.path.isfile(source):
        raise SystemExit(f"missing cheeseburger photo: {source}")
    if os.path.getsize(source) == 0:
        raise SystemExit(f"empty cheeseburger photo: {source}")
    destination = burger_output_path()
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    shutil.copyfile(source, destination)
    copied_bytes = os.path.getsize(destination)
    print(f"served cheeseburger photo -> {destination} ({copied_bytes} bytes)")


if __name__ == "__main__":
    serve_cheeseburger()
