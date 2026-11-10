
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

def test_name_xformer_changes_tag_name():
    html = "<p>Hello <b>world</b></p>"
    replacer = SoupReplacer(
        name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name
    )

    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert soup.find("blockquote") is not None
    assert soup.find("b") is None
    assert soup.find("blockquote").get_text() == "world"


def test_name_xformer_leaves_other_tags_unchanged():
    html = "<div><b>bold</b><i>italic</i></div>"
    replacer = SoupReplacer(
        name_xformer=lambda tag: "strong" if tag.name == "b" else tag.name
    )

    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert soup.find("strong") is not None
    assert soup.find("i") is not None
    assert soup.find("div") is not None


def test_attrs_xformer_changes_attributes():
    html = '<p class="old">Hello</p>'
    replacer = SoupReplacer(
        attrs_xformer=lambda tag: {"class": ["new"]} if tag.name == "p" else tag.attrs
    )

    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert soup.p["class"] == ["new"]


def test_attrs_xformer_preserves_other_attributes():
    html = '<p id="intro" class="old">Hello</p>'
    replacer = SoupReplacer(
        attrs_xformer=lambda tag: {
            **tag.attrs,
            "class": ["test"],
        } if tag.name == "p" else tag.attrs
    )

    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert soup.p["id"] == "intro"
    assert soup.p["class"] == ["test"]


def test_xformer_modifies_tag_with_side_effect():
    html = '<p class="intro">Hello</p>'

    def remove_class_attr(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]

    replacer = SoupReplacer(xformer=remove_class_attr)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert "class" not in soup.p.attrs


def test_multiple_transformers_work_together():
    html = '<b class="old">Hello</b>'

    replacer = SoupReplacer(
        name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name,
        attrs_xformer=lambda tag: {
            **tag.attrs,
            "class": ["new"],
        },
    )

    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert soup.blockquote is not None
    assert soup.blockquote["class"] == ["new"]
    assert soup.blockquote.get_text() == "Hello"