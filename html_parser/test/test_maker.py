from html_parser.context_maker import maker
import unittest


with open('html_parser/test/html_samples/form.html', 'r') as f:
  form = f.read()

with open('html_parser/test/html_samples/story.html', 'r') as f:
  story = f.read()


class TestMaker(unittest.TestCase):
  def test_simple(self):
    pass

unittest.main()