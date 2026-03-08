class Solution:
    def hasIncreasingSubarrays(self, nums, k):
        n = len(nums)

        for a in range(n - 2*k + 1):
            
            first = True
            for i in range(a, a + k - 1):
                if nums[i] >= nums[i+1]:
                    first = False
                    break

            second = True
            for i in range(a + k, a + 2*k - 1):
                if nums[i] >= nums[i+1]:
                    second = False
                    break

            if first and second:
                return True

        return False