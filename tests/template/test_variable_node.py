
from unittest import TestCase
from peco.template import VariableNode, Scope
from io import StringIO

class TestVariableNode (TestCase):
  
  def test_access_value (self):
    value = "this is variable nodes value."
    scope = Scope()
    node = VariableNode("a", scope)
    self.assertEqual(node.get_value(defaultvalue=None), None) # test
    node.set_value(value)
    self.assertEqual(node.get_value(defaultvalue=None), value) # test
  
  def test_write (self):
    value = "this is variable nodes value."
    scope = Scope()
    node = VariableNode("a", scope)
    node.set_value(value)
    with StringIO() as stream:
      node.write(stream)
      self.assertEqual(stream.getvalue(), value) # test
  