from src.array import Queue as ArrayQueue, Stack as ArrayStack, Vector as ArrayVector
from src.linkedList import Queue as LLQueue, Stack as LLStack
from src.tree import Heap


class DSFactory(object):

    def __init__(self):
        print("Factory Created")

    def makeHeap(self, size, comparer):
        return Heap.Heap(size, comparer)

    def makeArrayStack(self, value):
        return ArrayStack.Stack(value)

    def makeArrayQueue(self, value):
        return ArrayQueue.Queue(value)

    def makeArrayVector(self, value):
        return ArrayVector.Vector(value)

    def makeListQueue(self):
        return LLQueue.Queue()

    def makeListStack(self):
        return LLStack.Stack()
