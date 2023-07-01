from bs4 import BeautifulSoup
from bs4.element import Tag
import json
import collections

class Context():
  """
  A relational representation of html context.
  - html: the associated html string
  - children[<tag>]: a list of tags that are nested within <tag>
  - siblings[<tag>]: a list of tags that are on the same level as <tag>
  - parents[<tag>]: an ordered list of tages that contain <tag> as a descendant
  """
  def __init__(self, html, children=[], siblings=[], parents=[]):
    self._html = html
    self._children = children
    self._siblings = siblings
    self._parents = parents
  
  @property
  def parents(self):
    return self._parents
  
  @property
  def siblings(self):
    return self._siblings
  
  @property
  def children(self):
    return self._children
  
  @property
  def html(self):
    return self._html

  def __str__(self):
    return json.dumps({
      "children": self.children,
      "siblings": self.siblings,
      "parents": self.parents
    })


class ContextBuilder():
  """
  Builds a [Context] based on html string [html]

  Example usage:
    some_html_string = <h1>hello world<h1>
    some_context = ContextBuilder(some_html_string).build()
  """
  def __init__(self, html):
    self.html = html
    self.siblings = collections.defaultdict(list)
    self.children =  collections.defaultdict(list)
    self.parents = collections.defaultdict(list)
  

  def build(self):
    soup = BeautifulSoup(self.html, "html.parser")
    
    for tag in soup.findAll():
      if isinstance(tag, Tag):
        self.children[tag] = list(tag.descendants)
        self.siblings[tag] = list(tag.next_siblings)
      else:
        self.children[tag] = []
        self.siblings[tag] = []

      self.parents[tag] = tag.parents 
    

    return Context(self.html, children=self.children, siblings=self.siblings, parents=self.parents)

    
    
      





