class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = [0]
        pot = 1
        
        for i in range(1,n+1):
            if i == pot*2:
                pot = pot*2

            ans.append(1+ans[i-pot])
            
        return ans[:n+1]
            
