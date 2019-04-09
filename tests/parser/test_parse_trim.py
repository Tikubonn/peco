
from unittest import TestCase
from peco.parser import parse, parse_string

class TestParseJoin (TestCase):
  
  def test_parse (self):
    template = parse_string("@trim $value")
    # when undefined
    self.assertEqual(template.render_string(), "")
    # when "monaco"
    self.assertEqual(template.render_string(value="monaco"), "monaco")
    # when "  monaco"
    self.assertEqual(template.render_string(value="  monaco"), "monaco")
    # when "monaco  "
    self.assertEqual(template.render_string(value="monaco  "), "monaco")
    # when "  monaco  "
    self.assertEqual(template.render_string(value="  monaco  "), "monaco")
