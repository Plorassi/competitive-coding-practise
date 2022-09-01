class Solution:
    def minDistance(self, word1, word2):
        
        dp = {}
        
        def backtrack(w1, w2, i, j):
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if i == len(w1) and j == len(w2):
                return 0
            
            if i == len(w1):
                return len(w2) - j
            
            if j == len(w2):
                return len(w1) - i
            
            if w1[i] == w2[j]:
                ans = backtrack(w1,w2,i+1,j+1)
            else:
                insert = 1+backtrack(w1,w2,i,j+1)
                delete = 1+backtrack(w1,w2,i+1,j)
                replace = 1+backtrack(w1,w2,i+1,j+1)
                ans = min(insert,delete,replace)
                
            dp[(i,j)] = ans
            
            return dp[(i,j)]
            
            
        return backtrack(word1, word2, 0, 0)
            


        
