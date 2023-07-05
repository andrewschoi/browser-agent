import json
from bs4.element import Tag, NavigableString
from lxml import html


class Semantic:
    """
    Builder class for the most 'vague' form of a bs4.element.Tag or
    bs4.element.NavigableString semantic. Gives ability to access a particular
    tag's children, sibling, or k parents, with additional options, such as
    text-only, tags without class attributes, or tags without styles

    Example usage:
    - some_html = <html-string>
    - some_context = Context(some_html)
    - some_html_root = BeautifulSoup(some_html, 'html.parser')
    - some_tag_semantic =
        Semantic(tag=some_html_root, context=some_context)
        .with_children()
        .with_siblings()
        .with_parents()
        .with_text_only()
        .build()
    """

    def __init__(self, tag=None, context=None):
        self._tag = tag
        self._id = tag.get("id", None)
        self._name = tag.get("name", None)
        self._tag_name = tag.name
        self._classes = tag.get("class")
        self._xpath = self._xpath_from_tag(tag)

        self._context = context
        self._children = []
        self._siblings = []
        self._parents = []

    def _xpath_from_tag(self, tag):
        lxml_element = html.fromstring(str(tag))
        tree = lxml_element.getroottree()
        xpath = tree.getpath(lxml_element)
        return xpath

    @property
    def tag(self):
        return self._tag

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def tag_name(self):
        return self._tag_name

    @property
    def classes(self):
        return self._classes

    @property
    def xpath(self):
        return self._xpath

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

    def semantic_comparator(self, type):
        if self._name == "input":
            if self._type is None:
                return -1
            if self._type == "email":
                return -1
            if self._type == "password":
                return -1
            if self._type == "text":
                return -1
            if self._type == "submit":
                return 1

        if self._name == "select":
            return -1

        if self._name == "a":
            return 0

        if self._name == "button":
            return 1

    def __lt__(self, other):
        return self.semantic_comparator(self._name) < other.semantic_comparator(
            other.name
        )

    def __eq__(self, other):
        return self.semantic_comparator(self._name) == other.semantic_comparator(
            other.name
        )

    def __gt__(self, other):
        return self.semantic_comparator(self._name) > other.semantic_comparator(
            other.name
        )

    def __ne__(self, other):
        return self.semantic_comparator(self._name) != other.semantic_comparator(
            other.name
        )
