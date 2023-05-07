class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:

        next = [-1]*len(coins)
        dp = [c for c in coins]
        if coins[-1] == -1:
            return []

        for i in range(len(coins)-1)[::-1]:
            minCost = float('inf')
            for j in range(1,maxJump+1):
                nx = i+j
                if nx<len(coins) and coins[nx]>=0:
                    tmp = coins[i] + dp[nx]
                    if tmp < minCost:
                        minCost = tmp
                        next[i] = nx
            dp[i] = minCost
        
        i = 0
        res = [1]
        while i<len(coins)-1 and next[i] >= 0:
            i = next[i]
            res.append(i+1)
        return res if res[-1] == len(coins) else []
