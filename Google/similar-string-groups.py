class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] == -1:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        elif self.rank[px] >= self.rank[py]:
            self.parent[py] = px
            self.rank[px] += 1
        else:
            self.parent[px] = py
            self.rank[py] += 1

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if self.check(strs[i], strs[j]):
                    uf.union(i, j)
        for p in uf.parent:
            if p == -1:
                count += 1
        return count

    def check(self, str1, str2):
        count = 0
        for a,b in zip(str1, str2):
            if a != b:
                count += 1
                if count > 2:
                    return False
        return True
