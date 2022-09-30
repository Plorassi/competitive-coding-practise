class Solution:
    def maximumSwap(self, num: int) -> int:
        
		# segment 1
        digits = list(map(int, str(num)))
        container = {digit: i for i, digit in enumerate(digits)}
		
		# segment 2
        for i, digit in enumerate(digits):
            index = None
            for c in range(9, digit, -1):
                if container.get(c, -1) > i:
                    index = container.get(c)
                    break
            else: continue
            digits[i], digits[index] = digits[index], digits[i]
            break
        
		# segment 3
        res, n = 0, len(digits) - 1
        for digit in digits:
            res += (digit * 10**n)
            n -= 1
        return res
