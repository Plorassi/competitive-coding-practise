class Solution:

    def min_cost(self, costs: List[List[int]]) -> int:

        dp = {}

        def dfs(i,j):

            if (i,j) in dp:
                return dp[(i,j)]

            if i == len(costs)-1:
                return costs[i][j]

            if i >= len(costs):
                return 0

            dp[(i,j)] = float('inf')
            for k in range(len(costs[i])):
                if k != j:
                    dp[(i,j)] = min(dp[(i,j)], costs[i][j] + dfs(i+1, k))

            return dp[(i,j)]

        if  not costs:
            return 0
        return min(dfs(0,0), dfs(0,1), dfs(0,2))
