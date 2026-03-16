from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        q = deque([s])
        ans = s

        while q:
            cur = q.popleft()
            ans = min(ans, cur)

            if cur in visited:
                continue
            visited.add(cur)

            # Operation 1: add to odd indices
            arr = list(cur)
            for i in range(1, len(arr), 2):
                arr[i] = str((int(arr[i]) + a) % 10)
            add_op = "".join(arr)

            if add_op not in visited:
                q.append(add_op)

            # Operation 2: rotate right
            rot = cur[-b:] + cur[:-b]

            if rot not in visited:
                q.append(rot)

        return ans