import Node

class Stack(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, val):
        if self.isEmpty():
            self.head = Node.Node(val)
        else:
            newNode = Node.Node(val)
            newNode._next_setter = self.head
            self.head = newNode

        self.size = self.size + 1

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"

        value = self.head._value
        nodeToRemove = self.head._next
        self.head = self.head._next

        del nodeToRemove
        self.size = self.size - 1

        return value

    def isEmpty(self):
        if not self.head:
            return True
        return False

    @property
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.head._value