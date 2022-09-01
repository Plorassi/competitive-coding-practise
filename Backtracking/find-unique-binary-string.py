class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums)
        
        def dfs(x):
            if len(x) == n:
                if x in nums:
                    return 2
                return x
            
            l = dfs(x+"0")
            
            if l == 2:
                return dfs(x+"1")
            return l
            
        return dfs("")
