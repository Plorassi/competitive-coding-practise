class Solution:
    def maxLength(self, arr: List[str]) -> int:

        res = 0
        
        def backtrack(start, comb):
            
            nonlocal res
            
            for i in range(start, len(arr)):
                x = Counter(comb)
                y = Counter(arr[i])
                z = x+y

                if max(z.values()) > 1:
                    continue  
                    
                comb += arr[i]
                res = max(res, len(comb))
                backtrack(i+1, comb)
                comb = comb[:-(len(arr[i]))]
                
        backtrack(0,"")
        return res
