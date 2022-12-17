class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        x,y,dx,dy=0,0,0,1
        
        for c in instructions:
            if c == 'G':
                x += dx
                y += dy
                
            elif c == 'L':
                tmp = dy
                dy = dx
                dx = -tmp
                
            else:
                tmp = dx
                dx = dy
                dy = -tmp          
        
        return (x == 0 and y == 0) or (dy != 1)
