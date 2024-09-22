#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        unordered_map<int, int> unimap;

        for (int u : s) {
            unimap[u]++;
        }

        for (int u : t) {
            // if u was not in the map, unimap[u] would be initialized to 0
            if (--unimap[u] < 0) {
                return false;
            }
        }

        return true;
    }
};

int main() {
    string s = "anagram";
    string t = "nagaram";

    Solution sol;
    printf("%s\n", sol.isAnagram(s, t) ? "true" : "false");

    return 0;
}