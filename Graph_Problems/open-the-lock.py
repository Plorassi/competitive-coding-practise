class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        nxt =  {"0":"1",
                "1":"2",
                "2":"3",
                "3":"4",
                "4":"5",
                "5":"6",
                "6":"7",
                "7":"8",
                "8":"9",
                "9":"0"}
        
        prev = {"0":"9",
                "1":"0",
                "2":"1",
                "3":"2",
                "4":"3",
                "5":"4",
                "6":"5",
                "7":"6",
                "8":"7",
                "9":"8"}
        
        q = collections.deque(["0000"])
        res = 0
        visit = set()
        
        if "0000" in deadends:
            return -1
        
        while q:
            for i in range(len(q)):
                src = q.popleft()
                if src == target:
                    return res
                if src in visit:
                    continue
                visit.add(src)
                for i in range(4):
                    n = src[:i] + nxt[src[i]] + src[i+1:]
                    p = src[:i] + prev[src[i]] + src[i+1:]
                    if n not in deadends:
                        q.append(n)
                    if p not in deadends:
                        q.append(p)
                        
            res += 1
        return -1
