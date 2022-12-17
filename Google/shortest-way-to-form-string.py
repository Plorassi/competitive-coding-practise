class Solution:
    def shortestWay(self, source, target):
        positions = collections.defaultdict(list)
        for i, c in enumerate(source):
            positions[c].append(i)
            
        loop = 1
        prev = -1
        
        for i, c in enumerate(target):
            if c not in positions:
                return -1
            index = bisect.bisect_right(positions[c], prev)
            if index == len(positions[c]):
                loop += 1
                prev = positions[c][0]
            else:
                prev = positions[c][index]
                
        return loop   
