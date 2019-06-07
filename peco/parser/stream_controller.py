
class StreamController:

    def __init__(self, stream):
        self.stream = stream
        self.cache = None

    def peek(self):
        if self.cache is None:
            self.cache = self.stream.read(1)
        return self.cache

    def get(self):
        if self.cache is None:
            return self.stream.read(1)
        else:
            cache = self.cache
            self.cache = None
            return cache

    def read(self, size):
        if self.cache is None:
            return self.stream.read(size)
        else:
            cache = self.cache
            self.cache = None
            # precondition: cache.len == 1 and 0 < size
            return cache + self.stream.read(size - len(cache))
