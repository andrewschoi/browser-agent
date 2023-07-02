import json
from bs4.element import Tag, NavigableString


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
        self._children = self._context.children[self._tag]
        return self

    def with_siblings(self):
        self._siblings = self._context.siblings[self._tag]
        return self

    def with_parents(self, k=3):
        self._parents = self._context.parents[self._tag][:k]
        return self

    def with_text_only(self):
        self._children = list(
            map(
                lambda tag: tag.get_text(strip=True) if isinstance(tag, Tag) else tag,
                self._children,
            )
        )

        self._siblings = list(
            map(
                lambda tag: tag.get_text(strip=True) if isinstance(tag, Tag) else tag,
                self._siblings,
            )
        )

        self._parents = list(
            map(
                lambda tag: tag.get_text(strip=True) if isinstance(tag, Tag) else tag,
                self._parents,
            )
        )

        return self

    def without_classes(self):
        self._without_attr("class")
        self._without_attr("className")
        return self

    def without_style(self):
        self._without_attr("style")
        return self

    def _without_attr(self, attr):
        new_children = []
        for old_child in self._children:
            if isinstance(old_child, NavigableString):
                continue
            if old_child.attr is not None and attr in old_child.attr:
                del old_child[attr]
            new_children.append(old_child)
        self._children = new_children

        new_siblings = []
        for old_sibling in self._siblings:
            if isinstance(old_sibling, NavigableString):
                continue
            if old_sibling.attr is not None and attr in old_sibling.attr:
                del old_sibling[attr]
            new_siblings.append(old_sibling)
        self._siblings = new_siblings

        new_parents = []
        for old_parent in self._parents:
            if isinstance(old_parent, NavigableString):
                continue
            if old_parent.attr is not None and attr in old_parent.attr:
                del old_parent[attr]
            new_parents.append(old_parent)
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
