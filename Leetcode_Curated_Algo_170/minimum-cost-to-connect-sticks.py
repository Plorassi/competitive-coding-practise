class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        heapq.heapify(sticks)
        res = 0

        while len(sticks) > 1:
            val1 = heapq.heappop(sticks)
            val2 = heapq.heappop(sticks)
            res += val1 + val2
            heapq.heappush(sticks, val1+val2)

        return res
