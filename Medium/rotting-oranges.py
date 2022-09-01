class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()
        fresh = 0
        dist = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1
                   
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
                
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row = r+dr
                    col = c+dc
                    if (row not in range(ROWS) or
                        col not in range(COLS) or
                        (row,col) in visit or
                        grid[row][col] == 0):
                        continue
                        
                    visit.add((row,col))
                    q.append([row,col])
                    fresh -= 1
                    
            dist += 1
            
        return dist if fresh == 0 else -1
