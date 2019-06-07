
from .inline_end_for import InlineEndFor
from .syntax_error import SyntaxError
from .read_whitespace import read_whitespace
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
    return variable, source


def read_inline_for(preread, stream, parser):
    variable, source = read_beginning("", stream, parser)
    sentence = SentenceNode()
    try:
        while stream.peek():
            node = parser.read(stream)
            sentence.add(node)
        raise SyntaxError("reached eof.")
    except InlineEndFor:
        return ForNode(source, variable, sentence.trim(), parser.get_scope())
