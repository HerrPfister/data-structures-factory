class AQueue(object):

    def __init__(self, size):
        self.container = [None] * size
        self.current_size = 0
        self.front_item = 0
        self.empty_space = 0
        self.max = size

    def __len__(self):
        return self.current_size

    def enqueue(self, value):
        if self.isFull():
            print("Queue is full")
        else:
            self.container[self.empty_space] = value
            self.empty_space = (self.empty_space + 1) % self.max
            self.current_size = self.current_size + 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"

        removed_value = self.container[self.front_item]
        self.container[self.front_item] = None
        self.front_item = (self.front_item + 1) % self.max
        self.current_size = self.current_size - 1
        return removed_value

    def isEmpty(self):
        if self.current_size == 0:
            return True
        return False

    def isFull(self):
        if self.current_size == self.max:
            return True
        return False

    @property
    def front(self):
        if self.isEmpty():
            return "Queue is Empty"

        return self.container[self.front_item]