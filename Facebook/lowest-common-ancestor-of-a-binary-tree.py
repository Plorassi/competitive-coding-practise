# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node:
                return None
            
            if node == p or node == q:
                return node
            
            x  = dfs(node.left)
            y = dfs(node.right)
            
            if x and y:
                return node
            elif x and not y:
                return x
            else:
                return y
                
        
        return dfs(root)
            
        
