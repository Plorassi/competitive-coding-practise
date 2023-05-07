"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def __init__(self):
        self.res = []
        
    def employeeFreeTime(self, schedule):
        
        def insertRange(left, right):
            start = bisect.bisect_left(self.res, left)
            end = bisect.bisect_right(self.res, right)
            subtrack = []
            if start%2 == 0:
                subtrack.append(left)
            if end%2 == 0:
                subtrack.append(right)
            self.res[start:end] = subtrack
            
        for e in schedule:
            for i in e:
                insertRange(i.start, i.end)
                
        ans = []
        for i in range(2,len(self.res),2):
            ans.append(Interval(start=self.res[i-1], end=self.res[i]))
        return ans
        
