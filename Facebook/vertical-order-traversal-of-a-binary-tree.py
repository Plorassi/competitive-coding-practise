# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        hmap = collections.defaultdict(list)
        def dfs(node,r,c):
            if not node:
                return
            hmap[(r,c)].append(node.val)
            hmap[(r,c)].sort()
            dfs(node.left, r+1, c-1)
            dfs(node.right, r+1, c+1)
            
        dfs(root, 0, 0)
        keys = sorted(list(hmap.keys()), key=lambda x: (x[1], x[0]))
        res = collections.defaultdict(list)
        
        for k in keys:
            pos, depth = k
            res[depth].extend(hmap[(pos,depth)])
            
        return res.values()
