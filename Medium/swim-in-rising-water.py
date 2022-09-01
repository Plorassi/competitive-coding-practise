class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        visit = set()
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        minHeap = [[grid[0][0], 0, 0]]
        
        while minHeap:
            
            t, r, c = heapq.heappop(minHeap)
            
            if r == N-1 and c == N-1:
                return t
            
            for dr,dc in directions:
                
                r,c = r+dr, c+dc
                if (r not in range(N) or
                    c not in range(N) or
                    (r,c) in visit):
                    continue
                    
                visit.add((r,c))
                heapq.heappush(minHeap, (max(t, grid[r][c]), r, c))
                
        
                
            
        
        
        
