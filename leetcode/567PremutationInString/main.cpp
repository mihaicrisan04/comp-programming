#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool equal(vector<int>& m1, vector<int>& m2) {
        for (int i = 0; i < 26; i++) {
            if (m1[i] != m2[i]) return false;
        }
        return true;
    }

    bool checkInclusion(string s1, string s2) {
        
        if (s2.length() < s1.length()) return false;

        vector<int> m1(26, 0), m2(26, 0);
        for (char c: s1) m1[c - 'a']++;

        int l = 0, r = 0;
        while (r < s2.length()) {
            m2[s2[r] - 'a']++;
            if (r - l + 1 == s1.length()) {
                if (equal(m1, m2)) return true;
                m2[s2[l] - 'a']--;
                l++;
            }
            r++;
        }

        return false;
    }
};


int main() {
    Solution s;
    cout << s.checkInclusion("ab", "eidbaooo") << endl;
    cout << s.checkInclusion("ab", "eidboaoo") << endl;
    return 0;
}