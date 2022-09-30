class Solution:

    def __init__(self, nums: List[int]):
        self.tmp = collections.defaultdict(list)
        for i,n in enumerate(nums):
            self.tmp[n].append(i)
        

    def pick(self, target: int) -> int:
        x = random.randint(0,len(self.tmp[target])-1)
        return self.tmp[target][x]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
