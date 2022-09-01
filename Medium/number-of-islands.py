class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        visit = set()
        
        def bfs(r,c):
            
            visit.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                
                if (row in range(rows) and 
                    col in range(cols) and
                    grid[row][col] == "1" and
                    (row,col) not in visit):
                    
                    bfs(row,col)
                    visit.add((row,col))
                
        
        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
                    
                    
        return islands
        
