class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        num_rows = len(strs)
        num_cols = len(strs[0])
        delete_count = 0
        
        # Iterate through each column
        for col in range(num_cols):
            # Check characters vertically down the rows
            for row in range(1, num_rows):
                if strs[row][col] < strs[row - 1][col]:
                    # The column is not lexicographically sorted
                    delete_count += 1
                    break  # No need to check the rest of this column
                    
        return delete_count