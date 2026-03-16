class Solution:
    def minOperations(self, nums):
        stack = []
        ops = 0

        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()

            if num > 0 and (not stack or stack[-1] < num):
                stack.append(num)
                ops += 1

        return ops