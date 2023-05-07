class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = collections.defaultdict(int)
        
        for _from, to, amount in transactions:
            balance[_from] -= amount
            balance[to] += amount
        
        debt = [v for v in balance.values() if v]
        n = len(debt)
        
        def dfs(i):
            while i < n and debt[i] == 0:
                i += 1
            if i == n:
                return 0
            res, tested = math.inf, set()
            for j in range(i + 1, n):
                if debt[i] * debt[j] < 0 and debt[j] not in tested:
                    debt[j] += debt[i]
                    res = min(res, dfs(i + 1) + 1)
                    debt[j] -= debt[i]
                    tested.add(debt[j])
            return res
        
        return dfs(0)
