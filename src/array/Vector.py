class Vector(object):

    def __init__(self, size):
        self.container = [None] * size
        self.current_size = 0
        self.max = size

    def __len__(self):
        return self.current_size

    @property
    def first(self):
        if self.isEmpty():
            print("Vector is Empty")
            return None

        return self.container[0]

    @property
    def last(self):
        if self.isEmpty():
            print("Vector is Empty")
            return None

        return self.container[self.current_size - 1]

    def printVector(self):
        for x in self.container:
            print(("%s, " % x))

    def insertAt(self, value, rank):
        if self.isFull():
            return "Vector is Full"

        rank = rank - 1

        x = self.current_size
        while x > rank:
            self.container[x] = self.container[x - 1]
            x = x - 1

        self.container[rank] = value
        self.current_size = self.current_size + 1

    def insertFirst(self, value):
        if self.isFull():
            return "Vector is Full"

        x = self.current_size
        while x > 0:
            self.container[x] = self.container[x - 1]
            x = x - 1

        self.container[0] = value
        self.current_size = self.current_size + 1

    def insertLast(self, value):
        if self.isFull():
            return "Vector is Full"

        self.container[self.current_size] = value
        self.current_size = self.current_size + 1

    def isEmpty(self):
        if self.current_size == 0:
            return True
        return False

    def isFull(self):
        if self.current_size == self.max:
            return True
        return False