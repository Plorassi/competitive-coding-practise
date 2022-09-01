class Solution:
    def minDays(self, n: int) -> int:
        
        dp = {0:0,1:1}
        
        def dfs(x):
            
            if x in dp:
                return dp[x]
            
            l = x%2 + dfs(x//2)
            m = x%3 + dfs(x//3)
            
            dp[x] = 1 + min(l,m)
            
            return dp[x]
        
        return dfs(n)
