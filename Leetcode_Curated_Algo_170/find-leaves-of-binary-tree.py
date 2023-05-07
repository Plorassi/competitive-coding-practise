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
                return 0
            
            h = max(dfs(node.left), dfs(node.right)) + 1
            hmap[h].append(node.val)
            
            return h
        
        dfs(root)
        return hmap.values()
            
