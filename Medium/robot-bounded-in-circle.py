class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        s = [0,0]
        d = [0,1]
        
        
        for l in instructions:
            
            if l == 'G':
                s[0] += d[0]
                s[1] += d[1]
                
            elif l == 'L':
                d[0], d[1] = -1*d[1], d[0]
                    
            else:
                d[0], d[1] = d[1], -1*d[0]
                    
        if s == [0,0]: #back to original position
            return True
        elif d == [0,1]: #different from original position and direction does not change
            return False
        else:
            return True
