# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
                
        res = [0]

        def backtrack(node):

            if not node:
                return [0,0]

            incr, dcr = 1, 1
            if node.left:
                l = backtrack(node.left)
                if node.val == node.left.val + 1:
                    dcr = l[1]+1
                elif node.val + 1 == node.left.val:
                    incr = l[0]+1

            if node.right:
                r = backtrack(node.right)
                if node.val == node.right.val + 1:
                    dcr = max(r[1]+1,dcr)
                elif node.val + 1 == node.right.val:
                    incr = max(r[0]+1,incr)

            res[0] = max(res[0], dcr+incr-1)
            return [incr,dcr]

        backtrack(root)
        return res[0]
                
