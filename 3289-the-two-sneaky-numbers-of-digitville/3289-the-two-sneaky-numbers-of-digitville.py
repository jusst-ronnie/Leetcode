class Solution:
    def getSneakyNumbers(self, nums):
        seen = set()
        ans = []

        for x in nums:
            if x in seen:
                ans.append(x)
            else:
                seen.add(x)

        return ans