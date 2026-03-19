class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        temp = s + "#" + rev
        
        # Build LPS array
        lps = [0] * len(temp)
        
        j = 0
        for i in range(1, len(temp)):
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]
            
            if temp[i] == temp[j]:
                j += 1
                lps[i] = j
        
        # length of longest palindrome prefix
        length = lps[-1]
        
        # add remaining reversed part in front
        return rev[:len(s) - length] + s