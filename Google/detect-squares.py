import math
class DetectSquares:

    def __init__(self):
        self.myPoints=Counter()        
        self.x_coord=defaultdict(set)
        
    def add(self, point: List[int]) -> None:
        
        x,y=point
        self.myPoints[x,y]+=1
        self.x_coord[x].add(y) 
        
    def count(self, point: List[int]) -> int:
        
        x1,y1=point[0],point[1]
        ans=0
        
        for y2 in self.x_coord[x1]:
            if y1==y2: continue
            
            side_length=y2-y1
            x2a=x1 + side_length #x2 option 1
            x2b=x1 - side_length # x2 option 2
            
            ans += self.myPoints[x1,y2] * self.myPoints[x2a, y2 ] * self.myPoints[x2a,y1] 
            ans += self.myPoints[x1,y2] * self.myPoints[x2b, y2 ] * self.myPoints[x2b,y1] 
        return ans
