class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties.sort(key = lambda x: (-x[0],x[1]))
        
        res = 0
        cm = 0
        
        for a,d in properties:
            if d<cm:
                res += 1
            else:
                cm = d
                
        return res
            
