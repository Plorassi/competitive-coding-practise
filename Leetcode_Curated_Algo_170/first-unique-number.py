class FirstUnique:

    def __init__(self, nums: List[int]):
        
        self.hmap = {}
        self.q = collections.deque()

        for x in nums:
            if x in self.hmap:
                self.hmap[x] = False
            else:
                self.hmap[x] = True

            self.q.append(x)


    def showFirstUnique(self) -> int:
        while self.q and not self.hmap[self.q[0]]:
            self.q.popleft()
        return self.q[0] if self.q else -1
        

    def add(self, value: int) -> None:
        if value in self.hmap:
            self.hmap[value] = False
        else:
            self.hmap[value] = True
            self.q.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
