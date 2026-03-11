class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        
        # dp[j] will store the number of subsequences of s that match t[:j]
        # We use a 1D array and iterate backwards to avoid using updated values
        dp = [0] * (m + 1)
        
        # Base case: An empty t is a subsequence of any prefix of s (exactly 1 way)
        dp[0] = 1
        
        for i in range(1, n + 1):
            # Iterate backwards through t to use the dp values from the previous 'i'
            for j in range(m, 0, -1):
                if s[i-1] == t[j-1]:
                    # Current = (ways if we use s[i-1]) + (ways if we skip s[i-1])
                    dp[j] = dp[j-1] + dp[j]
                else:
                    # Current = (ways if we skip s[i-1])
                    # dp[j] remains the same as it was for the previous character in s
                    pass
                    
        return dp[m]