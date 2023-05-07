class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node.count+=1
            node = node.children[char]
            
    def find(self, word):
        node = self.root
        for i, char in enumerate(word):
            if node.count==1:
                return i
            node = node.children[char]


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def abbrev(w, i=1):
            # i included in the prefix
            if len(w)-i<3:
                return w
            return w[:i]+str(len(w)-i-1)+w[-1]
        
        abbr2word = defaultdict(list) # store all initial abbrevations for each word
        word2abbr = {} # final abbrevation dictionary

        for word in words:
            # just add basic abbrevations to group them
            abbr2word[abbrev(word)].append(word)

        for abbr, group in abbr2word.items():
            # go through each group
            if len(group)>1:
                trie = Trie()
                for word in group:
                    trie.insert(word)
                
                for word in group:
                    # search for index where count=1
                    index = trie.find(word)
                    word2abbr[word] = abbrev(word, index)
                
            else:
                # if not group then its a solution, add directly
                word2abbr[group[0]] = abbr
        return [word2abbr[word] for word in words]
