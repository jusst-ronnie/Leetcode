class Solution:
    def maximumTotalDamage(self, power):
        from collections import Counter
        
        count = Counter(power)
        values = sorted(count.keys())
        n = len(values)

        total = [v * count[v] for v in values]

        dp = [0] * n

        for i in range(n):
            take = total[i]

            j = i - 1
            while j >= 0 and values[i] - values[j] <= 2:
                j -= 1

            if j >= 0:
                take += dp[j]

            skip = dp[i-1] if i > 0 else 0
            dp[i] = max(skip, take)

        return dp[-1]