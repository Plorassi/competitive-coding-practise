class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.append(nums[0])
        
        l = len(nums)
        
        for i in range(l):
            nums[nums[i]%l] += l
            
        for i in range(l):
            if nums[i] < l:
                return i
