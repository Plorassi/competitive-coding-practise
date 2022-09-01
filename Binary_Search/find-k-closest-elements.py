class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        l,r = 0, len(arr)-1
        start = 0
        
        while l<=r:
            mid = (l+r)//2
            if arr[mid] > x:
                r = mid-1
            elif arr[mid] < x:
                l = mid+1
            else:
                start = mid
                break
                

        if l>r:
            if l == len(arr):
                start = r
            elif r < 0:
                start = l
            elif abs(arr[l] - x) < abs(arr[r] - x):
                start = l
            else:
                start = r
            
            
        res = [arr[start]]
        k -= 1
        l,r = start-1, start+1
        
        while k > 0:
            if l < 0:
                res.append(arr[r])
                r += 1
                k -= 1
                    
            elif r > len(arr)-1:
                res.append(arr[l])
                l -= 1
                k -= 1

            elif abs(arr[l] - x) <= abs(arr[r] - x):
                res.append(arr[l])
                l -= 1
                k -= 1

            else:
                res.append(arr[r])
                r += 1
                k -= 1

        res.sort()
        return res
