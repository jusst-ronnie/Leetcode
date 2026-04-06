class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Directions: North, East, South, West
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        # Starting position and direction (North)
        x = y = 0
        di = 0 # 0: North, 1: East, 2: South, 3: West
        
        # Convert obstacles to a set of tuples for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))
        
        max_dist_sq = 0
        
        for cmd in commands:
            if cmd == -2:  # Turn left
                di = (di + 3) % 4
            elif cmd == -1:  # Turn right
                di = (di + 1) % 4
            else:
                # Move forward k units
                for _ in range(cmd):
                    next_x = x + dx[di]
                    next_y = y + dy[di]
                    
                    # Check if the next position is an obstacle
                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y
                        # Update max distance squared
                        max_dist_sq = max(max_dist_sq, x*x + y*y)
                    else:
                        # Hit an obstacle, stop moving for this command
                        break
                        
        return max_dist_sq