class Stack(object):
    """Class to store the moves of the cars in, to keep track of efficiency"""
    def __init__(self):
        """ create empty stack"""
        self.items = []

    def push(self, item):
        """ insert items at the end of the stack"""
        return self.items.append(item)

    def pop(self):
        """ remove items at the end of the stack"""
        return self.items.pop()

    def size(self):
        """ returns size of the stack"""
        return len(self.items)

    def __repr__(self):
        return str(self.items)