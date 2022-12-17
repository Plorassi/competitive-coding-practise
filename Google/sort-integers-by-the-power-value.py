class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        dp = {1:0}
        
        def power(x):
            if x in dp:
                return dp[x]
            if x % 2 == 0:
                dp[x] = 1 + power(x // 2)
            else:
                dp[x] = 1 + power(3 * x + 1)
            return dp[x]
        
        res = []
        for i in range(lo,hi+1):
            res.append([power(i),i])
        return sorted(res)[k-1][1]
