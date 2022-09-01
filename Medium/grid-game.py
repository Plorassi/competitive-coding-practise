class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        N = len(grid[0])
        grid1, grid2 = grid[0].copy(), grid[1].copy()
        
        for i in range(1,N):
            grid1[i] += grid1[i-1]
            grid2[i] += grid2[i-1]
            
        res = float('inf')
        
        for i in range(N):
            x = grid1[-1] - grid1[i]
            y = grid2[i-1] if i > 0 else 0
            z = max(x,y)
            res = min(res, z)
            
        return res
        
            
