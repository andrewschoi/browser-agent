from bs4 import BeautifulSoup


class Page:
    """
    Consolidates the essential information found in a HTML webpage: webpage
    text-content, interactable elements, header text-content, etc.
    """

    def __init__(self, html):
        self._soup = BeautifulSoup(html, "html.parser")
        self._html = html
        self._title = self._soup.find("title")
        self._text = self._soup.get_text(separator="\n", strip=True)
        self._interactable_elements = self._soup.find_all(
            ["a", "input", "select", "button"]
        )
        self._buttons = self._soup.find_all(["button"])
        self._hrefs = self._soup.find_all(["a"])
        self._inputs = self._soup.find_all(["input"])
        self._selects = self._soup.find_all(["select"])

    @property
    def html(self):
        return self._html

    @property
    def text(self):
        return self._text

    @property
    def interactable_elements(self):
        return self._interactable_elements

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
        return "\n".join(
            list(map(lambda tag: tag.get_text(separator="\n", strip=True), headers))
        )
