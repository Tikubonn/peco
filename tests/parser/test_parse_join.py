
from unittest import TestCase
from peco.parser import parse, parse_string

class TestParseJoin (TestCase):
  
  def test_parse (self):
    template = parse_string("@join , $iter")
    # when undefined
    self.assertEqual(template.render_string(), "")
    # when (a, b, c)
    self.assertEqual(template.render_string(iter=["a", "b", "c"]), "a,b,c")
    