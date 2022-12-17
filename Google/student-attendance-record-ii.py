class Solution:
    def checkRecord(self, n: int) -> int:
        
        dp = {0:1, 1:2, 2:4, 3:7}
        
        for i in range(4,n+1):
            dp[i] = (2*dp[i-1] - dp[i-4])%(10**9+7)
            
        ans = dp[n]
        
        for i in range(1,n+1):
            ans += (dp[i-1]*dp[n-i])%(10**9+7)
            
        return ans%(10**9+7)
        
    
