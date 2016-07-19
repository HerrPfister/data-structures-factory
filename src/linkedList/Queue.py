import Node


class Queue(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, val):
        if self.isEmpty():
            self.head = Node.Node(val)
            self.tail = self.head
        else:
            newNode = Node.Node(val)
            self.tail._next_setter = newNode
            self.tail = newNode

        self.size = self.size + 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"

        value = self.head._value
        nodeToRemove = self.head
        self.head = self.head._next

        del nodeToRemove
        self.size = self.size - 1

        return value

    def isEmpty(self):
        if not self.head:
            return True
        return False

    @property
    def front(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.head._value
