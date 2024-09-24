#include <stdio.h>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> near_map;

        for (int i = 0; i < nums.size(); i++) {
            int n = nums[i];
            if (near_map.find(n) != near_map.end()) {
                if (abs(near_map[n] - i) <= k) {
                    return true;
                }
            }
            near_map[n] = i;
        }

        return false;
    }
};

int main() {
    vector<int> nums = {1,2,3,1,2,3};
    int k = 2;

    Solution sol;
    printf("%s\n", sol.containsNearbyDuplicate(nums, k) ? "true" : "false");

    return 0;
}