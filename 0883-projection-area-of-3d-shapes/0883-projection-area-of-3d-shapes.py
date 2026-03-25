class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        total_area = 0
        
        for i in range(n):
            row_max = 0
            col_max = 0
            for j in range(n):
                # Top View: If there is a tower, it contributes 1 to the area
                if grid[i][j] > 0:
                    total_area += 1
                
                # Tracking maximum for Front View (Row max)
                row_max = max(row_max, grid[i][j])
                
                # Tracking maximum for Side View (Column max)
                # Note: grid[j][i] lets us look at columns while iterating i
                col_max = max(col_max, grid[j][i])
            
            total_area += row_max + col_max
            
        return total_area