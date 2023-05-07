class HitCounter:

    def __init__(self):
        self.res = []

    def hit(self, timestamp: int) -> None:
        self.res.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        r = bisect.bisect_right(self.res, timestamp)
        l = bisect.bisect_right(self.res, timestamp-300)

        return r-l


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
