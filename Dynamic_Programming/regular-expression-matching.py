class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        main_str = [char for char in s]
        pat_str = [char for char in p]
        
        main_str = ['-'] + main_str
        pat_str = ['-'] + pat_str
        
        dp = [[0 for i in range(len(main_str))] for j in range(len(pat_str))]
        
        
        dp[0][0] = 1
        
        for i in range(1,len(pat_str)):
            if pat_str[i] == '*':
                dp[i][0] = dp[i-2][0]
            else:
                dp[i][0] = 0
                
                
        for i in range(1,len(pat_str)):
            for j in range(1,len(main_str)):
                
                if pat_str[i] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif pat_str[i] == '*':
                    if dp[i-2][j]:
                        dp[i][j] = 1
                    elif pat_str[i-1] == main_str[j] or pat_str[i-1] == '.':
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = 0
                elif pat_str[i] == main_str[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 0
                    
        return dp[-1][-1]
