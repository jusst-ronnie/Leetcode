from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # Separate characters by index parity
        s1_even = s1[0::2]
        s2_even = s2[0::2]
        
        s1_odd = s1[1::2]
        s2_odd = s2[1::2]
        
        # Check if the multiset of characters matches for both parities
        return Counter(s1_even) == Counter(s2_even) and Counter(s1_odd) == Counter(s2_odd)
