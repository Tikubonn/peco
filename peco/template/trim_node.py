
from .writer import Writer
from .evaluatable import Evaluatable
import string


class TrimNode (Writer, Evaluatable):

    def __init__(self, node):
        self.node = node

    # override
    def get_value(self, defaultvalue=None):
        return str(self.node.get_value(defaultvalue="")).strip(string.whitespace)

    # override
    def write(self, stream):
        stream.write(self.get_value(defaultvalue=""))
