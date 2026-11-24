Milestone 4 – Iterable BeautifulSoup

1. Overview

Milestone 4 extends the BeautifulSoup API by making the BeautifulSoup object iterable. This allows users to traverse all nodes in the parsed document directly using a for loop.

2. Implementation

Added an __iter__() method to the BeautifulSoup class in bs4/__init__.py.
def __iter__(self) -> Iterator[PageElement]:
    """Iterate over all nodes in the document tree."""
    return self.descendants
The implementation reuses the existing descendants generator to traverse the document tree one node at a time. It does not create a list of nodes.

3. Usage

soup = BeautifulSoup(html_doc, "html.parser")

for node in soup:
    print(node)
Iteration includes nested tags and text nodes in document order.

4. Unit Tests

Added five tests in bs4/tests/test_soup_iteration.py covering:
1.	Top-level tags.
2.	Nested tags.
3.	Text nodes.
4.	Document traversal order.
5.	Exclusion of the BeautifulSoup object itself.
All five M4 tests passed.

5. Testing Results

Full test suite:
•	632 passed
•	1 failed
•	216 skipped
The existing Python 3.15-related failure is TestHTMLParserTreeBuilder.test_rejected_input, which was also present before M4.

6. Files Changed

•	bs4/__init__.py – Added BeautifulSoup iteration support.
•	bs4/tests/test_soup_iteration.py – Added five unit tests.
•	apps/m4/M4-README.md – Added this technical brief.

