class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_temp(nums_temp):
        
            dp = {}
        
            def dfs(i):
            
                if i in dp:
                    return dp[i]
            
                if i == len(nums_temp) - 1:
                    return nums_temp[-1]
            
                if i >= len(nums_temp):
                    return 0
            
                dp[i] = max(nums_temp[i] + dfs(i+2), dfs(i+1))
            
                return dp[i]
        
            return dfs(0)
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(rob_temp(nums[1:]), rob_temp(nums[:-1]))
