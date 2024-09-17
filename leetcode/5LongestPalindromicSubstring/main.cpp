#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int maxStart = 0;
        int maxLength = 1;

        for (int i = 0; i < s.size(); i++) {        
            expand(s, i, i, maxLength, maxStart); // for palindromes of form "aba"
            expand(s, i, i+1, maxLength, maxStart); // for palindormes of form "abba"
        }

        return s.substr(maxStart, maxLength);
    }
private:
    void expand(string s, int i, int j, int& maxLength, int& maxStart) {
        while (i >= 0 && j < s.size() && s[i] == s[j]) {
            i--;
            j++;
        }
        // <|      |>
        // "iaabbaaj" formula for length = j - i + 1 but i and j are both outside so we must subtract -2
        // end formula for actual palindrome = j - i + 1 - 2 => j - i - 1
        if (j - i - 1 > maxLength) {
            maxStart = i + 1;
            maxLength = j - i - 1;
        }
    }
};


int main() {
    Solution s;
    string str = "babad";
    cout << s.longestPalindrome(str) << endl;
    str = "cbbd";
    cout << s.longestPalindrome(str) << endl;
    return 0;
}