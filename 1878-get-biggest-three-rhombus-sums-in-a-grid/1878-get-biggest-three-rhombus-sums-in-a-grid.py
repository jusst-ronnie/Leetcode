class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        sums = set()

        for i in range(m):
            for j in range(n):

                # k = 0 (single cell rhombus)
                sums.add(grid[i][j])

                # try larger rhombus sizes
                k = 1
                while True:
                    if i-k < 0 or i+k >= m or j-k < 0 or j+k >= n:
                        break

                    total = 0

                    # 4 edges
                    for d in range(k):
                        total += grid[i-k+d][j+d]   # top → right
                        total += grid[i+d][j+k-d]   # right → bottom
                        total += grid[i+k-d][j-d]   # bottom → left
                        total += grid[i-d][j-k+d]   # left → top

                    sums.add(total)
                    k += 1

        return sorted(sums, reverse=True)[:3]