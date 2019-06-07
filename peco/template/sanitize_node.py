
from .writer import Writer
from .evaluatable import Evaluatable
from io import StringIO


class SanitizeNode (Writer, Evaluatable):

    @staticmethod
    def escape(source, stream):
        for character in source:
            if character == "<":
                stream.write("&lt;")
            elif character == ">":
                stream.write("&gt;")
            elif character == "&":
                stream.write("&amp;")
            elif character == "'":
                stream.write("&#39;")
            elif character == "\"":
                stream.write("&quot;")
            else:
                stream.write(character)

    def __init__(self, node):
        self.node = node

    # override
    def get_value(self, defaultvalue=None):
        with StringIO() as stream:
            source = self.node.get_value(defaultvalue="")
            SanitizeNode.escape(source, stream)
            return stream.getvalue()

    # override
    def write(self, stream):
        source = self.node.get_value(defaultvalue="")
        SanitizeNode.escape(source, stream)
