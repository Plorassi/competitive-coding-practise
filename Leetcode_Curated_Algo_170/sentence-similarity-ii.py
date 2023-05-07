class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(sentence1) != len(sentence2):
            return False

        parent = {}
        for x in sentence1+sentence2:
            parent[x] = x

        def find(a):
            if a not in parent:
                parent[a] = a
            elif parent[a]!=a:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a,b):
            parent[find(a)] = find(b)
            return

        for a,b in similarPairs:
            union(a,b)

        for x in sentence1+sentence2:
            parent[x] = find(x)

        for a,b in zip(sentence1, sentence2):
            if a!=b and parent[a] != parent[b]:
                return False

        return True
