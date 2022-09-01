class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid1), len(grid1[0])
        visit = set()
        res = 0
        
        def dfs(r,c):
            
            if (r not in range(ROWS) or
                c not in range(COLS) or
                grid2[r][c] == 0 or
                (r,c) in visit):
                
                return True
            
            visit.add((r,c))
            tmp = True
            if grid1[r][c] == 0:
                tmp = False
                
            tmp = dfs(r+1, c) and tmp
            tmp = dfs(r-1, c) and tmp
            tmp = dfs(r, c+1) and tmp
            tmp = dfs(r, c-1) and tmp
            
            return tmp
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r,c) not in visit and dfs(r,c):
                    res += 1
                    
        return res
