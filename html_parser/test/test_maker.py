from html_parser.context_maker.maker import ContextBuilder
from bs4 import BeautifulSoup
import unittest
import collections


with open('html_parser/test/html_samples/form.html', 'r') as f:
  form = f.read()

with open('html_parser/test/html_samples/story.html', 'r') as f:
  story = f.read()


class TestMaker(unittest.TestCase):
  def test_build_successful(self):
    story_context = ContextBuilder(story).build()
    form_context = ContextBuilder(form).build()    


  def test_story_relations(self):
    soup = BeautifulSoup(story, 'html.parser')
    story_context = ContextBuilder(story).build()

    story_children = story_context.children
    correct_children = collections.defaultdict(list)

    for tag in soup.findAll():
      correct_children[tag] = list(tag.descendants)
    
    self.assertEqual(len(story_children.keys()), len(correct_children.keys()))
    for k in correct_children.keys():
      self.assertEqual(set(story_children[k]), set(correct_children[k]))
    
    story_siblings = story_context.siblings
    correct_siblings = collections.defaultdict(list)
    for tag in soup.findAll():
      correct_siblings[tag] = list(tag.next_siblings)
    
    self.assertEqual(len(story_siblings.keys()), len(correct_siblings.keys()))
    for k in correct_siblings.keys():
      self.assertEqual(set(story_siblings[k]), set(correct_siblings[k]))

    
    story_parents = story_context.parents
    correct_parents = collections.defaultdict(list)
    for tag in soup.findAll():
      correct_parents[tag] = list(tag.parents)

    self.assertEqual(len(story_parents), len(correct_parents))
    for k in correct_parents.keys():
      self.assertEqual(set(story_parents[k]), set(correct_parents[k]))
      

unittest.main()