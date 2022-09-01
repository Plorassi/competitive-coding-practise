class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = {0:1, 1:1}
        
        def dfs(x):
            if x in dp:
                return dp[x]
            
            dp[x] = 0
            for i in range(x):
                dp[x] += (dfs(i) * dfs(x-i-1))
                
            return dp[x]
        
        return dfs(n)
