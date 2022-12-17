class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        minHeap = []
        curRooms = 0
        
        intervals.sort()
        
        for s,e in intervals:
            if minHeap and minHeap[0] <= s:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, e)
            else:
                heapq.heappush(minHeap, e)
                curRooms += 1
                
        return curRooms
