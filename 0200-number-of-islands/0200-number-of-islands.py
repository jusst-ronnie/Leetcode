class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # Base Case: If out of bounds or at a water cell ('0')
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
                return
            
            # Mark the current cell as visited by "sinking" it
            grid[r][c] = '0'
            
            # Explore all 4 neighbors
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    # We found a new island!
                    island_count += 1
                    # Sink the entire island
                    dfs(r, c)
                    
        return island_count