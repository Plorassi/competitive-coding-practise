class Solution:
    def totalCost(self, costs: List[int], k: int, cand: int) -> int:
        n = len(costs)
        l , r = cand-1, n-cand
        leftHeap = costs[:min(l+1,n)] + [float("inf")]    
        rightHeap = costs[max(0,r,l+1):] + [float("inf")]
        heapq.heapify(leftHeap)
        heapq.heapify(rightHeap)
        res = 0
        while k :
            min1,min2 = leftHeap[0],rightHeap[0]
            if min1 <= min2 :   # min found on left side
                res += heapq.heappop(leftHeap)
                l += 1
                if l < r and l<n :   
                    heapq.heappush(leftHeap,costs[l])
            else:   # min found on right side
                res += heapq.heappop(rightHeap)
                r -= 1
                if l < r and r>=0 :
                    heapq.heappush(rightHeap,costs[r])
            k -= 1
        return res
