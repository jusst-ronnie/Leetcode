class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        max_dist = 0
        
        # Strategy 1: Compare everything with the first house
        # We look from the right end for the first color != colors[0]
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
                break
        
        # Strategy 2: Compare everything with the last house
        # We look from the left end for the first color != colors[n-1]
        for i in range(n):
            if colors[i] != colors[n - 1]:
                max_dist = max(max_dist, (n - 1) - i)
                break
                
        return max_dist