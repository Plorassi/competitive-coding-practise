class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.hashmap = collections.defaultdict(list)
        for i,w in enumerate(wordsDict):
            self.hashmap[w].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.hashmap[word1], self.hashmap[word2]
        i,j = 0,0
        res = float('inf')
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i]-l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
