#include <stdio.h>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> num_set;
        for (int num : nums) {
            num_set.insert(num);
        }

        int longest = 0;
        for (int num : num_set) {
            int small = num - 1;

            // if true, num can't be the start of a sequence
            // if false, num is the start of a sequence
            if (num_set.find(small) == num_set.end()) {
                int start = num;
                int len = 1;

                while (num_set.find(start + 1) != num_set.end()) {
                    start++;
                    len++;
                }

                longest = max(longest, len);
            }
        }

        return longest;
    }
};

int main() {
    vector<int> nums = {100,4,200,1,3,2};

    Solution sol;
    printf("%d\n", sol.longestConsecutive(nums));

    return 0;
}