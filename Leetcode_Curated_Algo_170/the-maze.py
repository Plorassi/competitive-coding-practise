class Solution:
    def hasPath(self, maze, start, destination):

            Q = collections.deque()
            Q.append(start)
            n = len(maze)
            m = len(maze[0])
            visit = set()
            dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
            visit.add((start[0], start[1]))
            
            while Q:
                i, j = Q.popleft()

                if i == destination[0] and j == destination[1]:
                    return True
                
                for x, y in dirs:
                    row = i
                    col = j
                    while 0 <= row+x < n and 0 <= col+y < m and maze[row+x][col+y] == 0:
                        row += x
                        col += y
                    if maze[row][col] == 0 and (row,col) not in visit:
                        Q.append([row, col])
                        visit.add((row,col))
            
            return False

