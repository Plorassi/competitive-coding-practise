class Solution:
    def numSquares(self, n: int) -> int:
        
        amount = n
        
        dp = [amount for i in range(amount+1)]
        
        dp[0] = 0
        
        if amount <= 3:
            return amount
        
        coins = [i**2 for i in range(1,n)]
        
        
        for i in range(1,amount+1):
            
            for coin in coins:
                
                if i - coin < 0:
                    break    
                dp[i] = min(dp[i], 1+dp[i-coin])
                
                    
        return dp[amount]
