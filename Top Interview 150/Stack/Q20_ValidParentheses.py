class Solution:
    def isValid(self, s: str) -> bool:
        close = []

        for symbol in s:
            if symbol =='(':
                close.append(')')
            elif symbol == '[':
                close.append(']')
            elif symbol == '{':
                close.append('}')
            else:
                if not close or close.pop() != symbol:
                    return False

        return True if not close else False

# Testcases
s = "()[]{}"

sol = Solution()
print(sol.isValid(s))