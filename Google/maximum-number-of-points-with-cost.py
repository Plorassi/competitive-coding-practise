class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        dp = points[0]
        
        for i in range(1,len(points)):
            left, right = [], []
            
            for j in range(len(points[0])):
                if not left:
                    left.append(dp[j])
                else:
                    left.append(max(dp[j], left[-1]-1))
            
            for j in range(len(points[0]))[::-1]:
                if not right:
                    right.append(dp[j])
                else:
                    right.append(max(dp[j], right[-1]-1))
                    
            for j in range(len(dp)):
                dp[j] = max(left[j],right[len(dp)-j-1])+points[i][j]
            
        return max(dp)
