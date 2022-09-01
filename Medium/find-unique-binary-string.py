class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums)
        
        def dfs(s):
            
            if len(s) == n:
                if s in nums:
                    return 2
                return s
            
            l = dfs(s+"0")
            
            if l == 2:
                return dfs(s+"1")
            
            return l
        
        return dfs("")
