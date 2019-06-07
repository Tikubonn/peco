
from io import StringIO
from peco.template import WhitespaceNode
import string


def read_whitespace(preread, stream, parser):
    with StringIO() as readstr:
        readstr.write(preread)
        while True:
            character = stream.peek()
            if not character:
                break
            if character not in string.whitespace:
                break
            readstr.write(character)
            stream.get()
        return WhitespaceNode(readstr.getvalue())
