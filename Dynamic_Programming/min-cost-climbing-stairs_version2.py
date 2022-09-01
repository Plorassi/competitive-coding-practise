class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [0,0]
        
        for i in range(2,len(cost)+1):
            l = cost[i-1] + dp[i-1]
            r = cost[i-2] + dp[i-2]
        
            dp.append(min(l,r))
            
        return dp[-1]
            
            
            
            
        
