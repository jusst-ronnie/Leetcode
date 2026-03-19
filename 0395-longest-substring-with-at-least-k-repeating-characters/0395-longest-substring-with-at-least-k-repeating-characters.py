class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        # base case
        if len(s) < k:
            return 0
        
        # frequency map
        from collections import Counter
        count = Counter(s)
        
        for ch in count:
            if count[ch] < k:
                # split and solve recursively
                return max(self.longestSubstring(sub, k) for sub in s.split(ch))
        
        # all characters valid
        return len(s)