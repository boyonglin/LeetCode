from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        res = 0

        if len(tokens) == 1:
            return int(tokens[0])

        for t in tokens:
            if t not in '+-*/':
                num_stack.append(int(t))
            else:
                a = num_stack.pop()
                b = num_stack.pop()

                if t == '+':
                    res = b + a
                elif t == '-':
                    res = b - a
                elif t == '*':
                    res = b * a
                else:
                    res = int(b / a)

                num_stack.append(res)

        return res

# Testcases
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

sol = Solution()
print(sol.evalRPN(tokens))