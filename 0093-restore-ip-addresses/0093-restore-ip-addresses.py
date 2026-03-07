class Solution:
    def restoreIpAddresses(self, s: str):
        res = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start+length]

                if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                    continue

                backtrack(start + length, path + [part])

        backtrack(0, [])
        return res