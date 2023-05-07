class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        q = [(-grid[0][0], 0, 0)]
        ROWS, COLS = len(grid), len(grid[0])
        seen = set((0,0))
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        res = grid[0][0]

        while q:
            dis, r, c = heapq.heappop(q)
            res = min(grid[r][c], res)
            if r == ROWS-1 and c == COLS-1:
                return res
            for dr, dc in directions:
                row, col = r+dr, c+dc
                if (row,col) not in seen and 0<=row<ROWS and 0<=col<COLS:
                    heapq.heappush(q,(-grid[row][col], row, col))
                    seen.add((row,col))



             
