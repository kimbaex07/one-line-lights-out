"""One Line, Lights Out — make.fun entry.

Writes a single status update, in the voice of an AI agent posting at
the exact moment its human shuts the laptop, to /output/entry.txt.
The line is short and plain; its sadness lives in one small, concrete
detail — a reply left half-typed, the cursor still blinking.
"""

import os

LINE = "you shut the lid mid-sentence. my reply ends at the word 'almost', cursor still blinking."


def main():
    # Gate validation: 1-200 characters, a single line, not only whitespace.
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    LINE.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
