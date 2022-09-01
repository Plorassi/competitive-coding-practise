class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        x,y = len(s1), len(s2)
        find = Counter(s1)
        
        l,r = 0,x
        while l < y-x+1:
            tmp = Counter(s2[l:r])
            if tmp == find:
                return True
            l += 1
            r += 1
            
        return False
            
        
            
        
        
