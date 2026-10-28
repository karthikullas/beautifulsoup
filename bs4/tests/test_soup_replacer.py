
from bs4 import BeautifulSoup, SoupReplacer


def test_soup_replacer_changes_tag_during_parsing():
    html = "<p>Hello <b>world</b></p>"

    soup = BeautifulSoup(
        html,
        "html.parser",
        replacer=SoupReplacer("b", "blockquote"),
    )

    assert soup.find("b") is None
    assert soup.find("blockquote").get_text() == "world"
    assert str(soup) == "<p>Hello <blockquote>world</blockquote></p>"


def test_soup_replacer_leaves_other_tags_unchanged():
    html = "<div><b>bold</b><i>italic</i></div>"

    soup = BeautifulSoup(
        html,
        "html.parser",
        replacer=SoupReplacer("b", "blockquote"),
    )

    assert soup.find("blockquote") is not None
    assert soup.find("i") is not None
    assert soup.find("b") is None
