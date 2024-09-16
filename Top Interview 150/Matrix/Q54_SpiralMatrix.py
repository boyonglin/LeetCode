from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        res = []

        while matrix:
            # left to right
            res += matrix.pop(0)

            # top to bottom
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())

            # right to left
            if matrix:
                res += matrix.pop()[::-1]

            # bottom to top
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))

        return res

        # m = len(matrix)
        # n = len(matrix[0])

        # if m == 0 or n == 0:
        #     return []

        # dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # d = 0
        # x = 0
        # y = 0

        # res = [matrix[0][0]]
        # matrix[0][0] = None

        # while len(res) < m * n:
        #     x += dir[d][0]
        #     y += dir[d][1]

        #     if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] == None:
        #         x -= dir[d][0]
        #         y -= dir[d][1]
        #         d = (d + 1) % 4
        #     else:
        #         res.append(matrix[x][y])
        #         matrix[x][y] = None

        # return res

# Testcase
matrix = [[1,2,3],[4,5,6],[7,8,9]]

sol = Solution()
print(sol.spiralOrder(matrix))