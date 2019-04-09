
from unittest import TestCase
from peco.template import JoinNode, TextNode, VariableNode, Scope
from io import StringIO

class TestJoinNode (TestCase):
  
  def test_write (self):
    with StringIO() as stream:
      separator = TextNode(",")
      scope = Scope()
      variable = VariableNode("a", scope)
      variable.set_value(["a", "b", "c"])
      node = JoinNode(separator, variable)
      node.write(stream)
      self.assertEqual(stream.getvalue(), "a,b,c")
