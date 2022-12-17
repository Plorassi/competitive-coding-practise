class Solution:
    def earliestAcq(self, logs, N):
        uf = {x: x for x in range(N)}
        self.groups = N

        def merge(x, y):
            x, y = find(x), find(y)
            if x != y:
                self.groups -= 1
                uf[x] = y

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        for t, x, y in sorted(logs):
            merge(x, y)
            if self.groups == 1:
                return t
        return -1
