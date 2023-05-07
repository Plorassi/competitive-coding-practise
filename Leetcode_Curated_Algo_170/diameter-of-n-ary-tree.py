"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        res = [0]

        def dfs(node):
            if not node:
                return 0
            distance = -1
            top1, top2 = 0, 0
            for child in node.children:
                distance = 1+dfs(child)
                if distance > top1:
                    top1, top2 = distance, top1
                elif distance > top2:
                    top2 = distance
                res[0] = max(res[0], top1+top2)
            return top1

        dfs(root)
        return res[0]
