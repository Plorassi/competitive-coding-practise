class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        n = len(height)
        l,r = 0, n-1
        lmax,rmax = height[l],height[r]
        res = 0
        
        while l<r:
            if lmax <rmax:
                l += 1
                lmax = max(height[l],lmax)
                res += lmax-height[l]
            else:
                r -= 1
                rmax = max(height[r],rmax)
                res += rmax-height[r]
                
        return res
