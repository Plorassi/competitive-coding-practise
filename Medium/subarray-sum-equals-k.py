class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        tmp = 0
        res = 0
        prefix = {0:1}
        
        for n in nums:
            tmp += n
            if tmp-k in prefix:
                res += prefix[tmp-k]
            prefix[tmp] = 1 + prefix.get(tmp, 0)
            
        return res
