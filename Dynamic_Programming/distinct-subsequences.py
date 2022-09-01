class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = {}
        
        
        def backtrack(s,t,i,j):
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            dp[(i,j)] = 0
            
            if s[i] == t[j]:
                dp[(i,j)] = backtrack(s,t,i+1,j+1) + backtrack(s,t,i+1,j)
            else:
                dp[(i,j)] = backtrack(s,t,i+1,j)
                
            return dp[(i,j)]
        
        return backtrack(s,t,0,0)
                
                
                
            
            
        
