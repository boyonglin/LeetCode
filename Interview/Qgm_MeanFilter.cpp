#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<double> meanFilter(vector<int>& nums, int k) {
        int n = nums.size();
        vector<double> res(n, 0);

        for (int i = 0; i < n; i++) {
            double sum = 0;  // to avoid integer division
            int count = 0;

            for (int j = i - k; j <= i + k; j++) {
                if (j >= 0 && j < n) {
                    sum += nums[j];
                    count++;
                }
            }

            res[i] = round((sum / count) * 100) / 100.0;
        }

        return res;
    }
};

int main() {
    vector<int> nums = {1, 2, 3, 5, 6, 7};
    int k = 1;

    Solution sol;
    vector<double> res = sol.meanFilter(nums, k);
    for (double i : res) {
        printf("%.2f ", i);
    }

    return 0;
}