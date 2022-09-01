class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        
        dp[len(s)] = True
        
        for i in range(0,len(s))[::-1]:
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
                    
                    
                    
        return dp[0]
                
                    
                    
            
            
            
            
        

