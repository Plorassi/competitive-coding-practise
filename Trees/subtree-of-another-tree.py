# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSameTree(root.left, subRoot) or self.isSameTree(root.right, subRoot)
        
        
        
    def isSameTree(self, node1, node2):
            
        if not node1 or not node2:
            return not node1 and not node2
            
        if node1.val != node2.val:
            return False
            
        return self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)
