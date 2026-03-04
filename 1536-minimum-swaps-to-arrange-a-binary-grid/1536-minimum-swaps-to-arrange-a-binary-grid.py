class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        
        # Step 1: Count trailing zeros
        trailing = []
        
        for row in grid:
            count = 0
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0
        
        # Step 2: Try fixing each row
        for i in range(n):
            required = n - i - 1
            j = i
            
            # Find row with enough trailing zeros
            while j < n and trailing[j] < required:
                j += 1
            
            if j == n:
                return -1
            
            # Bring row j to position i
            while j > i:
                trailing[j], trailing[j-1] = trailing[j-1], trailing[j]
                swaps += 1
                j -= 1
        
        return swaps