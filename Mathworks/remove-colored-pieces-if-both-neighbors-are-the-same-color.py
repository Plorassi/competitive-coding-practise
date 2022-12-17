class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        ta, tb = 0, 0
        
        for i in range(1,len(colors)-1):
            if colors[i-1] == 'A' and colors[i] == 'A' and colors[i+1] == 'A':
                ta += 1
            if colors[i-1] == 'B' and colors[i] == 'B' and colors[i+1] == 'B':
                tb += 1
                
        if ta > tb:
            return True
        else:
            return False
        
