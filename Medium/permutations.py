class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def dfs(left, path):
            if not left:
                res.append(path)
                return
            
            for i in range(len(left)):
                x = left[:i] + left[i+1:]
                dfs(x, path + [left[i]])
                
            return
                
        dfs(nums,[])
        return res
