class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()
        dist = -1
        count = 0
        
        def spread(r,c):
            if(r<0 or c<0 or
               r==ROWS or c==COLS or
               (r,c) in visit or grid[r][c] == 0):
                return
            
            visit.add((r,c))
            q.append([r,c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
                if grid[r][c] == 0:
                    count += 1
                    
        if count == ROWS*COLS:
            return 0
        
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                spread(r+1,c)
                spread(r,c+1)
                spread(r-1,c)
                spread(r,c-1)
            dist += 1
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    return -1
        
        return dist      
