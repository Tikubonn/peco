
from unittest import TestCase
from peco.template import Template, SentenceNode, VariableNode, Scope
from io import StringIO


class TestTemplate (TestCase):

    def test_render(self):
        with StringIO() as stream:
            scope = Scope()
            sentence = SentenceNode()
            sentence.add(VariableNode("a", scope))
            sentence.add(VariableNode("b", scope))
            sentence.add(VariableNode("c", scope))
            template = Template(sentence, scope)
            template.render(stream, a="a", b="b", c="c")
            self.assertEqual(stream.getvalue(), "abc")
