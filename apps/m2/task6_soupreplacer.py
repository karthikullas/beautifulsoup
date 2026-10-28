
import sys
from pathlib import Path

from bs4 import BeautifulSoup, SoupReplacer


def main():
    if len(sys.argv) not in (2, 3):
        print(
            "Usage: python task6_soupreplacer.py "
            "<input_file> [output_file]"
        )
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.is_file():
        print(f"File not found: {input_path}")
        sys.exit(1)

    output_path = (
        Path(sys.argv[2])
        if len(sys.argv) == 3
        else input_path.with_name(
            input_path.stem + "_replaced" + input_path.suffix
        )
    )

    parser = "xml" if input_path.suffix.lower() == ".xml" else "html.parser"

    with input_path.open("r", encoding="utf-8", errors="replace") as file:
        soup = BeautifulSoup(
            file,
            parser,
            replacer=SoupReplacer("b", "blockquote"),
        )

    output_path.write_text(str(soup), encoding="utf-8")
    print(f"Replaced <b> tags during parsing. Output saved to: {output_path}")


if __name__ == "__main__":
    main()
