class Solution:
    def maximumEnergy(self, energy, k):
        n = len(energy)
        dp = [0] * n
        ans = -10**18

        for i in range(n-1, -1, -1):
            dp[i] = energy[i]
            if i + k < n:
                dp[i] += dp[i + k]
            ans = max(ans, dp[i])

        return ans