
from unittest import TestCase
from peco.parser import parse, parse_string


class TestParseSanitize (TestCase):

    def test_parse(self):
        template = parse_string("@sanitize $value")
        # when undefined
        self.assertEqual(template.render_string(), "")
        # when html code
        self.assertEqual(template.render_string(value="<br>"), "&lt;br&gt;")
