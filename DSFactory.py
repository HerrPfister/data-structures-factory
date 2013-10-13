from ds_src import LLQueue, LLStack, AQueue, AStack


class DSFactory(object):

    def __init__(self):
        print("Factory Created")

    def makeArrayStack(self, value):
        return AStack.AQueue(value)

    def makeArrayQueue(self, value):
        return AQueue.AQueue(value)

    def makeListQueue(self):
        return LLQueue.LLQueue()

    def makeListStack(self):
        return LLStack.LLStack()