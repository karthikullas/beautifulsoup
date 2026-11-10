Milestone 3 – Extended SoupReplacer API
1. Overview
Milestone 3 extends the SoupReplacer API developed in Milestone 2. The original implementation supported replacing one tag name with another during HTML parsing. The extended implementation introduces callback-based transformations that can modify tag names, attributes, or the entire Tag object.
All transformations are applied during parsing, rather than requiring a separate post-processing step.
2. M2 API
The Milestone 2 API uses:
SoupReplacer(og_tag, alt_tag)
It replaces a specified original tag name (og_tag) with an alternative tag name (alt_tag).
For example:
replacer = SoupReplacer("b", "strong")
soup = BeautifulSoup(html, "html.parser", replacer=replacer)
This approach is simple and suitable when the only requirement is replacing one tag name with another.
3. M3 API
Milestone 3 extends the constructor with three optional callback parameters:
SoupReplacer(
    og_tag=None,
    alt_tag=None,
    name_xformer=None,
    attrs_xformer=None,
    xformer=None
)
name_xformer
Accepts a function that receives a Tag object and returns a replacement tag name.
Example:
def change_name(tag):
    if tag.name == "b":
        return "strong"
    return tag.name
attrs_xformer
Accepts a function that receives a Tag object and returns a replacement attributes dictionary.
Example:
def change_attributes(tag):
    if tag.name == "p":
        attributes = dict(tag.attrs)
        attributes["class"] = ["test"]
        return attributes
    return tag.attrs
xformer
Accepts a function that receives a Tag object and modifies it directly. This callback works through side effects and does not need to return a value.
Example:
def modify_tag(tag):
    if "class" in tag.attrs:
        del tag.attrs["class"]
The three callbacks can also be combined in a single SoupReplacer instance.
4. Application – Task 7
The application is implemented in:
apps/m3/task7_attrs_xformer.py
The objective is to read an HTML file, assign the class test to every paragraph (p) tag, and write the prettified HTML to an output file.
The application uses attrs_xformer to modify paragraph attributes while BeautifulSoup parses the input.
Run the application using:
python apps/m3/task7_attrs_xformer.py input.html output.html
The implementation preserves other existing paragraph attributes while setting the class to test.
5. M2 vs. M3 Comparison
Aspect	M2 API	M3 API
Tag name replacement	Supported	Supported
Attribute transformation	Not directly supported	Supported
Entire Tag modification	Not directly supported	Supported
Flexibility	Limited	More flexible
Implementation	Simple fixed replacement	Callback-based transformations
Backward compatibility	Original interface	Retains the M2 interface
6. Recommendation
The M2 API is appropriate for simple tag-name replacement because it is straightforward and easy to use.
The M3 API is recommended for more complex HTML transformations because it supports tag-name changes, attribute transformations, and direct modifications to Tag objects. Its callback-based design makes it more flexible and extensible.
The original M2 constructor arguments are retained, allowing existing M2 applications to continue using the API.
Therefore, the M3 API is the preferred approach for general-purpose HTML transformations, while the M2 interface remains useful for simple replacement operations.
7. Testing
The test file is:
bs4/tests/test_soup_replacer.py
It contains two existing M2 tests and six new M3 tests covering:
1.	Changing tag names using name_xformer.
2.	Leaving unrelated tag names unchanged.
3.	Changing attributes using attrs_xformer.
4.	Preserving other existing attributes.
5.	Modifying a Tag through xformer side effects.
6.	Combining multiple transformers.
Results from the focused test file:
•	8 passed.
Results from the complete test suite:
•	627 passed.
•	1 failed.
•	216 skipped.
The single failure was in test_rejected_input under bs4/tests/test_htmlparser.py, an existing Python 3.15-related failure also observed before the M3 changes.
8. Files Added or Modified
•	bs4/__init__.py – Extended the SoupReplacer implementation and integrated callback transformations into parsing.
•	bs4/tests/test_soup_replacer.py – Added six M3 test cases while retaining the two M2 tests.
•	apps/m3/task7_attrs_xformer.py – Implemented Task 7 using the new attrs_xformer API.
•	apps/m3/M3-README.md – Technical brief comparing the M2 and M3 APIs.

