from collections import Counter

class Solution:
    def maximumTotalDamage(self, power):
        count = Counter(power)
        nums = sorted(count.keys())
        
        values = [x * count[x] for x in nums]
        n = len(nums)
        
        dp = [0] * n
        
        for i in range(n):
            take = values[i]
            
            j = i - 1
            while j >= 0 and nums[i] - nums[j] <= 2:
                j -= 1
            
            if j >= 0:
                take += dp[j]
            
            skip = dp[i-1] if i > 0 else 0
            dp[i] = max(take, skip)
        
        return dp[-1]