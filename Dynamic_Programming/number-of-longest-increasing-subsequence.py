class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]
        dp_res = [1 for i in range(n)]
        res = 0
        
        for i in range(n-1)[::-1]:
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    if 1+dp[j] > dp[i]:
                        dp[i] = 1+dp[j]
                        dp_res[i] = dp_res[j]
                    elif 1+dp[j] == dp[i]:
                        dp_res[i] += dp_res[j]
                    
        x = max(dp)
        for i in range(n):
            if x == dp[i]:
                res += dp_res[i]
                
        return res
