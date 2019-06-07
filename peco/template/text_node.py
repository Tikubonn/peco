
from .writer import Writer


class TextNode (Writer):

    def __init__(self, text):
        self.text = text

    # override
    def write(self, stream):
        stream.write(str(self.text))
