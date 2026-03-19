class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = [0] * 26
        
        # Step 1: count frequency
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        
        # Step 2: find first unique
        for i, ch in enumerate(s):
            if count[ord(ch) - ord('a')] == 1:
                return i
        
        return -1