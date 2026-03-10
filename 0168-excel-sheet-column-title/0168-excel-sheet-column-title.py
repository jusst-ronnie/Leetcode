class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""

        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result += chr(remainder + ord('A'))
            columnNumber //= 26

        return result[::-1]