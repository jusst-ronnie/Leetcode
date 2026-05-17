class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        # --- Disjoint Set Union (DSU) Helper Functions ---
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])  # Path compression
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_root_j = find(j)
            if root_i != root_root_j:
                parent[root_i] = root_root_j

        # --- Initial Setup ---
        # Initially, person 0 and firstPerson know the secret. 
        # We connect them together.
        union(0, firstPerson)
        
        # Group meetings by their timestamp
        # { time: [(person1, person2), (person3, person4), ...] }
        time_groups = {}
        for x, y, t in meetings:
            if t not in time_groups:
                time_groups[t] = []
            time_groups[t].append((x, y))
            
        # Process meetings chronologically
        for t in sorted(time_groups.keys()):
            pool = set()  # Tracks all unique people meeting at this specific time 't'
            
            # Connect people meeting at this time frame
            for x, y in time_groups[t]:
                union(x, y)
                pool.add(x)
                pool.add(y)
                
            # Check who actually got the secret.
            # If a person's root is not connected to person 0's root, 
            # they did NOT learn the secret at this time. We isolate them back.
            secret_root = find(0)
            for person in pool:
                if find(person) != secret_root:
                    parent[person] = person  # Reset their connection
                    
        # --- Gather Results ---
        # Anyone whose component root matches the secret group (root of 0) knows the secret
        secret_root = find(0)
        return [i for i in range(n) if find(i) == secret_root]