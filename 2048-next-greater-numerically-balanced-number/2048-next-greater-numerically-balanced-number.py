class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(num: int) -> bool:
            # Convert to string to count digit occurrences
            s = str(num)
            # If '0' is present, it can't be balanced (0 must occur 0 times)
            if '0' in s:
                return False
            
            from collections import Counter
            counts = Counter(s)
            
            for digit_char, count in counts.items():
                if int(digit_char) != count:
                    return False
            return True

        # Increment from n + 1 until we find a match
        curr = n + 1
        while True:
            if is_balanced(curr):
                return curr
            curr += 1