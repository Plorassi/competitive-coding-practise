class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = []
        
        def backtrack(i, substr):
            
            if len(substr) == len(s):
                res.append(substr)
                return
            
            backtrack(i+1,substr + s[i])
            if s[i].isalpha():
                backtrack(i+1, substr + s[i].swapcase())
            
        
        
        backtrack(0,"")
        return res
            
        
