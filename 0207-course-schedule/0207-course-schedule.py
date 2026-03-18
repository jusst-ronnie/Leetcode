from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build Adjacency List and In-Degree array
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1
            
        # 2. Add all courses with NO prerequisites to the queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        processed_count = 0
        
        # 3. BFS (Kahn's Algorithm)
        while queue:
            course = queue.popleft()
            processed_count += 1
            
            # For each course that depends on this current course
            for neighbor in adj[course]:
                in_degree[neighbor] -= 1
                # If all prerequisites for 'neighbor' are met
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 4. If we processed all courses, no cycle exists
        return processed_count == numCourses