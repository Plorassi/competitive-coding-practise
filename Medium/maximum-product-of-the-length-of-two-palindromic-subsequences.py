class Solution:
    def maxProduct(self, s: str) -> int:
        
        N, pali = len(s), {}
        
        for mask in range(1,1<<N):
            string = ""
            for i in range(N):
                if mask & 1<<i:
                    string += s[i]
            if string == string[::-1]:
                pali[mask] = len(string)
                
        res = 0
        for pali1 in pali:
            for pali2 in pali:
                if pali1 & pali2 == 0:
                    res = max(res, pali[pali1]*pali[pali2])
                    
        return res
        
        
