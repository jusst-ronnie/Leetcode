from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        # Step 1: Map bottom pairs to possible top blocks
        adj = defaultdict(list)
        for pattern in allowed:
            adj[pattern[:2]].append(pattern[2])
        
        memo = {}

        def solve(current_row):
            # Base case: We reached the top
            if len(current_row) == 1:
                return True
            
            if current_row in memo:
                return memo[current_row]
            
            # Generate all possible next rows
            next_rows = []
            
            # This helper builds all valid 'next row' strings for the current row
            def build_next_row(idx, path):
                if idx == len(current_row) - 1:
                    next_rows.append("".join(path))
                    return
                
                pair = current_row[idx:idx+2]
                if pair in adj:
                    for top in adj[pair]:
                        path.append(top)
                        build_next_row(idx + 1, path)
                        path.pop() # Backtrack

            build_next_row(0, [])
            
            # Try each possible next row
            for nxt in next_rows:
                if solve(nxt):
                    memo[current_row] = True
                    return True
            
            memo[current_row] = False
            return False

        return solve(bottom)
