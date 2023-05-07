# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def str2tree(self, s: str) -> TreeNode:
        if not s or len(s) == 0:
            return None
        
        root, _ = self.helper(s,0)
        return root
    
    def helper(self, s, i):
        start = i
        while i<len(s) and (s[i] == '-' or s[i].isdigit()):
            i += 1
        node = TreeNode(int(s[start:i]))
        if i<len(s) and s[i] == '(':
            i += 1
            node.left, i = self.helper(s,i)
            i += 1
        if i<len(s) and s[i] == '(':
            i += 1
            node.right, i = self.helper(s,i)
            i += 1
        return node, i 
