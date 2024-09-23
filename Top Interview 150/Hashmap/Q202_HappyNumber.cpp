#include <stdio.h>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        map<int, int> loop_map;

        while (n != 1) {
            int sum = 0;

            // square and sum each digit
            while (n > 0) {
                int digit = n % 10;
                sum += digit * digit;
                n /= 10;
            }

            //  record appeared numbers (4 > 16 > 37 > 58 > 89 > 145 > 42 > 20 > 4)
            if (loop_map.find(sum) != loop_map.end()) {
                return false;
            }

            loop_map[sum] = 1;
            n = sum;
        }

        return true;
    }
};

int main() {
    int n = 19;

    Solution sol;
    printf("%s\n", sol.isHappy(n) ? "true" : "false");

    return 0;
}