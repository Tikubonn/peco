
from unittest import TestCase
from peco.parser import parse, parse_string

class TestParseInlineIf (TestCase):

  def test_parse1 (self):
    template = parse_string("@if $value true @else false @endif")
    # when undefined
    self.assertEqual(template.render_string(), "false")
    # when true
    self.assertEqual(template.render_string(value=True), "true")
    # when false
    self.assertEqual(template.render_string(value=False), "false")
    
  def test_parse2 (self):
    template = parse_string("@if $value @then true @else false @endif")
    # when undefined
    self.assertEqual(template.render_string(), "false")
    # when true
    self.assertEqual(template.render_string(value=True), "true")
    # when false
    self.assertEqual(template.render_string(value=False), "false")
    
  def test_parse3 (self):
    template = parse_string("@if $value @then true @endif")
    # when undefined
    self.assertEqual(template.render_string(), "")
    # when true
    self.assertEqual(template.render_string(value=True), "true")
    # when false
    self.assertEqual(template.render_string(value=False), "")
  