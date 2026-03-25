class Solution:
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        
        total = sum(sum(row) for row in grid)
        
        if total % 2 != 0:
            return False
        
        # Horizontal cut
        topSum = 0
        for i in range(m - 1):
            topSum += sum(grid[i])
            if topSum * 2 == total:
                return True
        
        # Vertical cut
        colSum = [0] * n
        
        for i in range(m):
            for j in range(n):
                colSum[j] += grid[i][j]
        
        leftSum = 0
        for j in range(n - 1):
            leftSum += colSum[j]
            if leftSum * 2 == total:
                return True
        
        return False