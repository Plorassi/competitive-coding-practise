class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        tmp = collections.defaultdict(int)
        
        for n in nums:
            tmp[n] += 1
            
        for key,value in tmp.items():
            heapq.heappush(heap, (-value, key))
            
        res = []
        while heap and k > 0:
            x,y = heapq.heappop(heap)
            k -= 1
            res.append(y)
            
        return res
    
        
