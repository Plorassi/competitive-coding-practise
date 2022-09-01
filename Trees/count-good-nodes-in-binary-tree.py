# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        
        def dfs(node, prev):
            
            nonlocal res
            
            if not node:
                return
            
            if node.val >= prev:
                prev = max(prev, node.val)
                res += 1
                
            dfs(node.left, prev)
            dfs(node.right, prev)
            
            return
        
        dfs(root,float('-inf'))
        return res
