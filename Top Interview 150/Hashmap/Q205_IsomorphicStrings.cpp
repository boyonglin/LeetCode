#include <stdio.h>
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        std::unordered_map<char, int> iso_map;

        for (int i = 0; i < s.size(); i++) {
            if (iso_map.find(s[i]) == iso_map.end()) {
                iso_map[s[i]] = t[i];
            } else {
                // same s char should map to same t char
                if (iso_map[s[i]] != t[i]) {
                    return false;
                }
            }
        }

        iso_map.clear();

        for (int i = 0; i < t.size(); i++) {
            if (iso_map.find(t[i]) == iso_map.end()) {
                iso_map[t[i]] = s[i];
            } else {
                if (iso_map[t[i]] != s[i]) {
                    return false;
                }
            }
        }

        return true;
    }
};

int main() {
    string s = "badc";
    string t = "baba";

    Solution sol;
    printf("%s\n", sol.isIsomorphic(s, t) ? "true" : "false");

    return 0;
}