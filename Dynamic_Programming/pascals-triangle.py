class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        dp = [[1]]
        
        for i in range(2,numRows+1):
            x = dp[-1]
            temp = []
            temp.append(1)
            for j in range(len(x)-1):
                temp.append(x[j] + x[j+1])
            temp.append(1)
            dp.append(temp)
            
        return dp
