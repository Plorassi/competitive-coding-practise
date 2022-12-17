class Solution:
    def findMinDifference(self, A):
        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])
        minutes = []
        for time in A:
            minutes.append(convert(time))
        minutes.sort()
        
        res = float('inf')
        for i in range(0,len(minutes)-1):
            res = min(res, minutes[i+1]-minutes[i])
            
        return min(res, (24*60)-minutes[-1]+minutes[0])
