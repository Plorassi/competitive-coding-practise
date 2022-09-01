class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        c = len(grid[0])
        r = len(grid)
        
        aux = [[0 for i in range(c)] for j in range(r)]
        
        aux[0][0] = grid[0][0]
        
        for i in range(1,r):
            aux[i][0] = grid[i][0] +  aux[i-1][0]       
            
        for i in range(1,c):
            aux[0][i] = grid[0][i] +  aux[0][i-1]
        
        for i in range(1,r):
            for j in range(1,c):
                aux[i][j] = grid[i][j] + min(aux[i-1][j], aux[i][j-1])

                
        return aux[-1][-1]
