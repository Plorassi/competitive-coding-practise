class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visitSet = set()
        preReq = {i:[] for i in range(numCourses)}
        
        for cre, pre in prerequisites:
            preReq[cre].append(pre)
            
        def dfs(crs):
            
            if crs in visitSet:
                return False
            if preReq[crs] == []:
                return True
            
            visitSet.add(crs)
            
            for pre in preReq[crs]:
                if not dfs(pre):
                    return False
                
            visitSet.remove(crs)
            preReq[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
            
            
            
        
