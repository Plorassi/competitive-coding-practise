class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = {}
        
        def dfs(x):
            
            if x in dp:
                return dp[x]
            
            if x == 0:
                return 1
            
            dp[x] = 0
            for num in nums:
                if x-num >= 0:
                    dp[x] += dfs(x-num)
                    
            return dp[x]
                

        return dfs(target)
