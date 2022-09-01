class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        l = len(rolls)
        s = mean*(l+n) - sum(rolls)
        res = []
        
        if s < n or s > n*6:
            return res
            
        while s:
            dice = min(s-n+1, 6)
            n -= 1
            s -= dice
            res.append(dice)
            
        return res
        
