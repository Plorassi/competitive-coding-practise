class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

            Q = []
            heapq.heappush(Q,(0,start[0],start[1]))
            n = len(maze)
            m = len(maze[0])
            visit = {(start[0],start[1]):0}
            dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
            
            
            while Q:
                dis, i, j = heapq.heappop(Q)

                if i == destination[0] and j == destination[1]:
                    return dis
                
                for x, y in dirs:
                    row = i
                    col = j
                    newDis = dis
                    while 0 <= row+x < n and 0 <= col+y < m and maze[row+x][col+y] == 0:
                        row += x
                        col += y
                        newDis += 1        

                    if (row,col) not in visit or newDis < visit[(row,col)]:
                        heapq.heappush(Q,(newDis,row,col))
                        visit[(row,col)] = newDis
            
            return -1
