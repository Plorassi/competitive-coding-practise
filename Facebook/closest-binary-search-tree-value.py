class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.diff, self.val = float('inf'), None
        def helper(root):
            if not root: return 
            if self.diff > abs(target - root.val):
                self.diff = abs(target - root.val)
                self.val = root.val              
            if target < root.val:
                helper(root.left)
            else:
                helper(root.right)
        helper(root)
        return self.val
