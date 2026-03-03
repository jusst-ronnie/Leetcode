class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        
        d = endPos - startPos
        
        # Impossible cases
        if abs(d) > k or (k + d) % 2 != 0:
            return 0
        
        r = (k + d) // 2
        
        # Compute nCr using iterative method
        res = 1
        for i in range(r):
            res = res * (k - i) // (i + 1)
        
        return res % MOD