#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    bool isValid(string s) {
        stack<int> stac;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                stac.push(s[i]);
            } 
            else {
                if (stac.empty()) {
                    return false;
                }
                if (s[i] == ')' && stac.top() != '(') {
                    return false;
                }
                if (s[i] == ']' && stac.top() != '[') {
                    return false;
                }
                if (s[i] == '}' && stac.top() != '{') {
                    return false;
                }
                stac.pop();
            }
        }
        return stac.empty();
    }
};


int main() {
    Solution s;
    string str = "()";
    string str2 = "()[]{}";
    string str3 = "(]";
    cout << s.isValid(str);
    cout << s.isValid(str2);
    cout << s.isValid(str3);
    return 0;
}