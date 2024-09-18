#include <stdio.h>
#include <vector>
using namespace std;

class Solution {
public:
    void gameOfLife(vector<vector<int>> &board) {
        int m = board.size();
        int n = board[0].size();

        vector<vector<int>> newBoard(m, vector<int>(n, 0));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int count = 0;

                for (int x = -1; x <= 1; x++) {
                    for (int y = -1; y <= 1; y++) {

                        if (x == 0 && y == 0)
                            continue;

                        if (i + x >= 0 && i + x < m && j + y >= 0 && j + y < n) {
                            count += board[i + x][j + y];
                        }
                    }
                }

                switch (count) {
                    case 2:
                        newBoard[i][j] = board[i][j];
                        break;

                    case 3:
                        newBoard[i][j] = 1;
                        break;

                    default:
                        newBoard[i][j] = 0;
                        break;
                }
            }
        }

        board = newBoard;
    }
};

int main() {
    vector<vector<int>> board = {{0, 1, 0}, {0, 0, 1}, {1, 1, 1}, {0, 0, 0}};
    Solution sol;
    sol.gameOfLife(board);
    
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            printf("%d ", board[i][j]);
        }
        printf("\n");
    }

    return 0;
}