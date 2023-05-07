class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        nn, result = len(s), []

        def getPerm(comb, counter):
            if len(comb) == nn:
                result.append(comb)
                return

            for key in counter.keys():
                if counter[key] > 0:
                    newCounter = counter.copy()
                    newCounter[key] -= 2
                    getPerm(key+comb+key, newCounter)


        counter = Counter(s)
        odds = []
        for key in counter.keys():
            if counter[key]%2==1:
                odds.append(key)
                counter[key]-=1

        if len(odds) > 1:
            return result

        comb = odds[0] if len(odds) == 1 else ''

        getPerm(comb, counter)
        return result
