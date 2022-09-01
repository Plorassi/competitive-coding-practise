class Solution:
    def minMeetingRooms(self, intervals):

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, cnt = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                cnt += 1

            else:
                e += 1
                cnt -= 1

            res = max(res, cnt)


        return res

