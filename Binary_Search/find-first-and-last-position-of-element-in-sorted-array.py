class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l,r = 0, len(nums)-1
        end = -1
        start = r+1
        
        while l<=r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                end = max(end, m)
                l = m+1
             
        l,r = 0, len(nums)-1
        
        while l<=r:
            m = (l+r)//2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                start = min(start, m)
                r = m-1
                
        if start == len(nums):
            start = -1
        
        return [start, end]
