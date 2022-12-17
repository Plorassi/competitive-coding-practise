class Solution(object):
    def cherryPickup(self, grid):
        
        N = len(grid)
        dp = {}
        
        def dfs(r1,c1,c2):
            
            r2 = r1+c1-c2
            
            if (r1,c1,c2) in dp:
                return dp[(r1,c1,c2)]
            
            if r1 >= N or c1 >= N or r2 >= N or c2 >= N or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            
            if r1 == N-1 and c1 == N-1:
                return grid[r1][c1]
            
            ans = grid[r1][c1] + (c1!=c2)*grid[r2][c2]
            ans += max(dfs(r1,c1+1,c2+1), dfs(r1+1,c1,c2), dfs(r1+1,c1,c2+1), dfs(r1,c1+1,c2))
            dp[(r1,c1,c2)] = ans
            return ans
        
        return max(0,dfs(0,0,0))
