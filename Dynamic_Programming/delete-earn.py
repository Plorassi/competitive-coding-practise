class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        
        nums = list(set(nums))
        
        nums.sort()
        
        dp = {0:count[nums[0]]*nums[0]}
        
        for i in range(1,len(nums)):
            
            dp[i] = count[nums[i]]*nums[i]
            
            if nums[i-1]+1 == nums[i]:
                dp[i] = max(dp[i]+dp.get(i-2,0), dp.get(i-1,0)) 
            else:
                dp[i] = dp[i]+dp.get(i-1,0) 
                
        return dp[len(nums)-1]
