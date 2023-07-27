from html_parser.context_maker.semantics.base_semantic import Semantic
import json


class Select(Semantic):
    def __init__(self, soup, tag=None, context=None):
        super().__init__(soup, tag=tag, context=context)
        option_tags = tag.find_all("option")
        self._values = list(map(lambda tag: tag["value"], option_tags))
        self._value_mappings = list(map(lambda tag: {tag["value"]: tag}, option_tags))
        self._clickable = True
        self._typeable = False

    @property
    def values(self):
        return self._values

    @property
    def clickable(self):
        return self._clickable

    @property
    def typeable(self):
        return self._typeable

    def __str__(self):
        return json.dumps(
            {
                "context": "select dropdown",
                "label": self.label_text,
                "values": self.values,
            }
        )

    def build(self):
        return {
            "context": "select dropdown",
            "label": self.label_text,
            "values": self.values,
        }
