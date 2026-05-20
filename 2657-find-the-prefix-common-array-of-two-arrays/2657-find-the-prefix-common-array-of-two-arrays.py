class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        n = len(A)
        C = [0] * n
        # Since numbers are from 1 to n, a size n + 1 array works perfectly
        freq = [0] * (n + 1)
        common_count = 0
        
        for i in range(n):
            # Process element from A
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common_count += 1
                
            # Process element from B
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common_count += 1
                
            # Store the current running tally for index i
            C[i] = common_count
            
        return C
