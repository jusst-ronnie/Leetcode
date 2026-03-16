class Solution:
    def countUnguarded(self, m, n, guards, walls):
        grid = [[0]*n for _ in range(m)]

        # mark guards
        for r,c in guards:
            grid[r][c] = 1

        # mark walls
        for r,c in walls:
            grid[r][c] = 2

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for r,c in guards:
            for dr,dc in directions:
                nr,nc = r+dr, c+dc

                while 0<=nr<m and 0<=nc<n and grid[nr][nc] != 1 and grid[nr][nc] != 2:
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 3
                    nr += dr
                    nc += dc

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1

        return count