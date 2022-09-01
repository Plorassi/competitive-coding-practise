class Solution:
    def minDistance(self, word1, word2):
        
        dp = {}
        
        def dfs(s,p,i,j):
            
            if i == len(s) and j == len(p):
                return 0
            
            if i == len(s):
                return len(p) - j
            
            if j == len(p):
                return len(s) - i
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            
            if s[i] == p[j]:
                return dfs(s, p, i+1, j+1)
            
            insert = dfs(s, p, i, j+1)
            replace = dfs(s, p, i+1, j+1)
            delete = dfs(s, p, i+1, j)
            
            dp[(i,j)] = 1+min(insert,replace,delete)
            
            return dp[(i,j)]
        
        return dfs(word1,word2,0,0)
            


        
