import heapq

class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []
        self.index = 0

    def push(self, board):
        heapq.heappush(self.queue, (self.index, board))
        self.index += 1 

    def get_priority(self):
        return heapq.heappop(self.queue)[-1]