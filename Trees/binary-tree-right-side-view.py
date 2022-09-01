# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if not root:
            return res
        tmp = collections.deque([root])
            
        while tmp:
            res.append(tmp[-1].val)
            for i in range(len(tmp)):
                x = tmp.popleft()
                if x.left:
                    tmp.append(x.left)
                if x.right:
                    tmp.append(x.right)
                    
        return res
