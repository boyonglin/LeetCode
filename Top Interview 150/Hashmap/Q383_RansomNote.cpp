#include <stdio.h>
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        std::unordered_map<char, int> hashmap;
        for (int i = 0; i < ransomNote.size(); i++) {
            hashmap[ransomNote[i]]++;
        }

        for (int i = 0; i < magazine.size(); i++) {
            if (hashmap.find(magazine[i]) != hashmap.end()) {
                hashmap[magazine[i]]--;
                if (hashmap[magazine[i]] == 0) {
                    hashmap.erase(magazine[i]);
                    if (hashmap.empty()) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};

int main() {
    string ransomNote = "aa";
    string magazine = "ab";

    Solution sol;
    printf("%s\n", sol.canConstruct(ransomNote, magazine) ? "true" : "false");

    return 0;
}