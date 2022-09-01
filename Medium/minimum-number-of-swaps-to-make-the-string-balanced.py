class Solution:
    def minSwaps(self, s: str) -> int:
        
        close = 0
        res = 0
        
        for c in s:
            if c == ']':
                close += 1
            else:
                close -= 1
            res = max(res, close)
            
        return (res+1)//2
