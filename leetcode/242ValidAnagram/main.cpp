#include <iostream>
#include <string>
#include <algorithm>

class Solution {
public:
    // O(n + m) time complexity
    bool isAnagram(std::string s, std::string t) {
        if (s.size() != t.size()) {
            return false;
        }
        int count[26] = {0};
        for (int i = 0; i < s.size(); i++) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) {
                return false;
            }
        }
        return true;
    }
    // O(nlogn) time complexity
    // bool isAnagram(std::string s, std::string t) {
    //     std::sort(s.begin(), s.end());
    //     std::sort(t.begin(), t.end());
    //     return s == t;
    // }
};


int main() {
    Solution solution;
    std::string s = "anagram";
    std::string t = "nagaram";
    std::cout << solution.isAnagram(s, t) << std::endl;
    return 0;
}