class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = filter(str.isalnum, s) # remove non-alphanumeric chars
        s = ''.join(s).lower()

        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
            else:
                return True

# Testcase
s = "A man, a plan, a canal: Panama"

sol = Solution()
print(sol.isPalindrome(s))