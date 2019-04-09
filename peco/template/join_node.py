
from .writer import Writer
from .sentence_node import SentenceNode

class JoinNode (Writer):
  
  def __init__ (self, separator, node):
    self.separator = separator
    self.node = node
  
  # override
  def write (self, stream):
    for index, value in enumerate(self.node.get_value(defaultvalue=[])):
      if 0 < index:
        self.separator.write(stream)
      stream.write(str(value))
  