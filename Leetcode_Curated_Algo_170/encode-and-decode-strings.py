class Codec:
    
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        part_1 = ''
        part_2 = ''
        for i,s in enumerate(strs):
            l = len(s)
            if i != 0:
                part_1 += ' ' + str(l)
            else:
                part_1 += str(l)

            part_2 += s

        part_1 += 'A'
        return part_1+part_2

    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        print(s)
        index = s.find('A')
        part_1 = s[:index]
        part_2 = s[index+1:]
        lenghts = part_1.split(' ')
        res = []
        i = 0
        for cnt in range(len(lenghts)):
            if lenghts[cnt] == '0':
                res.append("")
            else:
                res.append(part_2[i:i+int(lenghts[cnt])])
            i = i+int(lenghts[cnt])
            cnt += 1

        return res

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
