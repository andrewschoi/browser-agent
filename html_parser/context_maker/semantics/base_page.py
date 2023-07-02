from bs4 import BeautifulSoup


class Page:
    def __init__(self, html):
        soup = BeautifulSoup(html, "html.parser")
        self._html = html
        self._text = soup.get_text(separator="\n", strip=True)
        self._interactable_elements = soup.find_all(["a", "input", "select", "button"])
        self._buttons = soup.find_all(["button"])
        self._hrefs = soup.find_all(["a"])
        self._inputs = soup.find_all(["input"])
        self._selects = soup.find_all(["select"])

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
