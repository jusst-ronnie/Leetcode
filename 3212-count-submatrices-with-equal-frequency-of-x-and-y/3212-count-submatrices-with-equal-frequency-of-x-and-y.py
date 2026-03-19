class Solution:
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        
        prefix = [[0]*n for _ in range(m)]
        countX = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                val = 0
                if grid[i][j] == 'X':
                    val = 1
                elif grid[i][j] == 'Y':
                    val = -1
                
                x = 1 if grid[i][j] == 'X' else 0
                
                prefix[i][j] = val
                countX[i][j] = x
                
                if i > 0:
                    prefix[i][j] += prefix[i-1][j]
                    countX[i][j] += countX[i-1][j]
                if j > 0:
                    prefix[i][j] += prefix[i][j-1]
                    countX[i][j] += countX[i][j-1]
                if i > 0 and j > 0:
                    prefix[i][j] -= prefix[i-1][j-1]
                    countX[i][j] -= countX[i-1][j-1]
        
        count = 0
        for i in range(m):
            for j in range(n):
                if prefix[i][j] == 0 and countX[i][j] > 0:
                    count += 1
        
        return count