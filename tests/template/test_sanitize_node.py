
from unittest import TestCase
from peco.template import SanitizeNode, VariableNode, Scope
from io import StringIO

class TestSanitizeNode (TestCase):
  
  def test_write (self):
    scope = Scope()
    variable = VariableNode("a", scope)
    node = SanitizeNode(variable)
    # when undefined
    with StringIO() as stream:
      node.write(stream)
      self.assertEqual(stream.getvalue(), "")
    # when set value
    variable.set_value("<br>")
    with StringIO() as stream:
      node.write(stream)
      self.assertEqual(stream.getvalue(), "&lt;br&gt;")
    