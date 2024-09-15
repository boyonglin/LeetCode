class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if m < n:
            return ""

        t_count = {}
        for c in t:
            if c in t_count:
                t_count[c] += 1
            else:
                t_count[c] = 1

        s_count = {}
        required = len(t_count)
        formed = 0

        l = 0
        r = 0
        min_len = float('inf')
        min_window = ""

        while r < m:
            if s[r] in t_count:
                s_count[s[r]] = s_count.get(s[r], 0) + 1

                if s_count[s[r]] == t_count[s[r]]:
                    formed += 1

            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = s[l:r + 1]

                if s[l] in t_count:
                    s_count[s[l]] -= 1
                    if s_count[s[l]] < t_count[s[l]]:
                        formed -= 1

                l += 1

            r += 1

        return min_window

# Testcase
s = "ADOBECODEBANC"
t = "ABC"

sol = Solution()
print(sol.minWindow(s, t))