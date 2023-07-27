from html_parser.context_maker.semantics.base_semantic import Semantic
from bs4.element import Tag
import json


class Href(Semantic):
    def __init__(self, soup, tag=None, context=None):
        assert isinstance(tag, Tag)
        super().__init__(soup, tag=tag, context=context)
        self._inner_text = tag.get_text()
        self._clickable = True
        self._typeable = False

    @property
    def inner_text(self):
        return self._inner_text

    @property
    def clickable(self):
        return self._clickable

    @property
    def typeable(self):
        return self._typeable

    def __str__(self):
        return json.dumps(
            {"context": "link", "text": self.inner_text, "label": self.label_text}
        )

    def build(self):
        return {"context": "link", "text": self.inner_text, "label": self.label_text}
