class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        hmap = collections.defaultdict(int)
        res = 0
        for t in time:
            rem = t%60
            if rem == 0:
                res += hmap[rem]
            else:
                if 60-rem in hmap:
                    res += hmap[60-rem]
            hmap[rem] += 1
            
        return res
                
