class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res, cur = nums[0], nums[0]
        
        for n in nums[1:]:
            cur = max(n,cur+n)
            res = max(res, cur)
            
        return res
