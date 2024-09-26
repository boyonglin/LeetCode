
class Solution:
    def missingWords(self, s, t):
        s = s.split(' ')
        t = t.split(' ')
        ts = 0
        res = []

        for ss in s:
            if ts < len(t) and ss == t[ts]:
                ts += 1
            else:
                res.append(ss)

        return res

# Testcases
s = "I am using HackerRank to improve programming"
t = "am HackerRank to improve"

sol = Solution()
print(sol.missingWords(s, t))