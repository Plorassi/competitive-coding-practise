class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        res = ''
        stack = []
        remove = set()
        
        for i,c in enumerate(s):
            if c == '(':
                stack.append(['(',i])
            elif c == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    remove.add(i)
                    
        for ele in stack:
            remove.add(ele[1])
            
        for i,c in enumerate(s):
            if i not in remove:
                res += c
                
        return res
                    
                
