from collections import Counter

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        ans = []

        for i in range(n - k + 1):
            sub = nums[i:i+k]

            freq = Counter(sub)

            items = sorted(freq.items(), key=lambda a: (-a[1], -a[0]))

            s = 0
            for j in range(min(x, len(items))):
                val, cnt = items[j]
                s += val * cnt

            ans.append(s)

        return ans