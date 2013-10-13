class LLNode(object):

    def __init__(self, val):
        self.value = val
        self.next = None

    @property
    def _next(self):
        return self.next

    @_next.setter
    def _next_setter(self, n):
        self.next = n

    @property
    def _value(self):
        return self.value

    @_value.setter
    def _value_setter(self, val):
        self.value = val
