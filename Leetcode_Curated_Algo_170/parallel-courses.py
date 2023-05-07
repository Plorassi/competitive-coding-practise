class Solution:
    def minimumSemesters(self, N, relations):
        """
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """
        n = N        
        self.d = collections.defaultdict(list)
        self.visited = [0 for _ in range(n + 1)]
        self.depth = [1 for _ in range(n + 1)]
        for x, y in relations:
            self.d[y].append(x)
        for i in range(1, n + 1):
            if not self.dfs(i):
                return -1
        return max(self.depth)

    def dfs(self, i):
        if self.visited[i] == 1:
            return False
        if self.visited[i] == 2:
            return True
        self.visited[i] = 1
        for j in self.d[i]:
            if not self.dfs(j):
                return False
            self.depth[i] = max(self.depth[i], self.depth[j] + 1)
        self.visited[i] = 2
        return True
