class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, n):
            if n == 0:
                return 1
            elif n % 2 == 0:
                res = helper(x, n / 2)
                return res * res
            else:
                return x * helper(x, n - 1)
            
        return helper(x, n) if n >= 0 else (1 / helper(x, abs(n))) # In the case of -n, then 1/(x^n)
