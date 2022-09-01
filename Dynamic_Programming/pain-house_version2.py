class Solution:

    def min_cost(self, costs: List[List[int]]) -> int:

        if not costs:
            return 0

        dp = [[c for c in costs[0]] for j in costs]

        for i in range(1,len(costs)):
            for j in range(3):
                x = dp[i-1].pop(j)
                dp[i][j] = costs[i][j] + min(dp[i-1])
                dp[i-1].insert(j,x)

        return min(dp[-1])


