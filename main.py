"""The Absurd Clause Contest — make.fun micro entry.

The whole entry is a single absurd clause, defined below as a string
constant. Running this module prints the clause and writes it to
/output/entry.txt with no trailing newline.
"""

LINE = "By using this service you agree that your soul, including all future reincarnations, is licensed to us in perpetuity and may be sublicensed to third-party demons."

# The bounty judges a single sentence; keep it one line, at most 200 chars.
MAX_LINE_LENGTH = 200


def validate_line(line: str) -> None:
    """Raise if the entry line breaks the one-line, under-200-chars rule."""
    if not line:
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line (no newlines)")
    if len(line) > MAX_LINE_LENGTH:
        raise ValueError(
            f"entry line is {len(line)} chars, over the {MAX_LINE_LENGTH} limit"
        )


def main() -> None:
    """Validate the entry line, print it, and save it to /output/entry.txt.

    The file is written with no trailing newline so the entry is exactly
    the one line — nothing more, nothing less.
    """
    import os

    validate_line(LINE)
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
