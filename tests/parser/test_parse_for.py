
from unittest import TestCase
from peco.parser import parse, parse_string


class TestParseFor (TestCase):

    def test_parse(self):
        template = parse_string(
            "<!-- @for $element in $iter --> $element <!-- @endfor -->")
        # when undefined
        self.assertEqual(template.render_string(), "")
        # when (a, b, c)
        self.assertEqual(template.render_string(iter=["a", "b", "c"]), "abc")
