#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sumLeft = 0;
        int sumRight = 0;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            sumRight += nums[i];
        }

        for (int i = 0; i < n; i++) {
            sumRight -= nums[i];
            if (sumLeft == sumRight) {
                return i;
            }
            sumLeft += nums[i];
        }

        return -1;
    }
};

int main() {
    vector<int> nums = {1,7,3,6,5,6};

    Solution sol;
    printf("%d\n", sol.pivotIndex(nums));

    return 0;
}