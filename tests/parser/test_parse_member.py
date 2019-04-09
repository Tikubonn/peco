
from unittest import TestCase
from peco.parser import parse, parse_string

class TestParseMember (TestCase):
  
  def test_parse (self):
    template = parse_string("$person.name")
    # when undefined
    self.assertEqual(template.render_string(), "")
    # when did set
    self.assertEqual(template.render_string(person={"name": "tikubonn"}), "tikubonn")
  