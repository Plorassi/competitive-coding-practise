# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = [0]
        ans = [0]
        
        def dfs(node):
            
            if not node or res[0] > k:
                return
            
            dfs(node.left)
            
            res[0] += 1
            
            if res[0] == k:
                ans[0] = node.val
                return 
            
            dfs(node.right)
            
            return
        
        dfs(root)
        
        return ans[0]
