class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0], [0,1], [-1,0], [0,-1],
                       [1,1], [1,-1], [-1,1], [-1,-1]]
        
        board[rMove][cMove] = color
        
        def legalMove(r,c,color,direc):
            dr, dc = direc
            r,c = r+dr, c+dc
            l = 1
            
            while (r in range(ROWS) and c in range(COLS)):
                l += 1
                if board[r][c] == '.':
                    return False
                if board[r][c] == color:
                    return l >= 3
                    
                r,c = r+dr, c+dc
                
            return False
        
        for direc in directions:
            if legalMove(rMove, cMove, color, direc):
                return True
            
        return False
