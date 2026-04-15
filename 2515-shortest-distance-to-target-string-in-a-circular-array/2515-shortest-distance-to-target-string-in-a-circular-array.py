class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = float('inf')
        
        for i in range(n):
            if words[i] == target:
                # Calculate the direct distance between indices
                d = abs(i - startIndex)
                
                # In a circular array, the shortest path is either:
                # 1. The direct distance: d
                # 2. The wrap-around distance: n - d
                current_dist = min(d, n - d)
                
                if current_dist < min_dist:
                    min_dist = current_dist
        
        # Return the result, or -1 if the target was never found
        return min_dist if min_dist != float('inf') else -1
