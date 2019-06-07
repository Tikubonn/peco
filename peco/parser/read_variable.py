
from io import StringIO
from peco.template import VariableNode, MemberNode
import string


def read_variable_text(stream):
    with StringIO() as readstr:
        while True:
            character = stream.peek()
            if not character:
                break
            if character not in string.ascii_letters + "_" + ".":
                break
            readstr.write(character)
            stream.get()
        return readstr.getvalue()


def read_variable(preread, stream, parser):
    text = read_variable_text(stream)
    node = None
    for part in text.split("."):
        if node is None:
            node = VariableNode(part, scope=parser.get_scope())
        else:
            node = MemberNode(part, node)
    return node
