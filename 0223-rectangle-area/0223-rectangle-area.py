class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Area of rectangle A
        area_a = (ax2 - ax1) * (ay2 - ay1)
        
        # Area of rectangle B
        area_b = (bx2 - bx1) * (by2 - by1)
        
        # Calculate overlap boundaries
        overlap_width = min(ax2, bx2) - max(ax1, bx1)
        overlap_height = min(ay2, by2) - max(ay1, by1)
        
        # Area of overlap (ensure it's not negative)
        overlap_area = 0
        if overlap_width > 0 and overlap_height > 0:
            overlap_area = overlap_width * overlap_height
            
        # Total Area = Area A + Area B - Overlap
        return area_a + area_b - overlap_area