class Solution:
    def countValidSelections(self, nums):
        n = len(nums)
        ans = 0

        def simulate(start, direction):
            arr = nums[:]
            curr = start
            dir = direction

            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += dir
                else:
                    arr[curr] -= 1
                    dir *= -1
                    curr += dir

            return all(x == 0 for x in arr)

        for i in range(n):
            if nums[i] == 0:
                if simulate(i, -1):
                    ans += 1
                if simulate(i, 1):
                    ans += 1

        return ans