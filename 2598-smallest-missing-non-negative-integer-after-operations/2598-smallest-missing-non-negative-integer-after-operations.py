from collections import Counter

class Solution:
    def findSmallestInteger(self, nums, value):
        cnt = Counter(x % value for x in nums)

        i = 0
        while True:
            r = i % value
            if cnt[r] > 0:
                cnt[r] -= 1
                i += 1
            else:
                return i