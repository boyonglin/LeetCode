class Solution:
    def calculate(self, s: str) -> int:
        num_stack = []
        op_stack = []
        num = 0
        sign = 1
        res = 0

        i = 0

        while i < len(s):
            char = s[i]

            # multi-digit numbers
            if char.isdigit():
                num = 0

                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                res += sign * num
                continue

            elif char == '+':
                sign = 1

            elif char == '-':
                sign = -1

            elif char == '(':
                num_stack.append(res)
                op_stack.append(sign)
                res = 0
                sign = 1

            elif char == ')':
                res *= op_stack.pop()
                res += num_stack.pop()

            i += 1

        return res


# Testcases
s = "(1+(4+5+2)-3)+(6+8)"

sol = Solution()
print(sol.calculate(s))