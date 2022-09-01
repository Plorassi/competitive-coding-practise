class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        ans = r
        
        def timeTaken(s):
            res = 0
            for i in range(len(piles)):
                res += (math.ceil(piles[i]/s))
            return res
        
        while l<=r:
            m = (l+r)//2
            if timeTaken(m) <= h:
                ans = min(ans, m)
                r = m-1
            else:
                l = m+1
                
        return ans
