class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:

        dp = [[0]*(len(days[0])+1) for _ in range(len(days)+1)]

        for j in range(len(days[0]))[::-1]:
            for i in range(len(days)):
                dp[i][j] = days[i][j] + dp[i][j+1]
                for k in range(len(flights)):
                    if flights[i][k]:
                        dp[i][j] = max(dp[i][j], days[k][j]+dp[k][j+1])

        return dp[0][0]

