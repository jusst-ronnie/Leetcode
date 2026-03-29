class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Check even indices (0 and 2)
        # They are equal if they match directly or if they match after a swap
        even_match = (
            (s1[0] == s2[0] and s1[2] == s2[2]) or 
            (s1[0] == s2[2] and s1[2] == s2[0])
        )
        
        # Check odd indices (1 and 3)
        # They are equal if they match directly or if they match after a swap
        odd_match = (
            (s1[1] == s2[1] and s1[3] == s2[3]) or 
            (s1[1] == s2[3] and s1[3] == s2[1])
        )
        
        return even_match and odd_match