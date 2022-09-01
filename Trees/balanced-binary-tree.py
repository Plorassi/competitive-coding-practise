# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        res = 0
        
        def dfs(node):
            
            nonlocal res
            
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            
            if abs(l-r) > 1:
                res = 1
            
            return 1 + max(l,r)
        
        if not root:
            return True
        
        dfs(root)
        
        return True if not res else False
