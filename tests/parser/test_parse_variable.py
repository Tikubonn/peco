
from unittest import TestCase
from peco.parser import parse, parse_string


class TestParseVariable (TestCase):

    def test_parse(self):
        template = parse_string("$name")
        # when undefined
        self.assertEqual(template.render_string(), "")
        # when did set
        self.assertEqual(template.render_string(name="tikubonn"), "tikubonn")
