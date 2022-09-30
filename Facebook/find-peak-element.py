class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1
        
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if mid>0 and mid<len(nums)-1 and nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid
            if mid>0 and nums[mid-1]>nums[mid]:
                high=mid-1
            else:
                low=mid+1
        return -1
        
