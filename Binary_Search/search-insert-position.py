class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1
        while l <= r:
            
            mid = (l+r)//2
        
            if nums[mid] > target:
                r = mid - 1 
            else:
                l = mid + 1
                
        if nums[r] == target:
            return r
        else:
            return l
            
            
            
        
