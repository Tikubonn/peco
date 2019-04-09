
from .syntax_error import SyntaxError
from .read_whitespace import read_whitespace
from peco.template import TrimNode, Evaluatable

def read_trim (preread, stream, parser):
  read_whitespace("", stream, parser) # trim whitespace!
  variable = parser.read(stream)
  if not isinstance(variable, Evaluatable):
    raise SyntaxError("read unsupported type.")
  return TrimNode(variable)
