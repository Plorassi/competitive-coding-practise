class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def isSubSeq(s, sub):
            i, j = 0, 0
            
            while i < len(s) and j < len(sub):
                
                if i in removed or s[i] != sub[j]:
                    i += 1
                    continue
                    
                else:
                    i += 1
                    j += 1
                    
            return j == len(sub)
        
        removed = set()
        res = 0
        l, r = 0, len(removable) - 1
        
        while l <= r:
            
            m = (l+r)//2
            removed = set(removable[:m+1])
            if isSubSeq(s, p):
                res = max(res, m+1)
                l = m+1
            else:
                r = m-1
                
        return res
