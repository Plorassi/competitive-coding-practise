class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        left, right, count = {}, {}, collections.defaultdict(int)
        
        for i,n in enumerate(nums):
            if n not in left:
                left[n] = i
            right[n] = i
            count[n] += 1
            
        m = max(count.values())
        res = float('inf')
        for key,value in count.items():
            if value == m:
                res = min(res, right[key] - left[key] + 1)
        return res
