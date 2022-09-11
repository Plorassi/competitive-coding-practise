class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:(i[0], -i[1]))
        stack = [intervals[0]]
        
        for l,r in intervals[1:]:
            prevL, prevR = stack[-1]
            if prevL <= l and prevR >= r:
                continue
            stack.append([l,r])
            
        return len(stack)
            
                
                
