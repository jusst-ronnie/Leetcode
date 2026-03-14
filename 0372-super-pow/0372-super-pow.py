class Solution:
    def superPow(self, a: int, b):
        mod = 1337
        result = 1
        
        for digit in b:
            result = (pow(result, 10, mod) * pow(a, digit, mod)) % mod
        
        return result