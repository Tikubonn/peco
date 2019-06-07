
from .end_for import EndFor
from .syntax_error import SyntaxError
from .read_whitespace import read_whitespace
from .read_close_paren import read_close_paren
from peco.template import TextNode, SentenceNode, ForNode, Evaluatable


def read_in(preread, stream, parser):
    if stream.read(2) != "in":
        raise SyntaxError("could not read \"in\".")
    return TextNode("")


def read_beginning(preread, stream, parser):
    read_whitespace("", stream, parser)
    variable = parser.read(stream)
    if not isinstance(variable, Evaluatable):
        raise SyntaxError("read unsupported type.")
    read_whitespace("", stream, parser)
    read_in("", stream, parser)
    read_whitespace("", stream, parser)
    source = parser.read(stream)
    if not isinstance(source, Evaluatable):
        raise SyntaxError("read unsupported type.")
    read_whitespace("", stream, parser)
    read_close_paren("", stream, parser)
    return variable, source


def read_for(preread, stream, parser):
    variable, source = read_beginning("", stream, parser)
    sentence = SentenceNode()
    try:
        while stream.peek():
            node = parser.read(stream)
            sentence.add(node)
        raise SyntaxError("reached eof.")
    except EndFor:
        return ForNode(source, variable, sentence.trim(), parser.get_scope())
