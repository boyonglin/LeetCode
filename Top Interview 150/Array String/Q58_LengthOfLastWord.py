class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])

# Testcase
s = "   fly me   to   the moon  "

sol = Solution()
print(sol.lengthOfLastWord(s))