# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = [0]
        
        def dfs(node):
            
            ll, rl = 0, 0
            if node.left:
                ll = 1 + dfs(node.left)
            if node.right:
                rl = 1 + dfs(node.right)
            res[0] = max(res[0], ll+rl)
            return max(ll, rl)
        
        dfs(root)
        return res[0]
