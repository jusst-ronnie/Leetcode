class Solution:
    def maxIncreasingSubarrays(self, nums):
        ans = 0
        prev = 0
        curr = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1
            else:
                ans = max(ans, curr // 2)
                ans = max(ans, min(prev, curr))
                prev = curr
                curr = 1
        
        ans = max(ans, curr // 2)
        ans = max(ans, min(prev, curr))
        
        return ans