class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        s = sum(piles)
        n = len(piles)   
        dp = {}
        
        def dfs(i,j):
            
            if (i,j) in dp:
                return dp[(i,j)]   
            if i>=j:
                return 0
            
            even = False
            if (j-i)%2:
                even = True
                
            left, right = 0, 0
            if even:
                left = piles[i]
                right = piles[j]
            
            dp[(i,j)] = max(dfs(i+1,j)+left, dfs(i,j-1)+right)
            
            return dp[(i,j)]
            
        res = dfs(0,n-1)
        if res > s - res:
            return True
        else:
            return False
        
        
