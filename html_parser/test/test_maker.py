from html_parser.context_maker.maker import ContextBuilder
import unittest


with open('html_parser/test/html_samples/form.html', 'r') as f:
  form = f.read()

with open('html_parser/test/html_samples/story.html', 'r') as f:
  story = f.read()


class TestMaker(unittest.TestCase):
  def test_build_successful(self):
    story_context = ContextBuilder(story).build()
    form_context = ContextBuilder(form).build()    

unittest.main()