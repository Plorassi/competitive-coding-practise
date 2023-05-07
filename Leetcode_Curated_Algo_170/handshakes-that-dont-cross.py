class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        dp = [0]*(numPeople+1)
        m = 1000000007
        dp[0] = 1
        
        for i in range(2,numPeople+1,2):
            for j in range(0,i,2):
                dp[i] += dp[j]*dp[i-j-2]
                dp[i] %= m

        return dp[numPeople]
