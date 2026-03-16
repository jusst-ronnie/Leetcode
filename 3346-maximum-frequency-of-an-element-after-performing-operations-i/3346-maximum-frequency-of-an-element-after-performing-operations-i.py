from bisect import bisect_left, bisect_right
from collections import Counter

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        nums.sort()
        count = Counter(nums)
        ans = 0
        
        for t in set(nums):
            left = bisect_left(nums, t - k)
            right = bisect_right(nums, t + k)
            
            total = right - left
            same = count[t]
            
            ans = max(ans, same + min(numOperations, total - same))
        
        # also consider target values not in nums
        i = 0
        for j in range(len(nums)):
            while nums[j] - nums[i] > 2*k:
                i += 1
            ans = max(ans, min(numOperations, j - i + 1))
        
        return ans