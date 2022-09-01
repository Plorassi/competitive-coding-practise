class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        l1 = len(s1)
        l2 = len(s2)
        
        dp = {}
        
        def dfs(i,j):
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i == l1 and j == l2:
                return True
            
            if i < l1 and s1[i] == s3[i+j] and dfs(i+1,j):
                return True
            
            if j < l2 and s2[j] == s3[i+j] and dfs(i,j+1):
                return True
            
            dp[(i,j)] = False
            
            return False
        
        if len(s3) != (l1+l2):
            return False
        return dfs(0,0)
