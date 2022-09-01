class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        edges = {(a,b) for a,b in connections}
        neighbours = collections.defaultdict(list)
        
        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)
            
        visit = set()
        res = 0
        
        def dfs(city):
            
            nonlocal res 
            for neighbor in neighbours[city]:
                if neighbor in visit:
                    continue
                if (neighbor, city) not in edges:
                    res += 1
                visit.add(neighbor)
                dfs(neighbor)
            
        
        visit.add(0)
        dfs(0)
        return res        
            
        
