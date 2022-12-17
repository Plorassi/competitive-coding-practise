class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 or (x%10 == 0 and x!=0):
            return False
        
        tmp = 0
        while tmp < x:
            rem = x%10
            tmp = 10*tmp + rem
            x //= 10
            
        return x == tmp or x == tmp//10
