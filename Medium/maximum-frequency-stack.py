class FreqStack:

    def __init__(self):
        self.count = collections.defaultdict(int)
        self.res = collections.defaultdict(list)
        self.maxCount = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        if self.count[val] > self.maxCount:
            self.maxCount = self.count[val] 
        self.res[self.count[val]].append(val)

    def pop(self) -> int:
        x = self.res[self.maxCount].pop()
        if not self.res[self.maxCount]:
            self.maxCount -= 1
        self.count[x] -= 1
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
