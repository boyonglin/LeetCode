from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(len(strs[0])):
            for l in range(0, len(strs)):
                if i < len(strs[l]) and strs[l][i] == strs[0][i]:
                    if l == len(strs) - 1:
                        prefix += strs[0][i]
                    continue
                else:
                    return prefix
        return prefix

# Testcase
strs = ["cir","car"]

sol = Solution()
print(sol.longestCommonPrefix(strs))