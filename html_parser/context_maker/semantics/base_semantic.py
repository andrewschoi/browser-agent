import json
from bs4.element import Tag
import collections


class Semantic:
    def __init__(self, tag=None, context=None):
        self._tag = tag
        self._context = context
        self._children = []
        self._siblings = []
        self._parents = []

    @property
    def tag(self):
        return self._tag

    @property
    def context(self):
        return self._context

    @property
    def children(self):
        return self._children

    @property
    def siblings(self):
        return self._siblings

    @property
    def parents(self):
        return self._parents

    def with_children(self):
        self._children = self._context["children"]

    def with_siblings(self):
        self._siblings = self._context["siblings"]

    def with_parents(self, k=3):
        self._parents = self._context["parents"][:k]

    def with_text_only(self):
        self._children = list(
            map(
                lambda tag: tag.get_text() if isinstance(tag, Tag) else tag,
                self._children,
            )
        )

        self._siblings = list(
            map(
                lambda tag: tag.get_text() if isinstance(tag, Tag) else tag,
                self._sibling,
            )
        )

        self._parents = list(
            map(
                lambda tag: tag.get_text() if isinstance(tag, Tag) else tag,
                self._parents,
            )
        )

    def without_classes(self):
        self._without_attr("class")
        self._without_attr("className")

    def without_style(self):
        self._without_attr("style")

    def _without_attr(self, attr):
        new_children = collections.defaultdict(list)
        for old_tag, old_children in self._children:
            old_tag.pop(attr, None)
            for child in old_children:
                child.pop(attr, None)
                new_children[old_tag].append(child)
        self._children = new_children

        new_siblings = collections.defaultdict(list)
        for old_tag, old_siblings in self._siblings:
            old_tag.pop(attr, None)
            for child in old_siblings:
                child.pop(attr, None)
                new_siblings[old_tag].append(child)
        self._siblings = new_siblings

        new_parents = collections.defaultdict(list)
        for old_tag, old_parents in self._parents:
            old_tag.pop(attr, None)
            for child in old_parents:
                child.pop(attr, None)
            new_parents[old_tag].append(child)
        self._parents = new_parents

    def build(self):
        return {
            "children": self._children,
            "siblings": self._siblings,
            "parents": self._parents,
        }

    def __str__(self):
        return json.dumps(
            {
                "children": self._children,
                "siblings": self._siblings,
                "parents": self._parents,
            }
        )
