class Solution:

    def __init__(self, w: List[int]):
        #self.w = w
        
        self.prefix = [w[0]]
        for n in w[1:]:
            self.prefix.append(self.prefix[-1] + n)
        
        self.total_weight = self.prefix[-1]

        

    def pickIndex(self) -> int:
        rand_int = randint(1, self.total_weight)
        
        idx = bisect_left(self.prefix, rand_int)
        return idx
