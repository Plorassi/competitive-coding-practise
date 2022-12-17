class Solution:
    
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        n_subsequences = 0
        state = defaultdict(list)
        for i, word in enumerate(words):
            state[word[0]].append((i, 0))
        for char in S:
            old_bucket = state[char]
            state[char] = []
            for wordsidx, wordidx in old_bucket:
                newwordidx = wordidx + 1
                if newwordidx == len(words[wordsidx]):
                    n_subsequences += 1
                else:
                    state[words[wordsidx][newwordidx]].append((wordsidx, newwordidx))
        return n_subsequences
