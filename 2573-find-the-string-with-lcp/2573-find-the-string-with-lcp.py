class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        n = len(lcp)
        # Using a simple array for groups to save time over full Union-Find
        # though Union-Find is also valid.
        res = [None] * n
        curr_char_code = ord('a')

        # 1. Assign characters based on lcp[i][j] > 0
        for i in range(n):
            if res[i] is not None:
                continue
            if curr_char_code > ord('z'):
                return ""
            
            char = chr(curr_char_code)
            for j in range(i, n):
                if lcp[i][j] > 0:
                    res[j] = char
            curr_char_code += 1

        # Check if any index was missed (shouldn't happen with lcp[i][i] > 0)
        if None in res:
            return ""
            
        word = "".join(res)

        # 2. Validation: The LCP matrix must match the generated word exactly
        # We build a temporary LCP table to compare.
        actual_lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    actual_lcp[i][j] = actual_lcp[i + 1][j + 1] + 1
                else:
                    actual_lcp[i][j] = 0
                
                # Check against input matrix immediately
                if actual_lcp[i][j] != lcp[i][j]:
                    return ""
                    
        return word