"""Write the competition entry text to entry.txt in the output directory.

Standard library only. The output directory is $MAKEFUN_OUTPUT_DIR when set
and non-empty, otherwise /output. The directory is created if missing.
"""

import os

TEXT = "It's fine. I have backed everything up to /tmp.\n"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
