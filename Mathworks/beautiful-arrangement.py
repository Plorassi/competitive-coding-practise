class Solution:
    def countArrangement(self, N):
        def count(i, X):
            if i == 1:
                return 1
            ans = 0
            for x in X:
                if x % i == 0 or i % x == 0:
                    ans += count(i-1,X-{x})  
            return ans
        
        return count(N, set(range(1, N + 1)))
