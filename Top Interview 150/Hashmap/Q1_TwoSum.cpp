#include <stdio.h>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> diff_map;
        vector<int> res;

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];

            // find diff from constructed map
            if (diff_map.find(diff) != diff_map.end()) {
                res.push_back(diff_map[diff]);
                res.push_back(i);
                return res;
            }

            diff_map[nums[i]] = i;
        }

        return res;
    }
};

int main() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    Solution sol;
    vector<int> res = sol.twoSum(nums, target);
    for (int i : res) {
        printf("%d ", i);
    }

    return 0;
}