class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        i = 0
        res = ''
        while i<len(s):
            if i in indices:
                index = indices.index(i)
                if i+len(sources[index]) <= len(s) and sources[index] == s[i:i+len(sources[index])]:
                    res += targets[index]
                    i += len(sources[index])
                else:
                    res += s[i]
                    i += 1
                             
            else:
                res += s[i]
                i += 1
        return res
