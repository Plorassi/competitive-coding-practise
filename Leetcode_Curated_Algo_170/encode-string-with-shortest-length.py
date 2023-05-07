class Solution:
    @lru_cache(None)
    def encode(self, s):
        n = len(s)
        i = (s+s).find(s,1)
        one = s
        if i < n:
            cnt = n//i
            one = str(cnt) + '[' + self.encode(s[:i]) + ']'

        result = [one]
        for j in range(1,n):
            result.append(self.encode(s[:j]) + self.encode(s[j:]))

        return min(result,key=len)
