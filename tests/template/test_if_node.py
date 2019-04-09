
from unittest import TestCase
from peco.template import IfNode, TextNode, VariableNode, Scope
from io import StringIO

class TestIfNode (TestCase):
  
  def test_write (self):
    scope = Scope()
    variable = VariableNode("a", scope)
    thennode = TextNode("true")
    elsenode = TextNode("false")
    ifnode = IfNode(variable, thennode, elsenode)
    # when undefined
    with StringIO() as stream:
      ifnode.write(stream)
      self.assertEqual(stream.getvalue(), "false")
    # when true
    variable.set_value(True)
    with StringIO() as stream:
      ifnode.write(stream)
      self.assertEqual(stream.getvalue(), "true")
    # when false
    variable.set_value(False)
    with StringIO() as stream:
      ifnode.write(stream)
      self.assertEqual(stream.getvalue(), "false")
  