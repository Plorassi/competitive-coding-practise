# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        res = [0]
        def dfs(node):
            if not node:
                return 0
            
            if low <= node.val and node.val <= high:
                res[0] += node.val
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
                    
            elif node.val < low:
                if node.right:
                    dfs(node.right)
                    
            else:
                if node.left:
                    dfs(node.left)
                    
        dfs(root)
        return res[0]
