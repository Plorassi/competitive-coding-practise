class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        visit = set()
        q = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    heapq.heappush(q,(0,i,j))

        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while q:
            dis, r, c = heapq.heappop(q)
            if (r,c) not in visit:
                visit.add((r,c))
                rooms[r][c] = dis
                for dr,dc in directions:
                    row, col = r+dr, c+dc
                    if row < 0 or row >= len(rooms) or col < 0 or col >= len(rooms[0]) or (row,col) in visit or rooms[row][col] == -1:
                        continue
                    heapq.heappush(q,(dis+1,row,col))

