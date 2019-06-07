
from .read_whitespace import read_whitespace
from peco.template import SanitizeNode


def read_sanitize(preread, stream, parser):
    read_whitespace("", stream, parser)  # trim whitespace!
    variable = parser.read(stream)
    return SanitizeNode(variable)
