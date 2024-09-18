from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        position_of_zero = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]

        for i, j in position_of_zero:
            for row in range(m):
                matrix[row][j] = 0
            for col in range(n):
                matrix[i][col] = 0

        return matrix


# Testcase
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

sol = Solution()
print(sol.setZeroes(matrix))