class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        @lru_cache(None)
        def valid(i, j, k):
            if k < 0:
                return False
            
            if i >= j:
                return True
            
            if s[i] != s[j]:
                return valid(i, j - 1, k - 1) or valid(i + 1, j, k - 1)
            
            return valid(i + 1, j - 1, k)

        return valid(0, len(s) - 1, k)
