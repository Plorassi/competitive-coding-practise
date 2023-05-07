def IDX(row,column):
    if type(row) is int:
        row=str(row)
    return column+row

class Excel:

    def __init__(self, height: int, width: str):
        self.mat=defaultdict(int)
        self.link={}
    
    def set(self, row: int, column: str, val: int) -> None:
        idx=IDX(row,column)
        self.mat[idx]=val
        if idx in self.link:
            del self.link[idx]
        
    def __dfs(self,idx):
        if idx not in self.link:return self.mat[idx]
        return sum(self.link[idx][idx1]*self.__dfs(idx1) for idx1 in self.link[idx])
                
    def get(self, row: int, column: str) -> int:
        idx=IDX(row,column)
        if idx in self.link:
            return self.__dfs(idx)
        else:
            return self.mat[idx]
        
    def __getC(self,col0,col1):
        COL=''.join(chr(ord('A')+i) for i in range(26))
        return COL[COL.find(col0):COL.find(col1)+1]
    
    def getR(self,rg,cnt):
        idx0,idx1=rg.split(':')
        row0,col0=int(idx0[1:]),idx0[:1]
        row1,col1=int(idx1[1:]),idx1[:1]
        for row in range(row0,row1+1):
            for col in self.__getC(col0,col1):
                cnt[col+str(row)]+=1
        
    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        idx=IDX(row,column)
        cnt=defaultdict(int)
        for link in numbers:
            if ':' not in link:
                cnt[link]+=1
            else:
                self.getR(link,cnt)
        self.mat[idx]=0
        self.link[idx]=cnt
        return self.get(row,column)
