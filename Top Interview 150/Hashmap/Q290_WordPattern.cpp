#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> pattern_map;
        unordered_map<string, char> word_map;

        stringstream ss(s);
        string word;
        vector<string> words;

        // extracts until encounters a whitespace character
        while (ss >> word) {
            words.push_back(word);
        }

        if (pattern.size() != words.size()) {
            return false;
        }

        for (int i = 0; i < pattern.size(); i++) {
            char p_char = pattern[i];
            string word = words[i];

            if (pattern_map.find(p_char) == pattern_map.end()) {
                pattern_map[p_char] = word;
            } else {
                if (pattern_map[p_char] != word) {
                    return false;
                }
            }

            if (word_map.find(word) == word_map.end()) {
                word_map[word] = p_char;
            } else {
                if (word_map[word] != p_char) {
                    return false;
                }
            }
        }

        return true;
    }
};

int main() {
    string pattern = "jquery";
    string s = "jquery";

    Solution sol;
    printf("%s\n", sol.wordPattern(pattern, s) ? "true" : "false");

    return 0;
}