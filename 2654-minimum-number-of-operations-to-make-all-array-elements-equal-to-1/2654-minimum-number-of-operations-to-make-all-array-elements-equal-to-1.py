from math import gcd

class Solution:
    def minOperations(self, nums):
        n = len(nums)

        ones = nums.count(1)
        if ones > 0:
            return n - ones

        ans = float('inf')

        for i in range(n):
            g = nums[i]
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    ans = min(ans, j - i + 1)
                    break

        if ans == float('inf'):
            return -1

        return (ans - 1) + (n - 1)