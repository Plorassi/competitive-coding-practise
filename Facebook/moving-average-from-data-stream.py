class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()

    def next(self, val: int) -> float:
        self.queue.append(val)

        if len(self.queue) > self.size:
            self.queue.popleft()

        average = sum(self.queue) / len(self.queue)
        return average
