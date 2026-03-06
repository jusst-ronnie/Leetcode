from bisect import bisect_left
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        ans = []

        for spell in spells:
            target = (success + spell - 1) // spell
            idx = bisect_left(potions, target)
            ans.append(m - idx)

        return ans