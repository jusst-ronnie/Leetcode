class Solution:
    def mirrorDistance(self, n: int) -> int:
        original_n = n
        reversed_n = 0
        
        # Step 1: Reverse the integer mathematically
        temp = n
        while temp > 0:
            digit = temp % 10
            reversed_n = reversed_n * 10 + digit
            temp //= 10
            
        # Step 2: Return the absolute difference
        return abs(original_n - reversed_n)