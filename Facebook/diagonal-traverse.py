class Solution:
	def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
		levels = defaultdict(list)
		max_level = len(mat) + len(mat[0]) - 2

		for i in range(len(mat)):
			for j in range(len(mat[0])):
				levels[i+j].append(mat[i][j])

		res = []

		for key in sorted(levels.keys()):
			if key % 2 == 0:
				levels[key].reverse()

			res.extend(levels[key])

		return res
