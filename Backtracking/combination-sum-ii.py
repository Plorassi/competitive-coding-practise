class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, path, ret):
            if target < 0:
                return 
            if target == 0:
                ret.append(path)
                return 
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    dfs(nums[i+1:], target-nums[i], path+[nums[i]], ret)        

        ret = []
        candidates.sort()
        dfs(candidates, target, [], ret)
        return ret
