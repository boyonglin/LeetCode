#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        for (int i = 0; i <= x; i++) {
            long ub = pow(i, 2);

            if (ub > x) {
                return i - 1;
            } else if (ub == x) {
                return i;
            }
        }

        return x;
    }
};

int main() {
    int x = 8;

    Solution sol;
    printf("%d", sol.mySqrt(x));

    return 0;
}