class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        # Base case: If index is out of bounds or already visited, return False
        if start < 0 or start >= len(arr) or arr[start] < 0:
            return False
        
        # If we find a target index with value 0, we reached our goal
        if arr[start] == 0:
            return True
        
        # Mark the current index as visited by making it negative
        arr[start] = -arr[start]
        
        # Recursively check the two possible choices: jump forward or backward
        jump_distance = abs(arr[start])
        
        forward = self.canReach(arr, start + jump_distance)
        backward = self.canReach(arr, start - jump_distance)
        
        return forward or backward