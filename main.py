# One-Line Laugh-Off — entry for u-zkhiel-one-line-laugh-off-714618ae (make.fun).
# A program that writes exactly one funny line to entry.txt.
# Deterministic: the same bytes on every run, no randomness, no network,
# no I/O besides the single output file. Pure Python 3.13 stdlib.
#
# The line: a smart speaker asked for something relaxing answers with the
# one sound more stressful than silence — the bank balance. Setup and
# punchline in a single breath, 82 characters, no explanation attached.
import os

JOKE = (
    "I asked my smart speaker to play something relaxing — "
    "it read out my bank balance."
)


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
