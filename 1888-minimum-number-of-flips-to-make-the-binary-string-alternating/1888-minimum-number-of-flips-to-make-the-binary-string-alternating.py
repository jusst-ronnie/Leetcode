class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ss = s + s
        
        alt1 = ""
        alt2 = ""
        
        for i in range(2*n):
            if i % 2 == 0:
                alt1 += "0"
                alt2 += "1"
            else:
                alt1 += "1"
                alt2 += "0"
        
        res = float('inf')
        diff1 = diff2 = 0
        l = 0
        
        for r in range(2*n):
            if ss[r] != alt1[r]:
                diff1 += 1
            if ss[r] != alt2[r]:
                diff2 += 1
            
            if r - l + 1 > n:
                if ss[l] != alt1[l]:
                    diff1 -= 1
                if ss[l] != alt2[l]:
                    diff2 -= 1
                l += 1
            
            if r - l + 1 == n:
                res = min(res, diff1, diff2)
        
        return res