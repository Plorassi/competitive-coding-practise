class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dp = collections.defaultdict(int)
        
        for w in sorted(words, key=len):
            tmp = 0
            for i in range(len(w)):
                tmp = max(tmp, dp[w[:i] + w[i + 1:]])
            dp[w] = tmp + 1
                
        return max(dp.values())
