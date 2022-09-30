class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        m = len(matrix[0])
        n = len(matrix)
        
        for i in range(n - 1):
            if matrix[i][:m - 1] != matrix[i + 1][1:]:
                return False
        return True
