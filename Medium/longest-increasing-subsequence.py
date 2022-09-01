class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        l = len(nums)
        dp = [1 for i in range(l)]
        
        for i in range(l-1)[::-1]:
            
            for j in range(i+1, l):
                
                if nums[i] < nums[j]:
                    
                    dp[i] = max(dp[i], 1+dp[j])
                    
        return max(dp)
