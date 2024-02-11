#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    bool isPalindrome(string s) {
        string fs = "";
        for (auto c: s) {
            if (c >= 'a' && c <= 'z') {
                fs += c;
            }
            if (c >= 'A' && c <= 'Z') {
                fs += (c + 'a' - 'A');
            }
            if (c >= '0' && c <= '9') {
                fs += c;
            }
        }
        int l = 0, r = fs.size() - 1;
        while (l < r) {
            if (fs[l] != fs[r]) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
};


int main() {
    Solution s;
    string str = "A man, a plan, a canal: Panama";
    string str2 = "0P";
    cout << s.isPalindrome(str) << endl;
    cout << s.isPalindrome(str2) << endl;
    return 0;
}