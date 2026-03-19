class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26
        
        # Count magazine letters
        for ch in magazine:
            count[ord(ch) - ord('a')] += 1
        
        # Use letters for ransomNote
        for ch in ransomNote:
            idx = ord(ch) - ord('a')
            count[idx] -= 1
            
            if count[idx] < 0:
                return False
        
        return True