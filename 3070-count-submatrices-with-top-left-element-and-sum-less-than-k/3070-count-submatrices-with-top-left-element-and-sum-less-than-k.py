class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        # We'll use a 2D array to store prefix sums
        # S[i][j] represents the sum of the submatrix from (0,0) to (i,j)
        prefix_sum = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                # Using the Inclusion-Exclusion Principle:
                # Total Sum = Current + Top + Left - TopLeft (overlap)
                top = prefix_sum[r-1][c] if r > 0 else 0
                left = prefix_sum[r][c-1] if c > 0 else 0
                top_left = prefix_sum[r-1][c-1] if (r > 0 and c > 0) else 0
                
                current_sum = grid[r][c] + top + left - top_left
                prefix_sum[r][c] = current_sum
                
                if current_sum <= k:
                    count += 1
                else:
                    # Optimization: Since grid[i][j] >= 0, once a sum 
                    # exceeds k, any further submatrix expanding 
                    # to the right in this row will also exceed k.
                    break 
                    
        return count