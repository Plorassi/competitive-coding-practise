class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        self.hashmap = collections.defaultdict(list)
        for i,w in enumerate(wordsDict):
            self.hashmap[w].append(i)

        if word1 != word2:
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
        else:
            l1 = self.hashmap[word1]
            res = float('inf')
            for x,y in zip(l1,l1[1:]):
                res = min(res, abs(x-y))

            return res

