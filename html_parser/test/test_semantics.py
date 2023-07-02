from html_parser.context_maker.maker import ContextBuilder
from html_parser.context_maker.semantics.base_semantic import Semantic
from bs4 import BeautifulSoup
import unittest
import collections


with open("html_parser/test/html_samples/form.html", "r") as f:
    form = f.read()

with open("html_parser/test/html_samples/story.html", "r") as f:
    story = f.read()


class TestSemantic(unittest.TestCase):
    def test_build_successful(self):
        story_context = ContextBuilder(story).build()
        soup = BeautifulSoup(story, "html.parser")
        for tag in soup.find_all():
            Semantic(tag, story_context).build()
            Semantic(tag, story_context).with_children().build()
            Semantic(tag, story_context).with_siblings().build()
            Semantic(tag, story_context).with_parents().build()
            Semantic(
                tag, story_context
            ).with_children().with_siblings().with_parents().build()
            Semantic(
                tag, story_context
            ).with_children().with_siblings().with_parents().without_classes().build()


unittest.main()
