class TreeNode:
	# p1 is the upper-left point in sub-matrix, represented by this node
	# p2 is the down-right point in the sub-matrix
    def __init__(self, p1, p2):
        self.r1, self.c1 = p1
        self.r2, self.c2 = p2
		# self.val is the sum of the sub-matrix
        self.val = 0
		# pointers to its 4 children
        self.ul = None
        self.ur = None
        self.dl = None
        self.dr = None

class SegmentTree:
    def __init__(self, r, c, matrix):
        self.root = self.build(0, 0, r-1, c-1, matrix)
        self.matrix = matrix
        
    def build(self, r1, c1, r2, c2, matrix):
        if r1 == r2 and c1 == c2:
            node = TreeNode((r1, c1), (r2, c2))
            node.val = matrix[r1][c1]
            return node
        
        elif r1 > r2 or c1 > c2:
			# handle the null area case, I talked in the paragraph
            node = TreeNode((r1, c1), (r2, c2))
            node.val = 0
            return node
        
        mr = (r1 + r2) // 2
        mc = (c1 + c2) // 2
        node = TreeNode((r1, c1), (r2, c2))
        
        node.ul = self.build(r1, c1, mr, mc, matrix)
        node.ur = self.build(r1, mc+1, mr, c2, matrix)
        node.dl = self.build(mr+1, c1, r2, mc, matrix)
        node.dr = self.build(mr+1, mc+1, r2, c2, matrix)
        
        node.val = node.ul.val + node.ur.val + node.dl.val + node.dr.val
        
        return node
    
    def update(self, node, r, c, val):
        if node.r1 == node.r2 == r and node.c1 == node.c2 == c:
            node.val = val
            return
        
        if r > node.r2 or c > node.c2 or r < node.r1 or c < node.c1:
            return
        
        self.update(node.ul, r, c, val)
        self.update(node.ur, r, c, val)
        self.update(node.dl, r, c, val)
        self.update(node.dr, r, c, val)
        
        node.val = node.ur.val + node.ul.val + node.dl.val + node.dr.val
        
        return
    
    def query(self, node, qr1, qc1, qr2, qc2):
        if qr2 < node.r1 or qr1 > node.r2 or qc1 > node.c2 or qc2 < node.c1 or node.r1 > node.r2 or node.c1 > node.c2:
            return 0
        
        if qr1 <= node.r1 and qc1 <= node.c1 and qr2 >= node.r2 and qc2 >= node.c2:
            return node.val
        
        a = self.query(node.ul, qr1, qc1, qr2, qc2)
        b = self.query(node.ur, qr1, qc1, qr2, qc2)
        c = self.query(node.dl, qr1, qc1, qr2, qc2)
        d = self.query(node.dr, qr1, qc1, qr2, qc2)
        
        return a + b + c + d
        
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        self.tree = SegmentTree(len(matrix), len(matrix[0]), matrix)
        self.root = self.tree.root
        

    def update(self, row: int, col: int, val: int) -> None:
        self.tree.update(self.root, row, col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.tree.query(self.root, row1, col1, row2, col2)
