class Solution:
    def hasSameDigits(self, s: str) -> bool:
        arr = [int(c) for c in s]

        while len(arr) > 2:
            new = []
            for i in range(len(arr) - 1):
                new.append((arr[i] + arr[i+1]) % 10)
            arr = new

        return arr[0] == arr[1]