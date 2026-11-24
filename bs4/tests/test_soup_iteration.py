from bs4 import BeautifulSoup

def test_soup_iteration_includes_top_level_tag():
    soup = BeautifulSoup("<html><body><p>Hello</p></body></html>", "html.parser")
    nodes = list(soup)
    assert isinstance(nodes[0], type(soup.html))
    assert nodes[0].name == "html"

def test_soup_iteration_includes_nested_tags():
    soup = BeautifulSoup("<div><p><b>Hello</b></p></div>", "html.parser")
    names = [node.name for node in soup if getattr(node, "name", None) is not None]
    assert names == ["div", "p", "b"]

def test_soup_iteration_includes_text_nodes():
    soup = BeautifulSoup("<p>Hello <b>World</b></p>", "html.parser")
    text_nodes = [node for node in soup if isinstance(node, str)]
    assert len(text_nodes) == 2
    assert str(text_nodes[0]) == "Hello "
    assert str(text_nodes[1]) == "World"

def test_soup_iteration_visits_nodes_in_document_order():
    soup = BeautifulSoup("<div><p>First</p><p>Second</p></div>", "html.parser")
    nodes = [str(node) for node in soup]
    assert nodes == [
        "<div><p>First</p><p>Second</p></div>",
        "<p>First</p>",
        "First",
        "<p>Second</p>",
        "Second",
    ]

def test_soup_iteration_does_not_include_soup_itself():
    soup = BeautifulSoup("<p>Hello</p>", "html.parser")
    nodes = list(soup)
    assert all(node is not soup for node in nodes)
    assert len(nodes) == 2
