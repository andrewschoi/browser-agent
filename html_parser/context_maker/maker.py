from bs4 import BeautifulSoup, NavigableString

import collections

class Context():
  """
  A relational representation of html context.
  - html: the associated html string
  - descendents[<tag>]: a list of tags that are nested within <tag>
  - siblings[<tag>]: a list of tags that are on the same level as <tag>
  - parents[<tag>]: an ordered list of tages that contain <tag> as a descendent
  """
  def __init__(self, html, descendents=[], siblings=[], parents=[]):
    self.html = html
    self.descendents = descendents
    self.siblings = siblings
    self.parents = parents


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
    self.descendents =  collections.defaultdict(list)
    self.parents = collections.defaultdict(list)
  

  def build(self):
    soup = BeautifulSoup(self.html, "html.parser")
    rank = {}
    root = soup.find('html')
    q = [root]
    current_level = 0
    while len(q) > 0:
      for _ in range(len(q)):
        node = q.pop(0)
        for child in node.children:
          if type(child) == NavigableString:
            continue
          q.append(child)
        rank[child] = current_level
      current_level += 1
    
    for tag in soup.findAll():
      self.descendents[tag] = tag.descendents
      self.siblings[tag] = tag.siblings
    
    for tag in soup.findAll():
      par = []
      for  node, desc in self.descendents.items():
        if desc is not None and tag in desc:
          par.append(node)
      self.parents[tag] = sorted(par, key=lambda tag: rank[tag], reverse=True)


    return Context(self.html, descendents=self.descendents, siblings=self.siblings, parents=self.parents)

    
    
      





