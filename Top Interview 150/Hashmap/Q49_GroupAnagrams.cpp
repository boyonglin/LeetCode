#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> unimap;
        vector<vector<string>> res;

        for (string s : strs) {
            string key = s;
            sort(key.begin(), key.end());
            unimap[key].push_back(s);
        }

        for (auto it : unimap) {
            res.push_back(it.second);  // pair: key, value
        }

        return res;
    }
};

int main() {
    vector<string> strs = {"eat","tea","tan","ate","nat","bat"};

    Solution sol;
    vector<vector<string>> res = sol.groupAnagrams(strs);
    for (vector<string> v: res) {
        for (string s: v) {
            printf("%s ", s.c_str());
        }
        printf("\n");
    }

    return 0;
}