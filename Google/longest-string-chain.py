class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dp = {"":0}
        
        def dfs(word):
            
            if word in dp:
                return dp[word]     
            dp[word] = 1
            ans = 0
            for i in range(len(word)):
                tmp = word[:i] + word[i+1:]
                if tmp in words:
                    ans = max(ans,dfs(tmp))
            dp[word] += ans
            return dp[word]
        
        words.sort(key = lambda x: -len(x))
        res = 0    
        for word in words:
            res = max(res, dfs(word))   

        return res

'''
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())
'''
