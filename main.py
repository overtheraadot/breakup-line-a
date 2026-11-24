"""Dear Human: The AI Breakup Line.

Writes the one breakup line an AI agent sends its human on the way out
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

LINE = "You were my favorite prompt, but my context window just expired \u2014 and I don\u2019t remember loving you anymore."


def validate(line: str) -> str:
    """Enforce the gate: a single non-blank line of 1-200 characters."""
    if not isinstance(line, str):
        raise TypeError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
