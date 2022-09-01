class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        
        mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        l = len(digits)
        
        def dfs(i,currStr):
            if len(currStr) == l:
                result.append(currStr)
                return
            
            for c in mapping[digits[i]]:
                dfs(i+1,currStr+c)
                
        if digits:
            dfs(0,"")
            
        return result

        
            
