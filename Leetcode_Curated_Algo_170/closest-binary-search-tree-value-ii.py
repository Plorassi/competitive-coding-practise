# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:

        heap = []

        def dfs(node):
            if not node:
                return

            heapq.heappush(heap, (abs(target-node.val), node.val))
            dfs(node.left)
            dfs(node.right)

        res = []
        dfs(root)
        while k > 0:
            x,val = heapq.heappop(heap)
            res.append(val)
            k -= 1

        return res
