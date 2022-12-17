class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        fr,sr,tr = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        
        res = []
        for w in words:
            tmp = set(w.lower())
            if tmp <= fr or tmp <= sr or tmp <= tr:
                res.append(w)
                
        return res
