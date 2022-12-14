class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(nums, path, res):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            
            
        res = []
        nums.sort()
        dfs(nums,[],res)
        return res
