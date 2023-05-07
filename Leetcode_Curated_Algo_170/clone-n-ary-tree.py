"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':

        def deepCopy(node):
            if not node:
                return None
            newNode = Node(node.val)
            for child in node.children:
                newNode.children.append(deepCopy(child))
            return newNode


        return deepCopy(root)
