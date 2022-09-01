class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def timeTaken(p, s):
            res = 0
            for i in range(len(p)):
                res += math.ceil(p[i]/s)
            return res
        
        l,r = 1, max(piles)
        ans = r
        
        while l<=r:
            m = (l+r)//2
            if timeTaken(piles, m) <= h:
                ans = min(ans, m)
                r = m-1
            else:
                l = m+1
                
        return ans    
