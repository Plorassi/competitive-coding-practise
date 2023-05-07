class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        hamp = collections.defaultdict(int)

        for j in range(len(mat[0])):
            for i in range(len(mat)):
                hamp[mat[i][j]] += 1
                if hamp[mat[i][j]] == len(mat):
                    return mat[i][j]

        return -1
