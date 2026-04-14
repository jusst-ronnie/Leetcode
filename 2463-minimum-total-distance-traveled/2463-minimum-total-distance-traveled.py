class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        # 1. Sort both to ensure contiguous segments of robots map to factories
        robot.sort()
        factory.sort()
        
        # 2. Flatten the factories based on their capacity limits
        # Each "slot" in a factory is treated as a unique destination
        factory_positions = []
        for pos, limit in factory:
            factory_positions.extend([pos] * limit)
            
        n, m = len(robot), len(factory_positions)
        
        # 3. DP Table: dp[i][j] is the min distance for first i robots 
        # using first j factory slots.
        # Initialize with a large number (but not float('inf') to avoid overflow issues)
        # 1e15 is safe given constraints (100 robots * 10^9 distance)
        dp = [[10**15] * (m + 1) for _ in range(n + 1)]
        
        # Base case: 0 robots always cost 0 distance
        for j in range(m + 1):
            dp[0][j] = 0
            
        # 4. Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Option A: Skip this factory slot
                # The distance is whatever it was using the previous j-1 slots
                dp[i][j] = dp[i][j-1]
                
                # Option B: Use this factory slot for the i-th robot
                # Current robot's distance + best way to fix i-1 robots with j-1 slots
                current_dist = abs(robot[i-1] - factory_positions[j-1])
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + current_dist)
                
        return dp[n][m]