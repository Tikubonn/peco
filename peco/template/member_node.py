
from .writer import Writer
from .evaluatable import Evaluatable

class MemberNode (Writer, Evaluatable):
  
  def __init__ (self, name, node):
    self.name = name
    self.node = node
  
  # override
  def get_value (self, defaultvalue=None):
    value = self.node.get_value(defaultvalue={})
    return value.get(self.name, defaultvalue)
  
  # override
  def write (self, stream):
    stream.write(str(self.get_value(defaultvalue="")))
  