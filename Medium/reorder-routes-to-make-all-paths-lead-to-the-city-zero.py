class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        edges = {(a,b) for a,b in connections}
        adj = collections.defaultdict(list)
        
        for s,e in connections:
            adj[s].append(e)
            adj[e].append(s)
            
        visit = set()
        res = 0
        
        def dfs(city):
            
            nonlocal res
            for nei in adj[city]:
                if nei in visit:
                    continue
                if (nei, city) not in edges:
                    res += 1
                visit.add(nei)
                dfs(nei)
            
            
        
        visit.add(0)
        dfs(0)
        return res
