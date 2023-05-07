# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        def isPresent(x,node):
            if not node:
                return False

            if node.val > x:
                return isPresent(x,node.left)

            elif node.val < x:
                return isPresent(x,node.right)

            else:
                return True


        def dfs(target, node):
            if not node:
                return False

            if isPresent(target-node.val, root2):
                return True

            return dfs(target, node.left) or dfs(target, node.right)

        return dfs(target, root1)
