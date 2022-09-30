# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        res = []
        
        def dfs(node, cur):
            
            if not node:
                return ""
            
            tmp = cur + str(node.val)
            
            if not node.left and not node.right:
                res.append(int(tmp))
                return
            
            dfs(node.left, tmp)
            dfs(node.right, tmp)
            
        dfs(root, "")
        return sum(res)
            
            
            
            
                
