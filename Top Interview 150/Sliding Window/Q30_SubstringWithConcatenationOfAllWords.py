from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        m = len(words[0])
        window = m * len(words)
        result = []

        words_count = {}
        for word in words:
            words_count[word] = words_count.get(word, 0) + 1 # if word not in words_count, get 0 and add 1

        for i in range(n - window + 1):
            word = s[i:i + m]
            if word not in words:
                continue

            sub = s[i:i + window]
            split = [sub[j:j + m] for j in range(0, window, m)]

            split_count = {}
            for word in split:
                if word in words_count:
                    split_count[word] = split_count.get(word, 0) + 1
                else:
                    break

            if split_count == words_count:
                result.append(i)

        return result

# Testcase
s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]

sol = Solution()
print(sol.findSubstring(s, words))