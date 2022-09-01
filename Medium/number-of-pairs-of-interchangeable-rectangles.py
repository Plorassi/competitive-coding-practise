class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        pairs = {}
        
        for w,h in rectangles:
            pairs[w/h] = 1 + pairs.get(w/h,0)
            
        res = 0
        for x in pairs:
            res += math.comb(pairs[x],2)
            
        return res
