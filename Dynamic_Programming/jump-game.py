class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        i = n-2
        temp = n-1
        while i >= 0:
            if temp - i <= nums[i]:
                temp = i
            i -= 1
            
        if temp == 0:
            return True
        else:
            return False
