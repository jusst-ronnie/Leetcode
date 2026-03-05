class Solution:
    def combine(self, n: int, k: int):
        res = []
        path = []

        def dfs(start):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                dfs(i + 1)
                path.pop()

        dfs(1)
        return res