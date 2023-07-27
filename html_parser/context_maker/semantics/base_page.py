from bs4 import BeautifulSoup
from html_parser.context_maker.semantics.button import Button
from html_parser.context_maker.semantics.select import Select
from html_parser.context_maker.semantics.input import Input
from html_parser.context_maker.semantics.href import Href
from html_parser.context_maker.maker import ContextBuilder


def semantic_from_tag(soup, tag, context):
    if tag.name == "button":
        return Button(soup, tag, context)
    elif tag.name == "input":
        return Input(soup, tag, context)
    elif tag.name == "select":
        return Select(soup, tag, context)
    elif tag.name == "a":
        return Href(soup, tag, context)
    else:
        raise Exception("tag is not a button, input, select, or a")


class Page:
    """
    Consolidates the essential information found in a HTML webpage: webpage
    text-content, interactable elements, header text-content, etc.
    """

    def __init__(self, html):
        self._soup = BeautifulSoup(html, "html.parser")
        self._context = ContextBuilder(html).build()
        self._html = html
        self._title = self._soup.find("title")
        self._text = self._soup.get_text(separator="\n", strip=True)

        interactable_tags = self._soup.find_all(["a", "input", "select", "button"])

        self._elements_dict = {"button": [], "a": [], "input": [], "select": []}

        for tag in interactable_tags:
            semantic_element = semantic_from_tag(self._soup, tag, self._context)
            self._elements_dict[tag.name].append(semantic_element)

        self._buttons = self._elements_dict["button"]
        self._hrefs = self._elements_dict["a"]
        self._inputs = self._elements_dict["input"]
        self._selects = self._elements_dict["select"]
        self._interactables = sorted(
            self.buttons + self.hrefs + self.inputs + self.selects
        )

    @property
    def soup(self):
        return self._soup

    @property
    def context(self):
        return self._context

    @property
    def html(self):
        return self._html

    @property
    def text(self):
        return self._text

    @property
    def interactables(self):
        return self._interactables

    @property
    def buttons(self):
        return self._buttons

    @property
    def hrefs(self):
        return self._hrefs

    @property
    def inputs(self):
        return self._inputs

    @property
    def selects(self):
        return self._selects

    def header_text(self):
        headers = self._soup.find_all(["header", "h1", "h2", "h3", "h4", "h5", "h6"])
        return " ".join(
            list(map(lambda tag: tag.get_text(separator=" ", strip=True), headers))
        )
