class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
        cmap = collections.defaultdict(list)

        for i,c in enumerate(colors):
            cmap[c].append(i)

        res = []

        for index, c in queries:
            if c not in cmap:
                res.append(-1)
            else:
                tmp = bisect.bisect_left(cmap[c], index)

                left_nearest = abs(cmap[c][max(tmp - 1, 0)] - index)
                right_nearest = abs(cmap[c][min(tmp, len(cmap[c]) - 1)] - index)
                res.append(min(left_nearest, right_nearest))

        return res
                
