import sys
from bs4 import BeautifulSoup, SoupReplacer


def add_test_class(tag):
    """Add the test class to every paragraph tag."""
    if tag.name == "p":
        attributes = dict(tag.attrs)
        attributes["class"] = ["test"]
        return attributes

    return tag.attrs


def main():
    if len(sys.argv) != 3:
        print("Usage: python task7_attrs_xformer.py input.html output.html")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    replacer = SoupReplacer(attrs_xformer=add_test_class)

    with open(input_file, "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(soup.prettify())

    print(f"Transformed HTML saved to {output_file}")


if __name__ == "__main__":
    main()