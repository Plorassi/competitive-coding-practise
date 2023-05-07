class Solution:
    def numWays(self, n: int, k: int) -> int:

        if n == 1:
            return k
        if n == 2:
            return k*k
        
        total = [0]*(n+1)
        total[1] = k
        total[2] = k*k

        for i in range(3,n+1):
            total[i] = (k-1)*total[i-1] + (k-1)*total[i-2]

        return total[n] 
