class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        l1, l2 = len(nums1), len(nums2)
        
        total = l1+l2
        half = total // 2
        l,r = 0, l1-1
        
        while True:
            i = (l+r)//2
            j = half - i - 2
            
            Aleft = nums1[i] if i>=0 else float('-inf')
            Bleft = nums2[j] if j>=0 else float('-inf')
            Aright = nums1[i+1] if i+1<l1 else float('inf')
            Bright = nums2[j+1] if j+1<l2 else float('inf')
            
            if Bright >= Aleft and Aright >= Bleft:
                
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                
            elif Aleft > Bright:
                r = i-1
            else:
                l = i+1
