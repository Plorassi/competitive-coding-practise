class Node:
    def __init__(self, start, end) -> None:        
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class NumArray:

    def __init__(self, nums: List[int]):

        def buildTree(nums, l, r):
            if l > r:
                return None

            if l == r:
                n = Node(l,r)
                n.total = nums[l]
                return n

            m = (l+r)//2
            root = Node(l,r)
            root.left = buildTree(nums,l,m)
            root.right = buildTree(nums,m+1,r)
            root.total = root.left.total + root.right.total

            return root

        self.root = buildTree(nums,0,len(nums)-1)
        

    def update(self, index: int, val: int) -> None:

        def updateNode(root, index, val):
            if root.start == root.end:
                root.total = val
                return root.total

            m = (root.start+root.end)//2

            if index <= m:
                updateNode(root.left, index, val)

            else:
                updateNode(root.right, index, val)

            root.total = root.left.total + root.right.total

            return root.total

        return updateNode(self.root, index, val)
            
        

    def sumRange(self, left: int, right: int) -> int:
        
        def rangeSum(root, l, r):
            if root.start == l and root.end == r:
                return root.total

            m = (root.start+root.end)//2

            if right <= m:
                return rangeSum(root.left, l, r)

            elif left >= m+1:
                return rangeSum(root.right, l, r)

            else:
                return rangeSum(root.left, l, m) + rangeSum(root.right, m+1, r)

        return rangeSum(self.root, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
