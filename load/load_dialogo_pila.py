"""Load dialog for pila (stack) UI."""

class DialogoPila:
    def __init__(self):
        # simple stack implementation using Python list
        self.pila = []

    def push(self, item):
        self.pila.append(item)

    def pop(self):
        if not self.pila:
            raise IndexError("pop from empty stack")
        return self.pila.pop()

    def peek(self):
        if not self.pila:
            return None
        return self.pila[-1]

    def is_empty(self):
        return len(self.pila) == 0

    def size(self):
        return len(self.pila)
