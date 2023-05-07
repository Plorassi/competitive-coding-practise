class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        prefix, res = 0, 0
        indices = {}
        for i,n in enumerate(nums):
            prefix += n
            if prefix == k:
                res = i+1

            if prefix - k in indices:
                res = max(res, i-indices[prefix-k])

            if prefix not in indices:
                indices[prefix] = i

        return res

        
