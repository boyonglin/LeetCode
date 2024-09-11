from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []
        result = []
        width = 0

        for word in words:
            width += len(word)
            if width <= maxWidth:
                line.append(word)
                width += 1
            else:
                result.append(line)
                line = [word]
                width = len(word) + 1

        result.append(line)

        for i in range(len(result)):
            space = maxWidth - sum(len(word) for word in result[i])
            for j in range(space):
                if i == len(result) - 1 and j >= len(result[i]) - 1: # last line
                    result[i][-1] += ' '
                elif len(result[i]) > 1:
                    result[i][j % (len(result[i]) - 1)] += ' ' # separate spaces one by one
                else:
                    result[i][0] += ' '

            result[i] = ''.join(result[i])

        return result

# Testcase
words = words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do","do"]
maxWidth = 20

sol = Solution()
print(sol.fullJustify(words, maxWidth))