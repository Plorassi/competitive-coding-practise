class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        hm = collections.defaultdict(list)
        for string in strings:
            rd = []
            anch = ord(string[0])
            for a in string:
                cd = ord(a)-anch
                if cd < 0:
                    cd += 26
                rd.append(str(cd))
            key = '-'.join(rd)
            hm[key].append(string)
        return hm.values()
        
