class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:

        rc, cc = collections.defaultdict(int), collections.defaultdict(int)

        for r in range(len(picture)):
            for c in range(len(picture[0])):
                if picture[r][c] == 'B':
                    rc[r] += 1
                    cc[c] += 1

        res = 0
        for r in range(len(picture)):
            for c in range(len(picture[0])):
                if picture[r][c] == 'B':
                    if rc[r] == 1 and cc[c] == 1:
                        res += 1


        return res
                    


        
