class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            parent[find(b)] = find(a)
            return


        for x,y in edges:
            union(x,y)
        
        for i in range(n):
            parent[i] = find(i)

        return len(set(parent))

