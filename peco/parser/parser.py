
from .syntax_table import default_syntax_table
from .stream_controller import StreamController
from peco.template import SentenceNode, Scope, Template
from io import StringIO, TextIOBase


def parse(stream: TextIOBase, syntaxtable=default_syntax_table):
    """
    parse source code from file-like object.

    Parameters
    ----------
    stream: io.TextIOBase
      this file-like object used to input.
    syntaxtable: peco.parser.SyntaxTable
      used to parse source code.
      default is peco.parser.default_syntax_table

    Returns
    -------
    template: peco.template.Template
      this is parsed result.
    """

    parser = Parser(syntaxtable)
    parser.parse(stream)
    template = parser.result()
    return template


def parse_string(source: str, syntaxtable=default_syntax_table):
    """
    parse source code from str object.

    Parameters
    ----------
    source: str
      source code for input.
    syntaxtable: peco.parser.SyntaxTable
      used to parse source code.
      default is peco.parser.default_syntax_table

    Returns
    -------
    template: peco.template.Template
      this is parsed result.
    """

    parser = Parser(syntaxtable)
    parser.parse_string(source)
    template = parser.result()
    return template


class Parser:

    def __init__(self, syntaxtable=default_syntax_table):
        self.syntaxtable = syntaxtable
        self.scope = Scope()
        self.sentencenode = SentenceNode()

    def get_scope(self):
        return self.scope

    def is_syntax_character(self, character):
        return self.syntaxtable.has_character(character)

    def read(self, stream: StreamController):
        return self.syntaxtable.read(stream, self)

    def parse(self, stream: TextIOBase):
        """
        parse source code from file-like object.

        Parameters
        ----------
        stream: io.TextIOBase
          this file-like object used to input.
        """

        controller = StreamController(stream)
        while controller.peek():
            node = self.read(controller)
            if node:
                self.sentencenode.add(node)

    def parse_string(self, source: str):
        """
        parse source code from str object.

        Parameters
        ----------
        source: str
          source code for input.
        """

        with StringIO(source) as stream:
            self.parse(stream)

    def result(self):
        """
        get template object that parsed from source code.

        Returns
        -------
        template: peco.template.Template
          parsed template
        """

        template = Template(
            self.sentencenode,
            self.scope)
        return template
