class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
        n = len(word)
        words = [word, word[::-1]]
        for B in board,zip(*board):
            for row in B:
                q=''.join(row).split('#')
                for w in words:
                    for s in q:
                        if len(s) == n:
                            if all(s[i]==w[i] or s[i]==' ' for i in range(n)):
                                return True
        return False
