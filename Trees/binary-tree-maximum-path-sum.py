# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = [root.val]
        
        def get_max(root):
            
            if not root:
                return 0
            
            leftGain = max(get_max(root.left),0)
            rightGain = max(get_max(root.right),0)
            
            res[0] = max(res[0], leftGain+root.val+rightGain)
            
            return root.val + max(leftGain,rightGain)
        
        get_max(root)
        return res[0]
        
