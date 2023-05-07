# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:

        res = [0]

        def dfs(node):

            if not node:
                return [0,0]

            sL, cL = dfs(node.left)
            sR, cR = dfs(node.right)

            res[0] = max(res[0], (sL+node.val+sR)/(cL+1+cR))

            return [sL+node.val+sR, cL+1+cR]

        dfs(root)
        return res[0]
