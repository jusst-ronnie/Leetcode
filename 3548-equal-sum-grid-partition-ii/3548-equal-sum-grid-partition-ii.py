from collections import Counter

class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        def check(matrix):
            m, n = len(matrix), len(matrix[0])
            row_sums = [sum(row) for row in matrix]
            total_sum = sum(row_sums)
            
            # Counts for the bottom section (starts with the whole grid)
            top_counts = Counter()
            bottom_counts = Counter()
            for r in range(m):
                for c in range(n):
                    bottom_counts[matrix[r][c]] += 1
            
            current_top_sum = 0
            for i in range(m - 1): # Cut after row i
                # Move current row from bottom to top counts
                for val in matrix[i]:
                    bottom_counts[val] -= 1
                    if bottom_counts[val] == 0: del bottom_counts[val]
                    top_counts[val] += 1
                
                current_top_sum += row_sums[i]
                current_bottom_sum = total_sum - current_top_sum
                
                # Case 1: Perfect split
                if current_top_sum == current_bottom_sum:
                    return True
                
                # Case 2: Discount one cell from Top Section
                diff_top = current_top_sum - current_bottom_sum
                if diff_top > 0:
                    rows_top = i + 1
                    # If it's a 2D block, any cell works
                    if rows_top > 1 and n > 1:
                        if diff_top in top_counts: return True
                    # If it's a 1D line, only the ends work
                    elif rows_top == 1: # Single row
                        if matrix[0][0] == diff_top or matrix[0][n-1] == diff_top:
                            return True
                    elif n == 1: # Single column
                        if matrix[0][0] == diff_top or matrix[i][0] == diff_top:
                            return True
                
                # Case 3: Discount one cell from Bottom Section
                diff_bottom = current_bottom_sum - current_top_sum
                if diff_bottom > 0:
                    rows_bottom = m - (i + 1)
                    if rows_bottom > 1 and n > 1:
                        if diff_bottom in bottom_counts: return True
                    elif rows_bottom == 1: # Single row
                        if matrix[m-1][0] == diff_bottom or matrix[m-1][n-1] == diff_bottom:
                            return True
                    elif n == 1: # Single column
                        if matrix[i+1][0] == diff_bottom or matrix[m-1][0] == diff_bottom:
                            return True
            return False

        # Try horizontal cuts
        if check(grid): 
            return True
        
        # Try vertical cuts by transposing the grid
        # Use [list(row) for row in zip(*grid)] to convert tuples back to lists
        transposed = [list(row) for row in zip(*grid)]
        return check(transposed)