class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        res = 0
        
        l = 0
        
        while l < len(heights):
            
            if not stack:
                stack.append((l,heights[l]))
                res = max(res,heights[l])
                
            else:
                if heights[l] > stack[-1][1]:
                    stack.append((l,heights[l]))
                else:
                    index = stack[-1][0]
                    while stack and heights[l] < stack[-1][1]:
                        res = max(res, (l-stack[-1][0])*stack[-1][1])
                        index = stack[-1][0]
                        stack.pop()
                    stack.append((index,heights[l]))
                    
            l += 1
                    
                
        while stack:
            
            x,y = stack.pop()
            res = max(res, (len(heights)-x)*y)
            
        return res
