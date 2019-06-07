
from .inline_if_then import InlineIfThen
from .inline_if_else import InlineIfElse
from .inline_end_if import InlineEndIf
from .read_whitespace import read_whitespace
from peco.template import IfNode, SentenceNode, Evaluatable


def read_beginning(preread, stream, parser):
    read_whitespace("", stream, parser)
    variable = parser.read(stream)
    if not isinstance(variable, Evaluatable):
        raise SyntaxError("loaded unsupported type.")
    read_whitespace("", stream, parser)
    return variable


def read_then(preread, stream, parser, thennode=None, elsenode=None):
    thensentence = SentenceNode()
    try:
        while stream.peek():
            node = parser.read(stream)
            thensentence.add(node)
        raise SyntaxError("reached eof.")
    except InlineIfThen:
        return read_then(preread, stream, parser, thennode=thensentence, elsenode=elsenode)
    except InlineIfElse:
        return read_else(preread, stream, parser, thennode=thensentence, elsenode=elsenode)
    except InlineEndIf:
        return thensentence, elsenode


def read_else(preread, stream, parser, thennode=None, elsenode=None):
    elsesentence = SentenceNode()
    try:
        while stream.peek():
            node = parser.read(stream)
            elsesentence.add(node)
        raise SyntaxError("reached eof.")
    except InlineIfThen:
        return read_then(preread, stream, parser, thennode=thennode, elsenode=elsesentence)
    except InlineIfElse:
        return read_else(preread, stream, parser, thennode=thennode, elsenode=elsesentence)
    except InlineEndIf:
        return thennode, elsesentence


def read_inline_if(preread, stream, parser):
    variable = read_beginning("", stream, parser)
    thennode, elsenode = read_then("", stream, parser)
    return IfNode(
        variable,
        thennode.trim() if thennode else SentenceNode(),
        elsenode.trim() if elsenode else SentenceNode())
