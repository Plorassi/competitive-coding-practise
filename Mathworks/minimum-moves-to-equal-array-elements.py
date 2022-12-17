class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums))[::-1]:
            ans += nums[i] - nums[0]
        return ans
        
