# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        hmap = collections.defaultdict(list)
        
        def dfs(node):
            if not node:
                return -1
            l,r = dfs(node.left), dfs(node.right)
            hmap[1+max(l,r)].append(node.val)
            return 1+max(l,r)

        dfs(root)
        return hmap.values()
        
        
