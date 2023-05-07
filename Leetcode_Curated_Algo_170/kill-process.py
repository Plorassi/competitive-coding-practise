class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        adj = collections.defaultdict(list)
        for i,p in enumerate(ppid):
            adj[p].append(pid[i])

        res = []
        visit = set()
        def dfs(node):
            if not node:
                return
            visit.add(node)
            res.append(node)
            for children in adj[node]:
                if children not in visit:
                    dfs(children)

        dfs(kill)
        return res
