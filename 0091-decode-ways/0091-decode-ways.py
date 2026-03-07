class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if s[0] == '0':
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):

            # single digit
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # two digits
            two = int(s[i-2:i])
            if 10 <= two <= 26:
                dp[i] += dp[i-2]

        return dp[n]