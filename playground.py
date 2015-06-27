__author__ = 'matthias'


class FIFO():
    def __init__(self, max_size=64):
        self.max_size = max_size
        self.data = [None] * self.max_size
        self.read = 0
        self.write = 0
        self.full = False

    def available(self):
        return self.read != self.write

    def get(self):
        if self.available():
            if self.full:
                self.write = (self.write + 1) % self.max_size
                self.full = False
            item = self.data[self.read]
            self.read = (self.read + 1) % self.max_size
            return item
        else:
            raise Exception()

    def put(self, item):
        if self.full:
            raise Exception()
        self.data[self.write] = item
        next_write = (self.write + 1) % self.max_size
        if self.read == next_write:
            self.full = True
        else:
            self.write = next_write


