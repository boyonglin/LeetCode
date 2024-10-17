class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(" ")
        s = [x for x in s if x != ""]
        s.reverse()
        return " ".join(s)

# Testcase
s = "a good   example"

sol = Solution()
print(sol.reverseWords(s))