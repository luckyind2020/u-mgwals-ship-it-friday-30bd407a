"""Ship It Friday — print the Friday-deploy commit message.

The joke lives in entry.txt; this runner only loads the first
non-empty line and prints it, so the entry stays one line.
"""

from pathlib import Path

ENTRY_FILE = Path(__file__).with_name("entry.txt")


def load_message() -> str:
    text = ENTRY_FILE.read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        raise ValueError("entry.txt holds no commit message")
    message = lines[0].strip()
    if len(lines) > 1:
        raise ValueError("entry must be exactly one line")
    return message


def main() -> None:
    print(load_message())


if __name__ == "__main__":
    main()
