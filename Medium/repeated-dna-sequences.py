class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        visit = set()
        l,r = 0, 10
        res = set()
        n = len(s)
        
        if n <= 10:
            return res
        
        while r <= n:
            if s[l:r] not in visit:
                visit.add(s[l:r])
            else:
                res.add(s[l:r])            
            l += 1
            r += 1
        
        return list(res)
