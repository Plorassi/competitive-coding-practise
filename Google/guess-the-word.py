# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def cntMatch(self, a, b):
        count = 0
        for l,m in zip(a,b):
            if l == m:
                count += 1
                
        return count
    
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        
        n = len(words)
        index = random.randrange(n)
        
        x = master.guess(words[index])
        if x == 6:
            return words[index]
        
        tmp = []
        for word in words:
            if x == self.cntMatch(words[index], word):
                tmp.append(word)
                
        return self.findSecretWord(tmp, master)
            
        
        
