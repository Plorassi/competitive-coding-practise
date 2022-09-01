class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:

        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = collections.deque()


        def addRooms(self, r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r,c) in visit or
                rooms[r][c] == -1):
                return 

            visit.add((r,c))
            q.append([r,c])

        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    q.append([i,j])
                    visit.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rooms[r][c] = dist
                addRooms(r+1,c)
                addRooms(r,c+1)
                addRooms(r-1,c)
                addRooms(r,c-1)

            dist += 1
        

