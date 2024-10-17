#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n);
        int left = 0;
        int right = n - 1;
        int idx = n - 1;

        while (left <= right) {
            if (abs(nums[left]) > abs(nums[right])) {
                res[idx--] = nums[left] * nums[left];
                left++;
            } else {
                res[idx--] = nums[right] * nums[right];
                right--;
            }
        }

        return res;
    }
};

int main() {
    vector<int> nums = {-4,-1,0,3,10};

    Solution sol;
    vector<int> res = sol.sortedSquares(nums);
    for (int i : res) {
        printf("%d ", i);
    }

    return 0;
}