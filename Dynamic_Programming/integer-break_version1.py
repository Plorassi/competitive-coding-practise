class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = {1:1}
        
        def dfs(num):
            if num in dp:
                return dp[num]
            
            if num == n:
                dp[num] = 0
            else:
                dp[num] = num
                
            for i in range(1,num):
                dp[num] = max(dp[num], dfs(i)*dfs(num-i))
                
            return dp[num]
        
        return dfs(n)
