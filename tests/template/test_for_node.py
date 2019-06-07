
from unittest import TestCase
from peco.template import ForNode, SentenceNode, VariableNode, Scope
from io import StringIO


class TestForNode (TestCase):

    def test_write(self):
        with StringIO() as stream:
            scope = Scope()
            source = VariableNode("a", scope)
            source.set_value(["a", "b", "c"])
            variable = VariableNode("a", scope)
            sentence = SentenceNode()
            sentence.add(variable)
            fornode = ForNode(source, variable, sentence, scope)
            fornode.write(stream)
            self.assertEqual(stream.getvalue(), "abc")
