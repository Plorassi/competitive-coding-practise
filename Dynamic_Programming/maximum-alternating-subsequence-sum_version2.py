class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        sumEven, sumOdd = 0, 0
        
        for i in range(len(nums))[::-1]:
            tmpEven = max(sumOdd + nums[i], sumEven)
            tmpOdd = max(sumEven - nums[i], sumOdd)
            
            sumEven, sumOdd = tmpEven, tmpOdd
            
        return sumEven
        
        
