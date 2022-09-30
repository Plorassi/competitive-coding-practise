class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(e for e in s if e.isalnum())
        if s == s[::-1]:
            return True
        else:
            return False
