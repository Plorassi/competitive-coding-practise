# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def preorder(node):
            
            if not node:
                return None
            
            leftTail = preorder(node.left)
            rightTail = preorder(node.right)
            
            if node.left:
                leftTail.right = node.right
                node.right = node.left
                node.left = None
                
            return rightTail or leftTail or node
        
        preorder(root)
                
            
