# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        res = [0]

        def dfs(node):
            if not node:
                return 0

            li,ri = 1,1
            l,r = dfs(node.left), dfs(node.right)
            
            if node.left:
                if node.left.val == node.val+1:
                    li = max(li,1+l)

            if node.right:
                if node.right.val == node.val+1:
                    ri = max(ri,1+r)

            res[0] = max(res[0], l,r,li,ri)

            return max(li,ri)

        dfs(root)
        return res[0]

        
            
        
