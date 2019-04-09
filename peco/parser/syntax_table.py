
from .syntax_node import SyntaxNode
from .syntax_error import SyntaxError
from io import StringIO

class SyntaxTable (SyntaxNode):
  
  def __init__ (self, function=None):
    super().__init__(function=function)
  
  def register (self, code, function):
    node = self
    for character in code:
      node = node.dig(character)
    node.set_function(function)
  
  def try_call (self, readstr, node, stream, *arguments, **keywords):
    function = node.get_function()
    if not function:
      default_function = self.get_function()
      if not default_function:
        raise SyntaxError("%s was unmatched to syntax." % (readstr.getvalue(),))
      return default_function(
        readstr.getvalue(),
        stream,
        *arguments,
        **keywords)
    return function(
      readstr.getvalue(),
      stream,
      *arguments,
      **keywords)
  
  def read (self, stream, *arguments, **keywords):
    with StringIO() as readstr:
      node = self
      while True:
        character = stream.peek()
        # when reached eof
        if not character:
          return self.try_call(readstr, node, stream, *arguments, **keywords)
        newnode = node.get(character)
        # when not found
        if not newnode:
          return self.try_call(readstr, node, stream, *arguments, **keywords)
        stream.get()
        readstr.write(character)
        node = newnode
      return None

## define default_syntax_table :D

from .read_whitespace import read_whitespace
from .read_variable import read_variable
from .read_text import read_text
from .read_if import read_if
from .read_if_then import read_if_then
from .read_if_else import read_if_else
from .read_for import read_for
from .read_end_if import read_end_if
from .read_end_for import read_end_for
from .read_sanitize import read_sanitize
from .read_doll import read_doll
from .read_inline_if import read_inline_if
from .read_inline_if_then import read_inline_if_then
from .read_inline_if_else import read_inline_if_else
from .read_inline_end_if import read_inline_end_if
from .read_inline_for import read_inline_for
from .read_inline_end_for import read_inline_end_for
from .read_join import read_join 
from .read_at import read_at
from .read_trim import read_trim
import string

default_syntax_table = SyntaxTable()
default_syntax_table.set_function(read_text)
for character in string.whitespace:
  default_syntax_table.register(character, read_whitespace)
default_syntax_table.register("$", read_variable)
default_syntax_table.register("$$", read_doll)
default_syntax_table.register("<!-- @if", read_if)
default_syntax_table.register("<!-- @then -->", read_if_then)
default_syntax_table.register("<!-- @else -->", read_if_else)
default_syntax_table.register("<!-- @endif -->", read_end_if)
default_syntax_table.register("<!-- @for", read_for)
default_syntax_table.register("<!-- @endfor -->", read_end_for)
default_syntax_table.register("@sanitize", read_sanitize)
default_syntax_table.register("@if", read_inline_if)
default_syntax_table.register("@then", read_inline_if_then)
default_syntax_table.register("@else", read_inline_if_else)
default_syntax_table.register("@endif", read_inline_end_if)
default_syntax_table.register("@for", read_inline_for)
default_syntax_table.register("@endfor", read_inline_end_for)
default_syntax_table.register("@join", read_join)
default_syntax_table.register("@@", read_at)
default_syntax_table.register("@trim", read_trim)
