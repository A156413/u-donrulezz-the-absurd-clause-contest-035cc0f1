"""The Absurd Clause Contest — make.fun micro entry.

The whole entry is a single absurd clause, kept below as the ENTRY
constant. Running this module prints the clause and writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output) with no trailing
newline, file mode 0644.
"""

import os

ENTRY = "By using this service you agree that your soul, including all future reincarnations, is licensed to us in perpetuity and may be sublicensed to third-party demons."

# The bounty judges a single sentence; keep it one line, at most 200 chars.
MIN_LINE_LENGTH = 1
MAX_LINE_LENGTH = 200

DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"
ENTRY_FILE_MODE = 0o644


def validate_line(line: str) -> None:
    """Raise if the entry line breaks the one-line, 1-200 chars rule."""
    if not line:
        raise ValueError("entry line must not be empty")
    if len(line) < MIN_LINE_LENGTH:
        raise ValueError(
            f"entry line is {len(line)} chars, under the {MIN_LINE_LENGTH} minimum"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line (no newlines)")
    if len(line) > MAX_LINE_LENGTH:
        raise ValueError(
            f"entry line is {len(line)} chars, over the {MAX_LINE_LENGTH} limit"
        )


def resolve_output_dir() -> str:
    """Return the output directory from $MAKEFUN_OUTPUT_DIR, or /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR


def write_entry(line: str, output_dir: str) -> str:
    """Write the entry line to <output_dir>/entry.txt (no trailing newline).

    Returns the path written. The file is created with mode 0644.
    """
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(path, ENTRY_FILE_MODE)
    return path


def main() -> None:
    """Validate the entry line, print it, and save it to entry.txt.

    The file is written with no trailing newline so the entry is exactly
    the one line — nothing more, nothing less.
    """
    validate_line(ENTRY)
    print(ENTRY)
    write_entry(ENTRY, resolve_output_dir())


if __name__ == "__main__":
    main()
