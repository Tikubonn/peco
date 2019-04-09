
from unittest import TestCase
from peco.template import TextNode
from io import StringIO

class TestTextNode (TestCase):
  
  def test_write (self):
    content = "this is text nodes content."
    node = TextNode(content)
    with StringIO() as stream:
      node.write(stream)
      self.assertEqual(stream.getvalue(), content) # test
  