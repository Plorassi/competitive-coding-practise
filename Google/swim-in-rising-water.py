class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        ans = 0
        q = []
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        heapq.heappush(q,(grid[0][0], 0, 0))
        visit.add((0,0))
        while q:
            val, r, c = heapq.heappop(q)
            ans = max(ans, val)
            if r == ROWS-1 and c == COLS-1:
                return ans
            for dr,dc in directions:
                row, col = r+dr, c+dc
                if 0<=row<ROWS and 0<=col<COLS and (row,col) not in visit:
                    visit.add((row,col))
                    heapq.heappush(q,(grid[row][col],row,col))
                    
                    
