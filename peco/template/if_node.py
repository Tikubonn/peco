
from .writer import Writer


class IfNode (Writer):

    def __init__(self, condnode, thennode, elsenode):
        self.condnode = condnode
        self.thennode = thennode
        self.elsenode = elsenode

    # override
    def write(self, stream):
        if self.condnode.get_value(defaultvalue=False):
            self.thennode.write(stream)
        else:
            self.elsenode.write(stream)
