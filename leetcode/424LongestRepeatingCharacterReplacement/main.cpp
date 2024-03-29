#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int characterReplacement(string s, int k) {
        int f[26] = {0};
        int l = 0, r = 0, maxCount = 0, ans = 0;
        while (r < s.length()) {
            f[s[r] - 'A']++;
            maxCount = max(maxCount, f[s[r] - 'A']);
            if (r - l + 1 > maxCount + k) {
                f[s[l++] - 'A']--; 
            }
            ans = max(r - l + 1, ans);
            r++;
        }
        return ans;
    }    
};


int main() {
    Solution s;
    cout << s.characterReplacement("ABAB", 2) << endl;
    cout << s.characterReplacement("AABABBA", 1) << endl;
    return 0;
}