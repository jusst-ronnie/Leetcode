class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        # Combine data and sort by position: (pos, health, dir, original_index)
        # This is crucial because collisions happen based on their physical order
        robots = sorted(zip(positions, healths, directions, range(n)))
        
        stack = []     # Stores 'R' moving robots that might collide
        survivors = [] # Stores 'L' moving robots that survived all 'R' collisions
        
        for pos, health, direction, idx in robots:
            if direction == 'R':
                # 'R' moving robots are added to the stack to wait for potential 'L' robots
                stack.append([pos, health, direction, idx])
            else:
                # Robot is moving 'L', check for collisions with 'R' robots in stack
                while stack and health > 0:
                    if stack[-1][1] < health:
                        # 'R' robot in stack is destroyed, 'L' robot loses 1 health
                        stack.pop()
                        health -= 1
                    elif stack[-1][1] > health:
                        # 'L' robot is destroyed, 'R' robot in stack loses 1 health
                        stack[-1][1] -= 1
                        health = 0
                    else:
                        # Both have equal health and are both destroyed
                        stack.pop()
                        health = 0
                
                # If the 'L' robot survives all potential collisions in the stack
                if health > 0:
                    survivors.append([pos, health, direction, idx])
        
        # Combine the remaining 'R' robots from the stack and the 'L' survivors
        remaining = stack + survivors
        
        # Sort by the original index to return healths in the initial input order
        remaining.sort(key=lambda x: x[3])
        
        return [r[1] for r in remaining]
