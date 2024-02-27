#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        int ans = 0;
        unordered_map<char, int> map;
        for (int j = 0, i = 0; i < n; i++) {
            if (map.find(s[i]) != map.end()) { // if s[i] is in the map
                j = max(map[s[i]], j); // j = pos(s[i]) + 1
            }
            ans = max(ans, i - j + 1); // calculate the length of the substring at each iteration
            map[s[i]] = i + 1; // update the position of s[i] in the map
        }
        return ans;

        // end - start + 1 at each iteration
        // if end is in the map, start gets a position that will not contain the same
        // character as end, position which is last end position + 1
        // update the position of end in the map
    }
};


int main() {
    Solution s;
    string str = "abcabcbb";
    cout << s.lengthOfLongestSubstring(str) << endl;
    str = "bbbbb";
    cout << s.lengthOfLongestSubstring(str) << endl;
    str = "pwwkew";
    cout << s.lengthOfLongestSubstring(str) << endl;
    return 0;
}