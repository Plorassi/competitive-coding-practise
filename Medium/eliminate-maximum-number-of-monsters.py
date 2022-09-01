class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        minHeap = [(math.ceil(dist[i]/speed[i]), dist[i]) for i in range(len(dist))]
        heapq.heapify(minHeap)
        
        res = 0
        t = 0
        
        while minHeap:
            
            time, distance = heapq.heappop(minHeap)
            if time <= t:
                return res
            
            t += 1
            res += 1
            
        return res
