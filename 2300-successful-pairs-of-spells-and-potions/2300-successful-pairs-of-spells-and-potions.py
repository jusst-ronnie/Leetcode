from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            need = (success + spell - 1) // spell   # ceil(success/spell)
            idx = bisect_left(potions, need)
            result.append(m - idx)

        return result