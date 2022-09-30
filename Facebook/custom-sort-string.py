class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        tmp = Counter(s)
        res = ''
        for c in order:
            if c in tmp:
                res += c*tmp[c]
                tmp[c] = 0
        for key in tmp:
            if tmp[key] > 0:
                res += key*tmp[key]
                
        return res
            
        
