#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        int n = s.size();
        string res = "";
        int i = 0;        
        while (i < n) {
            string word = "";
            while (s[i] == ' ' && i < n) i++;
            while (s[i] != ' ' && i < n) word += s[i], i++;
            if (word.size() > 0) 
                if (res.size() == 0) res = word;
                else res = word + " " + res;
        }
        return res;
    }
};


int main() {
    Solution s;
    string str = "the sky is blue"; 
    str = "  hello world  ";
    cout << s.reverseWords(str) << endl;
    return 0;
}