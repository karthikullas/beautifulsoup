
import sys
from pathlib import Path
from bs4 import BeautifulSoup, SoupStrainer


def main():
    if len(sys.argv) != 2:
        print("Usage: python task2_strainer.py <input_file>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"File not found: {path}")
        sys.exit(1)

    parser = "xml" if path.suffix.lower() == ".xml" else "html.parser"
    strainer = SoupStrainer("a")

    with path.open("r", encoding="utf-8", errors="replace") as file:
        soup = BeautifulSoup(file, parser, parse_only=strainer)

    for tag in soup.find_all("a"):
        print(tag)


if __name__ == "__main__":
    main()
