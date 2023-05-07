class Solution:

    def wordSquares(self, words: List[str]) -> List[List[str]]:

        results = []
        prefixTable = collections.defaultdict(set)

        def backtrack(step, tmp, results, prefixTable):

            if step == len(tmp[0]):
                results.append(tmp.copy())
                return

            prefix = ''.join(word[step] for word in tmp)
            candidates = prefixTable[prefix]

            for word in candidates:
                tmp.append(word)
                backtrack(step+1,tmp,results,prefixTable)
                tmp.pop()

        for word in words:
            for i in range(1,len(word)):
                prefixTable[word[:i]].add(word)

        for word in words:
            tmp = [word]
            step = 1
            backtrack(step, tmp, results, prefixTable)

        return results
