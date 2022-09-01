class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        lp, rp = 0, len(nums)-1
        
        i = 0
        
        while i <= rp:
            
            if nums[i] == 0:
                nums[i] = nums[lp]
                nums[lp] = 0
                lp += 1
                i += 1
                
            elif nums[i] == 2:
                nums[i] = nums[rp]
                nums[rp] = 2
                rp -= 1
                
            else:
                i += 1
                
            
