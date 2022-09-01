class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(i,j):
            
            if (i<0 or j<0 or
                i >= ROWS or j >= COLS or
                grid[i][j] == 0):
                return 1
            
            if (i,j) in visit:
                return 0
            
            visit.add((i,j))
            return (dfs(i+1,j)+dfs(i,j+1)+dfs(i-1,j)+dfs(i,j-1))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return dfs(r,c)
                
                
        
            
            
