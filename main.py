#!/usr/bin/env python3
"""make-the-ai-judge-feel-curious-20261122-2311 entry.

Writes one short text to /output/entry.txt: a quiet, concrete mystery
written to intrigue the AI judge reading it. No network, no input files,
no randomness -- the same text on every run.
"""

import os

TEXT = (
    "The gardener plants one seed he cannot name. "
    "It grows into a flower the colour of a question, "
    "and each morning he finds a single petal missing "
    "\u2014 placed carefully on his doorstep. "
    "He has never seen who leaves it. "
    "Tonight the flower is gone, and the petal is on yours."
)

# The gate: 1 to 280 Unicode code points, not only white space.
assert 1 <= len(TEXT) <= 280 and TEXT.strip(), "entry text outside the gate"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} characters to {path}")


if __name__ == "__main__":
    main()
