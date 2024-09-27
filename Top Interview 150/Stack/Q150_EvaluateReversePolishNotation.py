from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []

        for token in tokens:
            if token not in "+-*/":
                num_stack.append(int(token))

# Testcases
tokens = ["2","1","+","3","*"]

sol = Solution()
print(sol.evalRPN(tokens))