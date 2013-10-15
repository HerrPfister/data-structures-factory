from ds_src import LLQueue, LLStack, AQueue, AStack, AVector


class DSFactory(object):

    def __init__(self):
        print("Factory Created")

    def makeArrayStack(self, value):
        return AStack.AQueue(value)

    def makeArrayQueue(self, value):
        return AQueue.AQueue(value)

    def makeArrayVector(self, value):
        return AVector.AVector(value)

    def makeListQueue(self):
        return LLQueue.LLQueue()

    def makeListStack(self):
        return LLStack.LLStack()