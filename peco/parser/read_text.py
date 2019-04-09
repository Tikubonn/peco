
from peco.template import TextNode
from io import StringIO

def read_text (preread, stream, parser):
  with StringIO() as readstr:
    readstr.write(preread)
    while True:
      character = stream.peek()
      if not character:
        break
      if parser.is_syntax_character(character):
        break
      readstr.write(character)
      stream.get()
    return TextNode(readstr.getvalue())
  