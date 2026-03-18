from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        minutes = 0
        
        # 1. Build initial state
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # If there are no fresh oranges to start with
        if fresh_count == 0:
            return 0
            
        # 2. BFS
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while queue and fresh_count > 0:
            minutes += 1
            # Process all rotten oranges at the current time level
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # If neighbor is in bounds and is a fresh orange
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 # Make it rotten
                        fresh_count -= 1
                        queue.append((nr, nc))
                        
        return minutes if fresh_count == 0 else -1