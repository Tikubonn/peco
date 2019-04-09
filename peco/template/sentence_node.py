
from .writer import Writer
from .whitespace_node import WhitespaceNode

class SentenceNode (Writer):
  
  def __init__ (self):
    self.nodes = list()
  
  def add (self, node):
    self.nodes.append(node)
  
  def trim (self): # create new instance.
    indexstart = None
    for index, node in enumerate(self.nodes):
      indexstart = index
      if not isinstance(node, WhitespaceNode):
        break
    indexend = None
    for index, node in enumerate(reversed(self.nodes)):
      if not isinstance(node, WhitespaceNode):
        break
      indexend = -(index +1)
    sentence = type(self)()
    for node in self.nodes[indexstart: indexend]:
      sentence.add(node)
    return sentence
    
  # override
  def write (self, stream):
    for node in self.nodes:
      node.write(stream)
  