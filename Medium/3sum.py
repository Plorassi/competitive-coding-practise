class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        lenght = len(nums)
        
        for i in range(lenght):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, lenght-1
            while l < r:
                
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1

                        
        return res 
