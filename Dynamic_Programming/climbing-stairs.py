class Solution:
    def climbStairs(self, n: int) -> int:

        dp = {}
        
        def backtrack(x):
            if x == 1:
                return 1
            if x == 2:
                return 2
            
            if x in dp:
                return dp[x]
            
            dp[x] = backtrack(x-1) + backtrack(x-2)
            
            return dp[x]
        
        return backtrack(n)
            
        
