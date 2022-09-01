class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(S, o, c):
            
            if len(S) == 2*n:
                res.append("".join(S))
                return
            
            if o < n:
                S.append("(")
                backtrack(S, o+1, c)
                S.pop()
                
            if c < o:
                S.append(")")
                backtrack(S, o, c+1)
                S.pop()
                
        backtrack([],0,0)
        return res
