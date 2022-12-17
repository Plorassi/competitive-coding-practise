class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.arr = encoding
        self.cur = 0

    def next(self, n: int) -> int:
        while self.cur < len(self.arr):
            if n <= self.arr[self.cur]:
                self.arr[self.cur] -= n
                return self.arr[self.cur+1]
            n -= self.arr[self.cur]
            self.cur += 2
        return -1
        

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
