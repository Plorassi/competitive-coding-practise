class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start, end = -1, -1
        
        if not nums or len(nums) == 0:
            return [start, end]
        
        l,r = 0, len(nums)-1
        
        while l <= r:
            
            m = (l+r)//2
            
            if nums[m] < target:
                l = m+1
            else:
                r = m-1
                
        start = r+1

        l,r = 0, len(nums)-1
        
        while l <= r:
            
            m = (l+r)//2
            
            if nums[m] > target:
                r = m-1
            else:
                l = m+1
                
        end = l-1
        
        return [start, end] if start in range(len(nums)) and nums[start] == target else [-1,-1]
        
