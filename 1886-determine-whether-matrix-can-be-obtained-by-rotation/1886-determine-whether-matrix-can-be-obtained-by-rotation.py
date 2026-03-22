class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        # Helper to rotate the matrix 90 degrees clockwise in-place
        def rotate(matrix):
            n = len(matrix)
            # Step 1: Transpose (Swap mat[i][j] with mat[j][i])
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # Step 2: Reverse each row
            for i in range(n):
                matrix[i].reverse()

        # Check all 4 possible rotations (0, 90, 180, 270)
        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)
            
        return False # This must be OUTSIDE the for loop