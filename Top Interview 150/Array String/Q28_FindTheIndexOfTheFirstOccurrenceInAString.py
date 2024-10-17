class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i + len(needle)] == needle:
                    return i

        return -1

        # for i in range(len(haystack) - len(needle) + 1):
        #     if haystack[i:i + len(needle)] == needle:
        #         return i

# Testcase
haystack = "sadbutsad"
needle = "sad"

sol = Solution()
print(sol.strStr(haystack, needle))