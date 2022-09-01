class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l,r = 0, len(matrix)-1
        start = 0
        
        while l<=r:
            m = (l+r)//2
            if matrix[m][0] <= target:
                start = max(start, m)
                l = m+1
            else:
                r = m-1
                
        l,r = 0,len(matrix[0])-1
        res = False
        
        while l<=r:
            m = (l+r)//2
            if matrix[start][m] < target:
                l = m+1
            elif matrix[start][m] > target:
                r = m-1
            else:
                res = True
                break
                
        return res            
