class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        res = {}
        
        for row in wall:
            cur = 0
            for value in row:
                cur += value
                res[cur] = 1 + res.get(cur, 0)
                
            
        res[sum(wall[0])] = 0
        
        return len(wall) - max(res.values())
