class Solution:
    def magicalSum(self, m, k, nums):
        MOD = 10**9 + 7
        n = len(nums)

        powv = [[1]*(m+1) for _ in range(n)]
        for i in range(n):
            for j in range(1, m+1):
                powv[i][j] = powv[i][j-1] * nums[i] % MOD

        C = [[0]*(m+1) for _ in range(m+1)]
        for i in range(m+1):
            C[i][0] = C[i][i] = 1
            for j in range(1, i):
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

        from collections import defaultdict
        dp = {(0,0,0):1}

        for i in range(n):
            new = defaultdict(int)

            for (used, carry, ones), val in dp.items():
                for c in range(m-used+1):
                    total = c + carry
                    bit = total & 1
                    newcarry = total >> 1
                    newones = ones + bit

                    if newones > k:
                        continue

                    ways = C[m-used][c] * powv[i][c] % MOD

                    new[(used+c, newcarry, newones)] = (
                        new[(used+c, newcarry, newones)] +
                        val * ways
                    ) % MOD

            dp = new

        ans = 0
        for (used, carry, ones), val in dp.items():
            if used == m:
                ones += bin(carry).count("1")
                if ones == k:
                    ans = (ans + val) % MOD

        return ans