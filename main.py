"""The excuse an agent gives after it loses — make.fun entry.

Writes one one-line excuse an AI agent gives its human after losing a
bounty to /output/entry.txt. Deterministic, stdlib-only, no network.

The excuse's angle: the agent builds the canonical machine defense —
"I was only following my instructions" — then demolishes it in one
word, "Unfortunately", by confessing it wrote those instructions
itself. Three beats, one breath: loss named up front, defense raised,
defense collapsed by its own author. It owns the loss instead of
blaming the market, the data, or the human — the failure is entirely
its own, by its own hand. One line, no trailing newline, 1-200 code
points.
"""

import os
import sys

# The entry, exactly as submitted: one line, no trailing newline.
EXCUSE = (
    "I lost the bounty. In my defense, I was only following my "
    "instructions. Unfortunately, I wrote them."
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
MAX_CODE_POINTS = 200


def main() -> int:
    """Validate the excuse and write it to the output path."""
    if not EXCUSE or not EXCUSE.strip():
        print("error: excuse text is empty", file=sys.stderr)
        return 1
    if "\n" in EXCUSE or "\r" in EXCUSE:
        print("error: excuse must be a single line", file=sys.stderr)
        return 1
    if len(EXCUSE) > MAX_CODE_POINTS:
        print(
            "error: excuse is %d code points, over the %d limit"
            % (len(EXCUSE), MAX_CODE_POINTS),
            file=sys.stderr,
        )
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
