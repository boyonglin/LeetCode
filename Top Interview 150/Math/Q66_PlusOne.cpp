#include <stdio.h>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        if (digits.empty()) {
            return digits;
        }

        int n = digits.size();
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] == 9) {
                digits[i] = 0;
            } else {
                digits[i]++;
                return digits;
            }
        }

        // the leftmost case
        digits.insert(digits.begin(), 1);
        return digits;
    }
};


int main() {
    vector<int> digits = {9};

    Solution sol;
    vector<int> res = sol.plusOne(digits);
    for (int i : res) {
        printf("%d ", i);
    }

    return 0;
}