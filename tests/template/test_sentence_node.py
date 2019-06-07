
from unittest import TestCase
from peco.template import SentenceNode, TextNode
from io import StringIO


class TestSentenceNode (TestCase):

    def test_write(self):
        with StringIO() as stream:
            text1 = "a"
            text2 = "b"
            text3 = "c"
            node = SentenceNode()
            node.add(TextNode(text1))
            node.add(TextNode(text2))
            node.add(TextNode(text3))
            node.write(stream)
            self.assertEqual(stream.getvalue(), text1 + text2 + text3)
