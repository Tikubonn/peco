
from .if_then import IfThen
from .if_else import IfElse
from .end_if import EndIf
from .read_whitespace import read_whitespace
from .read_variable import read_variable
from .read_close_paren import read_close_paren
from peco.template import IfNode, SentenceNode, Evaluatable


def read_beginning(preread, stream, parser):
    read_whitespace("", stream, parser)
    variable = parser.read(stream)
    if not isinstance(variable, Evaluatable):
        raise SyntaxError("loaded unsupported type.")
    read_whitespace("", stream, parser)
    read_close_paren("", stream, parser)
    return variable


def read_then(preread, stream, parser, thennode=None, elsenode=None):
    thensentence = SentenceNode()
    try:
        while stream.peek():
            node = parser.read(stream)
            thensentence.add(node)
        raise SyntaxError("reached eof.")
    except IfThen:
        return read_then(preread, stream, parser, thennode=thensentence, elsenode=elsenode)
    except IfElse:
        return read_else(preread, stream, parser, thennode=thensentence, elsenode=elsenode)
    except EndIf:
        return thensentence, elsenode


def read_else(preread, stream, parser, thennode=None, elsenode=None):
    elsesentence = SentenceNode()
    try:
        while stream.peek():
            node = parser.read(stream)
            elsesentence.add(node)
        raise SyntaxError("reached eof.")
    except IfThen:
        return read_then(preread, stream, parser, thennode=thennode, elsenode=elsesentence)
    except IfElse:
        return read_else(preread, stream, parser, thennode=thennode, elsenode=elsesentence)
    except EndIf:
        return thennode, elsesentence


def read_if(preread, stream, parser):
    variable = read_beginning("", stream, parser)
    thennode, elsenode = read_then("", stream, parser)
    return IfNode(
        variable,
        thennode.trim() if thennode else SentenceNode(),
        elsenode.trim() if elsenode else SentenceNode())
