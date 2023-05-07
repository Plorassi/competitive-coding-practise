class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        res=[]
        for i in range(sideLength):
            for j in range(sideLength):
                xFolds=(width-i-1)//sideLength+1
                yFolds=(height-j-1)//sideLength+1
                res.append(xFolds*yFolds)
        res.sort(reverse=True)
        return sum(res[:maxOnes])
