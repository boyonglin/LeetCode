// 4o

#include <iostream>
#include <stdio.h>
using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;

        // handle n < 0
        double res = 1;
        long long N = n;  // prevent overflow
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }

        // Exponentiation by Squaring
        // x^n = (x^2) ^ (n/2), if n is even
        // x^n = x * x^(n-1), if n is odd

        while (N > 0) {
            if (N % 2 == 1) {
                res *= x;
            }

            x *= x;
            N /= 2;
        }

        return res;
    }
};

int main() {
    double x = 2.00000;
    int n = 10;

    Solution sol;
    printf("%f\n", sol.myPow(x, n));

    return 0;
}