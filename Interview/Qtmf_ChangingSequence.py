class Solution:
    def changingSequence(self, array):
        head = array[0]
        next = array[1]

        if next > head:
            for i in range(1, len(array)):
                if array[i] <= array[i-1]:
                    return i - 1
        else:
            for i in range(1, len(array)):
                if array[i] >= array[i-1]:
                    return i - 1

        return -1

# Testcases
array = [1,2,4,8,4,2]

sol = Solution()
print(sol.changingSequence(array))