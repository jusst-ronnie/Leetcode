class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        
        for i in range(n - 1, -1, -1):
            freq = [0] * 26
            maxFreq = 0
            unique = 0   # 👈 track dynamically
            
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                
                if freq[idx] == 0:
                    unique += 1   # new character
                
                freq[idx] += 1
                maxFreq = max(maxFreq, freq[idx])
                
                length = j - i + 1
                
                # check balanced
                if length == maxFreq * unique:
                    dp[i] = min(dp[i], 1 + dp[j + 1])
        
        return dp[0]