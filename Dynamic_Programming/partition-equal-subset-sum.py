class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        dp = {}
        
        SUM = sum(nums)
        
        if SUM%2:
            return 0
        
        SUM = SUM//2
        
        def dfs(i,s):
            
            if s == 0:
                return True
            
            if s < 0:
                return False
            
            if i == len(nums):
                return False
            
            
            if (i,s) in dp:
                return dp[(i,s)]
   
            dp[(i,s)] = dfs(i+1, s-nums[i]) or dfs(i+1, s)
    
            return dp[(i,s)]
    
        return dfs(0,SUM)
