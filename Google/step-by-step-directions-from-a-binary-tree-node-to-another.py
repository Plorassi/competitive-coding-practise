# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def lca(node):
            
            if not node:
                return None
            
            if node.val == startValue or node.val == destValue:
                return node
            
            l,r = lca(node.left), lca(node.right)
            
            if l and r:
                return node
            elif l:
                return l
            else:
                return r
            
        root = lca(root)
        stack = [[root,'']]
        ps,pd = '', ''
        while stack:
            node, path = stack.pop()
            if node.val == startValue: 
                ps = path
            if node.val == destValue: 
                pd = path
            if node.left:
                stack.append([node.left,path+'L'])
            if node.right:
                stack.append([node.right,path+'R'])
            
        return 'U'*len(ps)+pd
                
            
            
            
        
            
            
            
            
