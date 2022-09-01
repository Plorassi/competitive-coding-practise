class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        temp = [(sqrt(points[i][0]**2 + points[i][1]**2), i) for i in range(len(points))]
        heapq.heapify(temp)
        res = []
        
        for i in range(k):
            weight, index = heapq.heappop(temp)
            res.append(points[index])
            
        return res
