class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        
        # A shift of k is the same as k % n
        k %= n
        
        # If k is 0 or a multiple of the row length, it's always identical
        if k == 0:
            return True
            
        for i in range(m):
            for j in range(n):
                # Check if current element matches the element k positions away
                if mat[i][j] != mat[i][(j + k) % n]:
                    return False
        
        # Return True only after checking ALL elements
        return True