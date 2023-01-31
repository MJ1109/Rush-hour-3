from collections import deque
​
class Queue:
    def __init__(self):
        self.items = deque()
    
    # add to the queue
    def enqueue(self, item):
        self.items.append(item)
    
    # remove first item
    def dequeue(self):
        return self.items.popleft()

    # get size of queue
    def size(self):
    return len(self.items)