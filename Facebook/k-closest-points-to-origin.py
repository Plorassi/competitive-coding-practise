class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        
        for i,point in enumerate(points):
            heapq.heappush(minHeap, (point[0]**2+point[1]**2,i))
            
        res = []
        while minHeap and k:
            d,i = heapq.heappop(minHeap)
            res.append(points[i])
            k -= 1
            
        return res
        
