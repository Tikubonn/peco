
from peco.template import TextNode
from .read_whitespace import read_whitespace
from .syntax_error import SyntaxError


def read_close_paren(preread, stream, parser):
    read_whitespace("", stream, parser)
    if stream.read(3) != "-->":
        raise SyntaxError("could not read \"-->\".")
    return TextNode("")
