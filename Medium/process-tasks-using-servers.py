class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        res = []
        avaliable = [(servers[i], i) for i in range(len(servers))] 
        heapq.heapify(avaliable)
        unavail = []
        t = 0
        
        for i in range(len(tasks)):
            t = max(t, i)
            
            if len(avaliable) == 0:
                t = unavail[0][0]
            while unavail and t >= unavail[0][0]:
                freeTime, weight, index = heapq.heappop(unavail)
                heapq.heappush(avaliable, (weight, index))
                
            weight, index = heapq.heappop(avaliable)
            res.append(index)
            heapq.heappush(unavail, (t+tasks[i], weight, index))
            
        return res
