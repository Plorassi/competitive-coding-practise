class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        dp = {}
        
        def backtrack(n):
            
            if n%2 == 0:
                return []
            if n == 1:
                return [TreeNode()]
            if n in dp:
                return dp[n]
            
            res = []
            
            for l in range(n):
                r = n-l-1
                lefttrees = backtrack(l)
                righttrees = backtrack(r)
                
                
                for left in lefttrees:
                    for right in righttrees:
                        res.append(TreeNode(0,left,right))
                        
            dp[n] = res
            return res
        
        return backtrack(n)
            
        
        
        
