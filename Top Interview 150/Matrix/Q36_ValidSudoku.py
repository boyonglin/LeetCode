from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sdk_map = {}

        for i in range(9):
            for j in range(9):
                filled = board[i][j]
                if filled != '.':
                    if filled in sdk_map:
                        for coord in sdk_map[filled]:
                            # use residual (0~8 -> 0~2) to defined the 3x3 box
                            if i == coord[0] or j == coord[1] or (i//3 == coord[0]//3 and j//3 == coord[1]//3):
                                return False
                        sdk_map[filled].append((i, j))
                    else:
                        sdk_map[filled] = [(i, j)]

        return True


# Testcase
board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","9","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

sol = Solution()
print(sol.isValidSudoku(board))