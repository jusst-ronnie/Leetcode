class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        # Start at bottom-left
        row = m - 1
        col = 0
        
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                # If grid[row][col] is negative, everything to its right 
                # in this row is also negative.
                count += (n - col)
                # Move up to the next row
                row -= 1
            else:
                # If grid[row][col] is positive/zero, move right to 
                # find where the negatives start.
                col += 1
                
        return count