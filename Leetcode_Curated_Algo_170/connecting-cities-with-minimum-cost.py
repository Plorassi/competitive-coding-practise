class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:

        self.groups = n
        self.ans = 0
        parent = {x: x for x in range(1,n+1)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            x,y = find(a), find(b)
            if x!=y:
                parent[y] = x
                return True
            return False

        for a,b,c in sorted(connections, key=lambda x: x[2]):
            if union(a,b):
                self.ans += c
                self.groups -= 1
                if self.groups == 1:
                    return self.ans 

        return -1
