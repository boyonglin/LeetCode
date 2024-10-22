#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int missing = 0;

        for (int i = 0; i < nums.size(); i++) {
            missing += i;
            missing -= nums[i];
        }

        missing += n;

        return missing;
    }
};

int main() {
    vector<int> nums = {3, 0, 1};

    Solution sol;
    printf("%d", sol.missingNumber(nums));

    return 0;
}