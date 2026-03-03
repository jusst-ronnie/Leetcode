class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        first_index = {}
        
        for i, ch in enumerate(s):
            if ch in first_index:
                prev = first_index[ch]
                if i - prev - 1 != distance[ord(ch) - ord('a')]:
                    return False
            else:
                first_index[ch] = i
        
        return True