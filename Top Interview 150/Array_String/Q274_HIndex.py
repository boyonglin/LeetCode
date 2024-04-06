from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        citations[:] = sorted(citations, reverse=True)
        for i, c in enumerate(citations, start=1):
            if i < c:
                h += 1
            elif i == c:
                return i
        return h

# Testcase
citations = [3,0,6,1,5]

sol = Solution()
print(sol.hIndex(citations))