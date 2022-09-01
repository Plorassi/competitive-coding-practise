class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        
        def capture(r,c):
            
            if (r not in range(ROWS) or
                c not in range(COLS) or
                board[r][c] != 'O' or
                (r,c) in visit):
                return 
            
            board[r][c] = 'T'
            visit.add((r,c))
            capture(r+1,c)
            capture(r,c+1)
            capture(r-1,c)
            capture(r,c-1)
            
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == 'O' 
                   and (r in [0,ROWS-1]
                   or c in [0,COLS-1])):
                    
                    capture(r,c)
                    
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                    
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
