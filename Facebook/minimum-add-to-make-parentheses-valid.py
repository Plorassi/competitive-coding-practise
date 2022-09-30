class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        res = 0
        
        for c in s:
            if c == ')':
                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        res += 1
                        stack.pop()
                else:
                    res += 1
                
            else:
                stack.append(c)
                
        return len(stack)+res
