import math
from collections import defaultdict

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        max_total = 1
        
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                dx = points[j][0] - x1
                dy = points[j][1] - y1
                
                g = math.gcd(dy, dx)
                
                # Normalize the sign so (dy, dx) is always consistent
                # regardless of the order of points.
                final_dy = dy // g
                final_dx = dx // g
                
                # Ensure the 'vector' always points in a consistent direction
                if final_dx < 0 or (final_dx == 0 and final_dy < 0):
                    final_dx = -final_dx
                    final_dy = -final_dy
                    
                slope = (final_dy, final_dx)
                slopes[slope] += 1
            
            if slopes:
                current_max = max(slopes.values()) + 1
                max_total = max(max_total, current_max)
                
        return max_total