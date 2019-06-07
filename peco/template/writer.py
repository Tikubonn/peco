
from abc import abstractmethod
from io import StringIO, TextIOBase


class Writer:

    @abstractmethod
    def write(self, stream: TextIOBase):
        pass
