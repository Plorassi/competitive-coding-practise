class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        
        mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        lenght = len(digits)
        
        def backtrack(i, currStr):
            if len(currStr) == lenght:
                result.append(currStr)
                return
            
            for c in mapping[digits[i]]:
                backtrack(i+1, currStr+c)
                
                
        if digits:
            backtrack(0,'')
            
        return result
        

        
            
