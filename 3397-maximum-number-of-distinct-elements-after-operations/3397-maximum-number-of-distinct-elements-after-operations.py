class Solution:
    def maxDistinctElements(self, nums, k):
        nums.sort()
        prev = -10**18
        count = 0

        for x in nums:
            low = x - k
            high = x + k

            val = max(low, prev + 1)

            if val <= high:
                count += 1
                prev = val

        return count