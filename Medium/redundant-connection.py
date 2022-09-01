class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)
        
        def find(node):
            p = parent[node]
            
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        
        def union(node1, node2):
            
            p1, p2 = find(node1), find(node2)
            
            if p1==p2:
                return False
            
            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
                
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
                
            return True
        
        for v1,v2 in edges:
            if not union(v1,v2):
                return [v1,v2]
            
        
        
