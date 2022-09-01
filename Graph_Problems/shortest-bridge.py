class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        visit = set()
        
        def invalid(r,c):
            return r<0 or c<0 or r == N or c == N
        
        def dfs(r,c):
            if (invalid(r,c) or not grid[r][c] or (r,c) in visit):
                return 
            visit.add((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc)
                
        def bfs():
            res, q = 0, collections.deque(visit)
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dr,dc in directions:
                        row, col = r+dr, c+dc
                        if invalid(row,col) or (row,col) in visit:
                            continue
                        if grid[row][col]:
                            return res
                        q.append([row,col])
                        visit.add((row,col))
                res += 1
            
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()
