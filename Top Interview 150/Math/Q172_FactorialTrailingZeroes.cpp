#include <stdio.h>
#include <vector>
using namespace std;

class Solution {
public:
    int trailingZeroes(int n) {
        int zeros = 0;
        while (n > 0) {
            n /= 5;
            zeros += n;
        }

        return zeros;
    }
};

int main() {
    int n = 5;

    Solution sol;
    printf("%d", sol.trailingZeroes(n));

    return 0;
}