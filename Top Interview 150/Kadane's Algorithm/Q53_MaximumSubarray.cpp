#include <stdio.h>
#include <vector>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_ending_here = 0;
        int result = -10000;

        for (int num : nums) {
            if (max_ending_here < 0) {
                max_ending_here = 0;
            }

            max_ending_here += num;
            result = max(result, max_ending_here);
        }

        return result;
    }
};

int main() {
    vector<int> nums = {-1};

    Solution sol;
    printf("%d", sol.maxSubArray(nums));

    return 0;
}