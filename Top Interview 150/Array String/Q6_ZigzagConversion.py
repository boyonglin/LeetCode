class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        div = ['' for _ in range(numRows)] # Repeat the whole pattern for numRows times
        row = 0
        step = 1

        for char in s:
            div[row] += char
            row += step
            if row == 0 or row == numRows - 1:
                step *= -1

        return ''.join(div)

# Testcase\
s = "PAYPALISHIRING"
numRows = 3

sol = Solution()
print(sol.convert(s, numRows))