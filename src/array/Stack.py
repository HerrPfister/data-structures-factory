class Stack(object):

    def __init__(self, size):
        self.container = [None] * size
        self.max = size
        self.top = -1

    def __len__(self):
        return self.top + 1

    def push(self, value):
        if self.isFull():
            print("Stack is Full")
        else:
            self.top = self.top + 1
            self.container[self.top] = value

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"

        removed_value = self.container[self.top]
        self.container[self.top] = None
        self.top = self.top - 1
        return removed_value

    def isEmpty(self):
        if self.top < 0:
            return True
        return False

    def isFull(self):
        if self.top == (self.max - 1):
            return True
        return False

    @property
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")

        return self.container[self.top]
