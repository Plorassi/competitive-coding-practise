class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        part = []
        
        def isPali(num, l, r):
            while l<r:
                if num[l] != num[r]:
                    return False
                l,r = l+1,r-1
            return True
        
        def backtrack(i):
            if i>=len(s):
                res.append(part.copy())
                return 
            
            for j in range(i,len(s)):
                if isPali(s, i, j):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
                    
        backtrack(0)
        return res
                    
