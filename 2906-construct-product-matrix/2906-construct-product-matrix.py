class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        MOD = 12345
        p = [[0] * m for _ in range(n)]
        
        # Step 1: Forward pass for Prefix Products
        current_product = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = current_product
                current_product = (current_product * grid[i][j]) % MOD
                
        # Step 2: Backward pass for Suffix Products
        current_product = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = (p[i][j] * current_product) % MOD
                current_product = (current_product * grid[i][j]) % MOD
                
        return p