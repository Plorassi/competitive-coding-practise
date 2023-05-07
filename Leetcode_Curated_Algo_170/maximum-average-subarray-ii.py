class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        def isbigger(target):
            cur=0
            for i in range(k):
                cur+=nums[i]-target
            if cur>=0:
                return True
            prev=0
            prevmin=0
            for i in range(k,n):
                cur+=nums[i]-target
                prev+=nums[i-k]-target
                prevmin=min(prevmin,prev)
                if cur>=prevmin:
                    return True
            return False
        i,j=min(nums),max(nums)
        while j-i>=0.00001:
            mid=(i+j)/2.0
            if isbigger(mid):
                i=mid
            else:
                j=mid
        return i
