class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        find = Counter(p)
        m,n = len(s),len(p)
        i = 0
        res = []
        
        while i < m-n+1:
            tmp = Counter(s[i:i+n])
            if tmp == find:
                res.append(i)
            i += 1
            
        return res
