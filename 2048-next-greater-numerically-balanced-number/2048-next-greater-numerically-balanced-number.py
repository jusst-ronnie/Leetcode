from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def balanced(x):
            c = Counter(str(x))
            for d in c:
                if c[d] != int(d):
                    return False
            return True
        
        num = n + 1
        while True:
            if balanced(num):
                return num
            num += 1