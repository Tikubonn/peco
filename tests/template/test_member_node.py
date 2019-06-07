
from unittest import TestCase
from peco.template import MemberNode, VariableNode, Scope
from io import StringIO


class TestMemberNode (TestCase):

    def test_get_value(self):
        scope = Scope()
        variable = VariableNode("person", scope)
        member = MemberNode("name", variable)
        # when undefined
        self.assertEqual(member.get_value(defaultvalue=None), None)
        # when did set
        variable.set_value({"name": "tikubonn"})
        self.assertEqual(member.get_value(defaultvalue=None), "tikubonn")

    def test_write(self):
        scope = Scope()
        variable = VariableNode("person", scope)
        member = MemberNode("name", variable)
        # when undefined
        with StringIO() as stream:
            member.write(stream)
            self.assertEqual(stream.getvalue(), "")
        # when did set
        variable.set_value({"name": "tikubonn"})
        with StringIO() as stream:
            member.write(stream)
            self.assertEqual(stream.getvalue(), "tikubonn")
