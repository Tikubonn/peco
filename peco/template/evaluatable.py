
from abc import abstractmethod


class Evaluatable:

    @abstractmethod
    def set_value(self, value):
        pass

    @abstractmethod
    def get_value(self, defaultvalue=None):
        pass
