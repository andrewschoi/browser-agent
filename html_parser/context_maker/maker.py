from bs4 import BeautifulSoup
import collections

class Context():
  def __init__(self, descendents=[], siblings=[], parents=[]):
    self.descendents = descendents
    self.siblings = siblings
    self.parents = parents


class ContextBuilder():
  def __init__(self, html):
    self.html = html
    self.siblings = collections.defaultdict(list)
    self.descendents =  collections.defaultdict(list)
    self.parents = collections.defaultdict(list)
  

  def build(self):
    soup = BeautifulSoup(html, "html.parser")
    rank = {}
    root = soup.find('html')
    q = [root]
    current_level = 0
    while len(q) > 0:
      for _ in range(len(q)):
        node = q.pop(0)
        for child in node.children:
          q.append(child)
        rank[child] = current_level
      current_level += 1
    
    for tag in soup.findAll():
      descendents[tag] = tag.descendents
      siblings[tag] = tag.siblings
    
    for tag in soup.findAll():
      par = []
      for [node, descendents] in descendents:
        if tag in descendents:
          par.append(par)
      parents[tag] = sorted(par, lambda tag: rank[tag], reverse=True)


    return Context(descendents=self.descendents, siblings=self.siblings, parents=self.parents)

    
    
      





