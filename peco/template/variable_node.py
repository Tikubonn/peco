
from .writer import Writer
from .evaluatable import Evaluatable

class VariableNode (Writer, Evaluatable):
  
  def __init__ (self, name, scope):
    self.name = name
    self.scope = scope
  
  # override
  def set_value (self, value):
    self.scope.set_value(self.name, value)
  
  # override
  def get_value (self, defaultvalue=None):
    return self.scope.get_value(self.name, defaultvalue)
  
  # override
  def write (self, stream):
    stream.write(str(self.get_value(defaultvalue="")))
  