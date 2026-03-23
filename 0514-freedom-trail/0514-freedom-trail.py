from functools import lru_cache
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring, key):
        n = len(ring)
        
        # Store positions of each character
        pos_map = defaultdict(list)
        for i, ch in enumerate(ring):
            pos_map[ch].append(i)
        
        @lru_cache(None)
        def dp(i, curr_pos):
            # If all characters matched
            if i == len(key):
                return 0
            
            res = float('inf')
            
            # Try all positions of key[i]
            for next_pos in pos_map[key[i]]:
                diff = abs(curr_pos - next_pos)
                step = min(diff, n - diff)  # circular rotation
                
                res = min(res, step + 1 + dp(i+1, next_pos))
            
            return res
        
        return dp(0, 0)