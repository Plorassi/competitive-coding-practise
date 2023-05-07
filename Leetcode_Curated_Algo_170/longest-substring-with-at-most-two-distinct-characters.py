from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        
        n = len(s)
        if n < 3:
            return n

        l,r = 0,0
        hashmap = defaultdict()
        res = 0

        while r<n:
            hashmap[s[r]] = r
            if len(hashmap) == 3:
                idx = min(hashmap.values())
                del hashmap[s[idx]]
                l = idx+1
            res = max(res, r-l+1)
            r += 1

        return res
