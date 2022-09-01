class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        dp = {}
        
        def dfs(i,j):
            if i >= rows or j >= cols:
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            dp[(i,j)] = 0
            right = dfs(i,j+1)
            down = dfs(i+1,j)
            diag = dfs(i+1,j+1)
            
            if matrix[i][j] == '1':
                dp[(i,j)] = 1 + min(right, down, diag)
                
            return dp[(i,j)]
        
        dfs(0,0)
        return max(dp.values())**2
