class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        diff = []
        for ca, cb in costs:
            diff.append([cb-ca, ca, cb])
            
        diff.sort()
        l = len(costs)
        res = 0
        
        for i in range(l//2):
            res += diff[i][2]
            
        for i in range(l//2,l):
            res += diff[i][1]
            
        return res
