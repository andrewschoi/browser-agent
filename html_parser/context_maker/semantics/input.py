from html_parser.context_maker.semantics.base_semantic import Semantic
import json


class Input(Semantic):
    def __init__(self, soup, tag=None, context=None):
        assert tag.name == "input"
        super().__init__(soup, tag=tag, context=context)
        self._type = tag.get("type")
        self._value = tag.get("value", None)
        self._clickable = True if tag.get("type", None) == "submit" else False
        self._typeable = True if tag.get("type") != "submit" else False

    @property
    def type(self):
        return self._type

    @property
    def value(self):
        return self._value

    @property
    def clickable(self):
        return self._clickable

    @property
    def typeable(self):
        return self._typeable

    def __str__(self):
        return json.dumps(
            {
                "context": "input",
                "type": self.type,
                "label": self.label_text,
                "value": self.value,
            }
        )

    def build(self):
        return {
            "context": "input",
            "type": self.type,
            "label": self.label_text,
            "value": self.value,
        }
