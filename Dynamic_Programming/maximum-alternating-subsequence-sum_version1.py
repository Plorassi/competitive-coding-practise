class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        dp = {}
        
        def backtrack(i, even):
            
            if i == len(nums):
                return 0
            
            if (i,even) in dp:
                return dp[(i,even)]
            
            if even:
                total = nums[i]
            else:
                total = -1*nums[i]
                
                
            dp[(i,even)] = max(total + backtrack(i+1, not even), backtrack(i+1, even))
            
            return dp[(i,even)]
        
        
        return backtrack(0,True)
        
        
