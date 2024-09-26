class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for p in path:
            if p == '..':
                if len(stack) > 0:
                    stack.pop()
            elif p == '.':
                continue
            elif p == '':
                continue
            else:
                stack.append(p)

        path = '/' + '/'.join(stack)
        return path

# Testcases
path = "/home/user///Documents/../Pictures/"

sol = Solution()
print(sol.simplifyPath(path))