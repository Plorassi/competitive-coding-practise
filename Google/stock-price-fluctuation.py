class StockPrice:

    def __init__(self):
        self.hmap = {}
        self.latest = 0
        self.minHeap = []
        self.maxHeap = []

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.latest:
            self.latest = timestamp
        self.hmap[timestamp] = price
        heapq.heappush(self.minHeap,(price, timestamp))
        heapq.heappush(self.maxHeap,(-price, timestamp))

    def current(self) -> int:
        return self.hmap[self.latest]
        
    def maximum(self) -> int:
        while self.maxHeap:
            price, timestamp = heapq.heappop(self.maxHeap)
            price = abs(price)
            if price == self.hmap[timestamp]:
                heapq.heappush(self.maxHeap, (-price, timestamp))
                return price
        return 0

    def minimum(self) -> int:
        while self.minHeap:
            price, timestamp = heapq.heappop(self.minHeap)
            if price == self.hmap[timestamp]:
                heapq.heappush(self.minHeap, (price, timestamp))
                return price
        return 0
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
