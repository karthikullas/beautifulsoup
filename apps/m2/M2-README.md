Milestone 2
Part 1: SoupStrainer Applications
This part implements three applications using BeautifulSoup's SoupStrainer and the parse_only constructor argument.
Task 2 — Print all hyperlinks
File: apps/m2/task2_strainer.py
Uses SoupStrainer("a") to restrict parsing to anchor tags and prints the matching <a> elements.
Task 3 — Print all tags
File: apps/m2/task3_strainer.py
Uses SoupStrainer(True) to match all tags and prints the matching elements.
Observation: SoupStrainer(True) can be used to select all tags during parsing. It does not independently select text nodes outside matching tags.
Task 4 — Print tags with an ID attribute
File: apps/m2/task4_strainer.py
Uses SoupStrainer(attrs={"id": True}) to restrict parsing to tags that have an id attribute and prints those elements.
Running the applications
Run these commands from the repository root:
python apps/m2/task2_strainer.py "path\to\input.html"
python apps/m2/task3_strainer.py "path\to\input.html"
python apps/m2/task4_strainer.py "path\to\input.html"
The applications select html.parser for HTML files and the XML parser for files with the .xml extension.
Part 2: Original BeautifulSoup API Source References
The following references are taken from the original, unmodified BeautifulSoup 4.13.0 source archive. The paths are relative to the source archive's root directory. These references do not refer to the modified Milestone 2 implementation.
API or class	Original source file	Line(s)	Purpose in the applications
BeautifulSoup class	bs4/__init__.py	133	Defines the main document-parsing class
BeautifulSoup.__init__	bs4/__init__.py	209–219	Defines the constructor and its parameters
BeautifulSoup.parse_only assignment	bs4/__init__.py	437	Stores the optional parsing filter
SoupStrainer class	bs4/filter.py	313	Defines the parsing and matching filter
SoupStrainer.__init__	bs4/filter.py	345–351	Accepts tag-name and attribute filtering rules
Tag.find_parent	bs4/element.py	992–997	Finds the closest matching parent element
Tag.prettify	bs4/element.py	2601–2617	Formats a document as a readable string
Tag.find	bs4/element.py	2684–2711	Finds the first matching element
Tag.find_all	bs4/element.py	2715–2740	Finds all matching elements
Tag.get	bs4/element.py	2160–2171	Retrieves an attribute value with an optional default
Tag.__getitem__	bs4/element.py	2203–2206	Retrieves an attribute using tag["href"]
Tag.__setitem__	bs4/element.py	2223–2226	Sets an attribute using tag["class"] = ["test"]
API usage in Milestone 1
•	Task 1: BeautifulSoup and Tag.prettify() parse and format the document.
•	Task 2: BeautifulSoup and Tag.find_all() retrieve hyperlink elements.
•	Task 3: Tag.find_all() retrieves all tags.
•	Task 4: Tag.find_all() filters tags by the presence of an ID attribute.
•	Task 5: Tag.find() locates the first hyperlink, and Tag.find_parent() locates its closest matching div ancestor.
•	Task 6: Tag.find_all() locates <b> elements; assigning to tag.name changes their names.
•	Task 7: Tag.find_all() locates paragraphs, and Tag.__setitem__() sets their class attributes.
•	Task 8: Tag.find_all() locates links with an href attribute, and Tag.__getitem__() retrieves that attribute.
Milestone 2 Part 1 additionally uses SoupStrainer and the parse_only constructor argument to filter elements during parsing.
Part 3: SoupReplacer
Implementation
The SoupReplacer(og_tag, alt_tag) class is a Milestone 2 addition implemented in bs4/__init__.py. It is intended to rename matching tags during parsing through the optional replacer argument to BeautifulSoup.
Example:
from bs4 import BeautifulSoup, SoupReplacer

html = "<p>Hello <b>world</b></p>"

soup = BeautifulSoup(
    html,
    "html.parser",
    replacer=SoupReplacer("b", "blockquote"),
)

print(soup)
Expected output:
<p>Hello <blockquote>world</blockquote></p>
Tests
File: bs4/tests/test_soup_replacer.py
Two tests verify that:
1.	A matching tag is renamed to the specified alternative tag.
2.	Tags that do not match the original tag name remain unchanged.
Task 6 demonstration application
File: apps/m2/task6_soupreplacer.py
The application demonstrates replacing <b> tags with <blockquote> during parsing and saving the resulting document.
Run it with:
python apps/m2/task6_soupreplacer.py "path\to\input.html"
An optional output path can be provided:
python apps/m2/task6_soupreplacer.py "path\to\input.html" "path\to\output.html"
Testing and Validation
The original test-suite baseline on the development machine was:
•	619 passed
•	1 failed
•	216 skipped
After implementing SoupReplacer and adding two tests, the full test suite reported:
•	621 passed
•	1 failed
•	216 skipped
The existing failure was bs4/tests/test_htmlparser.py::TestHTMLParserTreeBuilder::test_rejected_input. It was present in the original baseline run and remained present after the new tests were added.
The two new SoupReplacer tests passed, and the Task 6 demonstration application successfully replaced <b> with <blockquote> in the sample HTML document.

