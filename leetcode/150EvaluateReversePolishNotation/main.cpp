#include<bits/stdc++.h>


using namespace std;


class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;

        for (string s : tokens) {
            if (s == "+" || s == "-" || s == "*" || s == "/") {
                int b = st.top();
                st.pop();
                int a = st.top();
                st.pop();

                int n;
                switch (s[0]) {
                    case '+': n = a + b; break;
                    case '-': n = a - b; break;
                    case '*': n = a * b; break;
                    case '/': n = a / b; break;
                }
                st.push(n);
            }
            else {
                st.push(stoi(s));
            }
        }
        return st.top();
    }
};


int main() {
    Solution s;
    vector<string> tokens = {"2", "1", "+", "3", "*"};
    cout << s.evalRPN(tokens) << endl;
    return 0;
}