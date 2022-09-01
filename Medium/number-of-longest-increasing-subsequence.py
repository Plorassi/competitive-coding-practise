class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [1 for i in range(n)]
        dp_cnt = [1 for i in range(n)]
        
        for i in range(n-1)[::-1]:
            for j in range(i+1,n):
                
                if nums[j] > nums[i]:
                    if 1+dp[j] > dp[i]:
                        dp[i] = 1+dp[j]
                        dp_cnt[i] = dp_cnt[j]
                    elif 1+dp[j] == dp[i]:
                        dp_cnt[i] += dp_cnt[j]
                        
        ans = max(dp)
        res = 0
        for i in range(n):
            if dp[i] == ans:
                res += dp_cnt[i]
                
        return res
                        
