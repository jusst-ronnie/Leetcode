class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        res = []
        
        # We start from each column in the first row (row 0)
        for i in range(cols):
            curr_row = 0
            curr_col = i
            
            # Follow the diagonal until we run out of rows or columns
            while curr_row < rows and curr_col < cols:
                # Calculate the 1D index
                index = curr_row * cols + curr_col
                res.append(encodedText[index])
                
                # Move to the next diagonal element
                curr_row += 1
                curr_col += 1
                
        # Join and remove trailing spaces as per instructions
        return "".join(res).rstrip()