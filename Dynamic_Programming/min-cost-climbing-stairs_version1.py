class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        
        dp = {}
        
        def dfs(x):
            if x in dp:
                return dp[x]
            
            if x<=1:
                return 0
            
            l = cost[x-1] + dfs(x-1)
            m = cost[x-2] + dfs(x-2)
            
            dp[x] = min(l,m)
            
            return dp[x]
        
        return dfs(n)
