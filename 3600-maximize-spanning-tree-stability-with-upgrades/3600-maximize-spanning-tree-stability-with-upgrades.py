class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.components -= 1
            return True
        return False

class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        def can_form_tree(threshold):
            dsu = DSU(n)
            edges_used = 0
            
            # 1. Handle Mandatory Edges first
            # These MUST be included and cannot be upgraded.
            for u, v, s, m in edges:
                if m == 1:
                    if s < threshold: 
                        return False  # A required edge fails the stability check
                    if not dsu.union(u, v): 
                        return False  # Mandatory edges form a cycle
                    edges_used += 1
            
            # 2. Add Optional Edges that satisfy threshold WITHOUT upgrade
            for u, v, s, m in edges:
                if m == 0 and s >= threshold:
                    if dsu.union(u, v):
                        edges_used += 1
            
            # 3. Add Optional Edges that satisfy threshold WITH upgrade
            upgrades_left = k
            for u, v, s, m in edges:
                if m == 0 and s < threshold <= 2 * s:
                    if upgrades_left > 0:
                        if dsu.union(u, v):
                            edges_used += 1
                            upgrades_left -= 1
            
            # A valid spanning tree must connect all nodes (1 component) 
            # and have exactly n-1 edges.
            return dsu.components == 1 and edges_used == n - 1

        # Binary Search for the maximum minimum strength
        low = 1
        # Max strength is 10^5, so max upgraded strength is 2*10^5
        high = 200000 
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_form_tree(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans