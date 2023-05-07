class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        res = [0]*length
        if not updates:
            return res

        for s,e,i in updates:
            res[s] += i
            if e+1 < length:
                res[e+1] -= i


        for i in range(1,length):
            res[i] += res[i-1]

        return res
        
