class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = collections.defaultdict(lambda:-1)
        stack = []
        ans = []
        
        for n in nums2:
            while stack and stack[-1] < n:
                res[stack[-1]] = n
                stack.pop()
            stack.append(n)
            
        for n in nums1:
            ans.append(res[n])
        
        return ans
