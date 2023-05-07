class TrieNode:
    def __init__(self):
        self.words = set()
        self.children = {}

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.temp = self.root
        self.cache = collections.defaultdict(int)
        self.keyword = ''
        for sentence, time in zip(sentences, times):
            self.insert(self.root, sentence)
            self.cache[sentence] = time
            
    def insert(self, root, sentence):
        for char in sentence:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
            root.words.add(sentence)

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.cache[self.keyword] += 1
            self.insert(self.root, self.keyword)
            self.keyword = ''
            self.temp = self.root
            return []
        else:
            self.keyword += c
            if self.temp:
                self.temp = self.temp.children.get(c, None)
            if self.temp:
                return sorted(list(self.temp.words), key=lambda x: (-self.cache[x], x))[:3]
            return []
