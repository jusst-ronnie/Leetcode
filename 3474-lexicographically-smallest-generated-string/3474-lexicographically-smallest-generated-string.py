class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        res_len = n + m - 1
        res = [None] * res_len
        
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if res[i + j] is not None and res[i + j] != str2[j]:
                        return ""
                    res[i + j] = str2[j]
        
        def is_valid(idx):
            start = max(0, idx - m + 1)
            end = min(n - 1, idx)
            for i in range(start, end + 1):
                if str1[i] == 'F':
                    match = True
                    for j in range(m):
                        if res[i + j] is None or res[i + j] != str2[j]:
                            match = False
                            break
                    if match:
                        return False
            return True

        for i in range(res_len):
            if res[i] is None:
                res[i] = 'a'
                if not is_valid(i):
                    res[i] = 'b'
                    if not is_valid(i):
                        return ""
        
        candidate = "".join(res)
        for i in range(n):
            if str1[i] == 'F' and candidate[i : i + m] == str2:
                return ""
                
        return candidate