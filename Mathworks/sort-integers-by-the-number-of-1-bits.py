class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda num : (self.count_bits(num), num))
    
    def count_bits(self, n):
        count = 0
        while n:
            count += n&1
            n = n>>1
        return count
