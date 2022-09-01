class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        nums = list(set(nums))
        dp = {0: nums[0]*count[nums[0]]}
        
        def dfs(p):
            
            if p in dp:
                return dp[p]
            
            if p < 0 :
                return 0
            
            dp[p] = count[nums[p]]*nums[p]
            
            if nums[p] == nums[p-1] + 1:
                dp[p] = max(dp[p] + dfs(p-2), dfs(p-1))
            else:
                dp[p] += dfs(p-1)
                
            return dp[p]
        
        return dfs(len(nums)-1)
