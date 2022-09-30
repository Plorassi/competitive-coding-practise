class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
	    if not root: return []

	# Set containers:
	# a) queue for traversal.
	# b) map to keep track of cols.
	    queue = deque([(root, 0)])
	    cols = defaultdict(list)
	    minCol, maxCol = 0, 0

	# Perform BFS
	    while queue:
		    node, col = queue.popleft()

		# Perform pre-order traversal
		    if node:
			    cols[col].append(node.val)
			    queue.append((node.left, col-1))
			    queue.append((node.right, col+1))

			# Set current column range:
			    minCol = min(minCol, col)
			    maxCol = max(maxCol, col)

	    return [cols[col] for col in range(minCol, maxCol+1)]
