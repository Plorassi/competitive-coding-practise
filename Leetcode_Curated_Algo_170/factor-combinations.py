class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        res = []

        def dfs(num, start, path):
            if len(path) > 0:
                res.append(path+[num]) 

            for i in range(start, int(math.sqrt(num)+1)):
                if num%i==0:
                    dfs(num//i,i,path+[i])

        dfs(n,2,[])
        return res
