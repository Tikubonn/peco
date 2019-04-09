
from .writer import Writer

class ForNode (Writer):
  
  def __init__ (self, sourcenode, varnode, thennode, scope):
    self.sourcenode = sourcenode
    self.varnode = varnode
    self.thennode = thennode
    self.scope = scope
  
  # override
  def write (self, stream):
    with self.scope:
      for value in self.sourcenode.get_value(defaultvalue=[]):
        self.varnode.set_value(value)
        self.thennode.write(stream)
  