
from io import StringIO

class SyntaxNode:
  
  def __init__ (self, character=None, function=None):
    self.table = list()
    self.character = character
    self.function = function
      
  def get_function (self):
    return self.function
  
  def set_function (self, function):
    self.function = function
  
  def get (self, character):
    for node in self.table:
      if node.character == character:
        return node
    return None
  
  def has_character (self, character):
    for node in self.table:
      if node.character == character:
        return True
    return False
  
  def dig (self, character):
    if not self.has_character(character):
      self.table.append(SyntaxNode(character))
    return self.get(character)
  