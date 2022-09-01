class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        l,r = 1, n
        
        while l<=r:
            
            mid = (l+r)//2
            
            if (mid*(mid+1))//2 > n:
                r = mid-1
            elif (mid*(mid+1))//2 < n:
                l = mid + 1
            else:
                return mid
                
        return min(l,r)
