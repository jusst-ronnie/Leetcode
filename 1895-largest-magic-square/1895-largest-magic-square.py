class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # 1. Precompute Prefix Sums for Rows and Columns
        rows = [[0] * (n + 1) for _ in range(m)]
        cols = [[0] * (m + 1) for _ in range(n)]
        
        for r in range(m):
            for c in range(n):
                rows[r][c+1] = rows[r][c] + grid[r][c]
                cols[c][r+1] = cols[c][r] + grid[r][c]
        
        def is_magic(r, c, k):
            # Target sum is the sum of the first row of this square
            target = rows[r][c+k] - rows[r][c]
            
            # Check all Rows
            for i in range(r + 1, r + k):
                if rows[i][c+k] - rows[i][c] != target:
                    return False
            
            # Check all Columns
            for j in range(c, c + k):
                if cols[j][r+k] - cols[j][r] != target:
                    return False
            
            # Check Main Diagonal
            diag1 = 0
            for i in range(k):
                diag1 += grid[r+i][c+i]
            if diag1 != target:
                return False
            
            # Check Anti-Diagonal
            diag2 = 0
            for i in range(k):
                diag2 += grid[r+i][c+k-1-i]
            if diag2 != target:
                return False
            
            return True

        # 2. Iterate from largest possible k down to 2
        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
                        
        return 1