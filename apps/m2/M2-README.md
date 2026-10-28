Milestone 2
Part 1: SoupStrainer Applications
Three applications demonstrate filtering HTML/XML parsing with BeautifulSoup's SoupStrainer.
Task 2 — Print all hyperlinks
File: apps/m2/task2_strainer.py
Uses SoupStrainer("a") with the parse_only argument to parse and print anchor tags.
Task 3 — Print all tags
File: apps/m2/task3_strainer.py
Uses SoupStrainer(True) to match tags throughout the document.
Observation: This works for selecting tags, although text nodes outside matching tags are not independently selected by the filter.
Task 4 — Print tags with an ID attribute
File: apps/m2/task4_strainer.py
Uses SoupStrainer(attrs={"id": True}) to select tags that have an id attribute.
Running the applications
Run commands from the repository root:
python apps/m2/task2_strainer.py "path\to\input.html"
python apps/m2/task3_strainer.py "path\to\input.html"
python apps/m2/task4_strainer.py "path\to\input.html"
The scripts use html.parser for HTML files and the XML parser for files ending in .xml.
Part 2: Original Source References
The following references are intended to refer to the original, unmodified BeautifulSoup 4.13.0 source archive. Verify the exact line numbers against that archive before submission, since line numbers may vary between source versions.
API or class	Original source file	Line reference
BeautifulSoup	bs4/__init__.py	Class definition, approximately line 133
BeautifulSoup.__init__	bs4/__init__.py	Constructor, approximately line 209
SoupStrainer	bs4/filter.py	Class definition, approximately line 313
SoupStrainer.__init__	bs4/filter.py	Constructor, approximately line 345
Tag.find_parent	bs4/element.py	Approximately line 992
Tag.prettify	bs4/element.py	Approximately line 2601
Tag.find	bs4/element.py	Approximately line 2684
Tag.find_all	bs4/element.py	Approximately line 2715
Tag.get	bs4/element.py	Approximately line 2160
Tag.__getitem__	bs4/element.py	Approximately line 2203
Tag.__setitem__	bs4/element.py	Approximately line 2223
API usage summary
Milestone 1 uses BeautifulSoup parsing, tag searching, ancestor searching, pretty-printing, and attribute access and modification. Milestone 2 Part 1 uses SoupStrainer with parse_only to restrict parsing to matching tags.
SoupReplacer and the replacer constructor argument are new Milestone 2 additions and do not exist in the original source archive.
Important: Confirm the exact line numbers and include every API used by your Milestone 1 and Milestone 2 applications, as required by the assignment.
Part 3: SoupReplacer
Implementation
SoupReplacer(og_tag, alt_tag) is implemented in bs4/__init__.py. It replaces matching tag names during parsing when supplied to the BeautifulSoup constructor using the optional replacer argument.
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
The tests check that matching tags are replaced and that other tag names remain unchanged.
Task 6 demonstration application
File: apps/m2/task6_soupreplacer.py
Run:
python apps/m2/task6_soupreplacer.py "path\to\input.html"
An optional output path can also be supplied:
python apps/m2/task6_soupreplacer.py "path\to\input.html" "path\to\output.html"
The application replaces <b> tags with <blockquote> during parsing and saves the resulting document.
Validation
The original test-suite baseline on the development machine was:
•	619 passed
•	1 failed
•	216 skipped
After adding the two SoupReplacer tests, the expected result is 621 passed, 1 failed, and 216 skipped, provided no other test results changed. The existing failure was in bs4/tests/test_htmlparser.py::TestHTMLParserTreeBuilder::test_rejected_input.
Record the actual final test results before submission.

